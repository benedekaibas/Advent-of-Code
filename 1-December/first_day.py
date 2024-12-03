"""First day of Code of Advent."""

from typing import List


class AdventOfCode():
    """Class for containing the necessary functions."""
   
    def __init__(self, path):
        self.path = path
        self.list_one = []
        self.list_two = []

    def open_file(self):
        """Open the input file that contains the IDs."""
        with open(self.path, "r") as file:
            return file.read()
    
    def organize_data(self):
        """Organize the data from the input.txt file."""
        self.list_one = []
        self.list_two = []
        content = self.open_file()
        for line in content.strip().split('\n'):
            if line.strip():  # Ensure the line is not empty
                parts = line.split()
                if len(parts) == 2:  # Ensure there are exactly two parts
                    row1, row2 = map(int, parts)
                    self.list_one.append(row1)
                    self.list_two.append(row2)
        
        return self.list_one, self.list_two
    
    def compare_lists(self):
        """Compare the items of the two lists based on the requirements in the markdown file."""
        
        for i in self.list_one:
            i = min(self.list_one)
            


if __name__ == "__main__":
    aoc = AdventOfCode("input.txt")
    list_one, list_two = aoc.organize_data()
    print(list_one)
    print(list_two)
