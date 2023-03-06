# scrapy_parser_pep

Проект создан с использование фреймворка Scrapy.
Проект проводит парсинг страницы "https://peps.python.org/". Сохраняет список документов PEP.
Собирает данные о количестве и статусе документов PEP. Результат работы сохраняется в CSV-файлы.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt

## Примеры использования проекта:


```

Запуск парсера:

```
scrapy crawl pep
```

