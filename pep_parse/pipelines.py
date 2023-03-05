import csv
from datetime import datetime
from pep_parse.settings import BASE_DIR

TIME_FORMAT = "%Y-%m-%dT%H-%M-%S"
RESULT_DIR = "results"


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_statuses = {}
        self.total = 0

    def process_item(self, item, spider):
        if item["status"] not in self.pep_statuses:
            self.pep_statuses[item["status"]] = 1
        else:
            self.pep_statuses[item["status"]] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        now = datetime.now()
        now_formatted = now.strftime(TIME_FORMAT)
        file_name = f"status_summary_{now_formatted}.csv"
        file_path = BASE_DIR / RESULT_DIR / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            writer = csv.writer(f, dialect="unix")
            writer.writerow(("Статус", "Количество"))
            writer.writerows(self.pep_statuses.items())
            writer.writerow(("Total", self.total))
