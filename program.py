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
    good_updates = []
    good_updates_middle_numbers = []
    bad_updates = []
    bad_updates_middle_numbers = []

    for update in update_pages:
        if not is_correct_order(update, page_rules):
            bad_updates.append(update)

    for update in update_pages:
        if is_correct_order(update, page_rules):
            good_updates.append(update)

    for update in good_updates:
        length = len(update)
        middle_index = length // 2
        good_updates_middle_numbers.append(update[middle_index])
    total = 0
    for middle_number in good_updates_middle_numbers:
        total += middle_number

    for update in bad_updates:
        correct_order(update, page_rules)

    for update in bad_updates:
        length = len(update)
        middle_index = length // 2
        bad_updates_middle_numbers.append(update[middle_index])
    bad_total = 0
    for middle_number in bad_updates_middle_numbers:
        bad_total += middle_number

    print(bad_total)
    print(len(update_pages))
    print(len(good_updates))
    print(len(bad_updates))


def is_correct_order(update: list[int], rules: list[list[int]]) -> bool:
    """checks an update against rules"""
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


def correct_order(update, rules) -> None:
    """corrects the order"""
    while not is_correct_order(update, rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    first_index = update.index(rule[0])
                    second_index = update.index(rule[1])
                    temp = update[first_index]
                    update[first_index] = update[second_index]
                    update[second_index] = temp
