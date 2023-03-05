import re
import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        urls_list = response.css('section[id="numerical-index"] tr')
        for url in urls_list:
            pep_url = url.css("td a::attr(href)").get()
            if pep_url is not None:
                yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        pattern = r"PEP (?P<pep_number>\d+) – (?P<pep_name>.*)"
        full_name = response.css("h1.page-title::text").get()
        pep_name_match = re.search(pattern, full_name)
        number, name = pep_name_match.groups()
        status = (
            response.css('dt:contains("Status:") + dd').css("abbr::text").get()
        )
        data = {"number": number, "name": name, "status": status}
        yield PepParseItem(data)
