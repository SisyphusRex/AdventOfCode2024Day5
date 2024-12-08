"""program module"""

# System Imports

# First Party Imports
from text_reader import TextReader
from csv_reader import CSVReader

# Third Party Imports

UPDATE_PAGES_FILE = "update_pages.csv"
PAGE_RULES_FILE = "page_rules.txt"


def main(*args):
    """main method"""
    my_text_reader = TextReader()
    my_csv_reader = CSVReader()

    page_rules = my_text_reader.read_data_vertical_line_split(PAGE_RULES_FILE)
    update_pages = my_csv_reader.read_csv(UPDATE_PAGES_FILE)

    # print(page_rules)
    # print(update_pages)


def is_correct_order(update: list[int], rules: list[list[int]]) -> bool:
    """checks an update against rules"""
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0])