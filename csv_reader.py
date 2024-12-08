"""csv reader module"""

# System imports
import csv

# First Party Imports

# Third Party Imports


class CSVReader:
    """csv reaer class"""

    def read_csv(self, filename) -> list[list[int]]:
        """read csv"""
        list_of_data_lists = []
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)

            for line in csv_reader:
                inted_line = []
                for item in line:
                    inted_line.append(int(item))
                list_of_data_lists.append(inted_line)

        return list_of_data_lists
