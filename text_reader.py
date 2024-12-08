"""text reader module"""


class TextReader:
    """text reader class"""

    def read_data_vertical_line_split(self, filename: str) -> list[list[int]]:
        """read data and split |"""
        list_of_data_lists = []
        with open(filename, "r") as f:
            for line in f:
                stripped = line.strip()
                split_list = stripped.split("|")
                inted_list = []
                for item in split_list:
                    inted_list.append(int(item))
                list_of_data_lists.append(inted_list)
        return list_of_data_lists
