"""
Question 1
"""
import math

OUTPUT_FORMAT = """
SquarePyramid
=============
Side Length: {side_length}
Height: {height}
Base Area: {base_area}
Perimeter: {perimeter}
Volume: {volume}
LSA: {lsa}
TSA: {tsa}
Slant Height: {slant_height}
"""

def print_table(headers, data, name=None):
    """
    Utility function for printing a table
    """
    column_widths = [max(len(str(header)), max(len(str(row[i])) for row in data)) for i, header in enumerate(headers)]

    header_line = " | ".join(f"{header:^{width}}" for header, width in zip(headers, column_widths))
    separator_line = "-+-".join("-" * width for width in column_widths)
    
    if name:
        initial_line = "-"*len(separator_line)
        title_line = f"{name:^{len(separator_line)}}"
        print(f"+{initial_line}+")
        print(f"|{title_line}|")

    print(f"+{separator_line}+")
    print(f"|{header_line}|")
    print(f"+{separator_line}+")

    # Print the data rows
    for row in data:
        row_line = " | ".join(f"{str(value):^{width}}" for value, width in zip(row, column_widths))
        print(f"|{row_line}|")
    
    print(f"+{separator_line}+")


class SquarePyramid:
    """
    SquarePyramid calss
    """

    def __init__(self, side_length, height):
        """
        Constructor for the SquarePyramid Class
        """
        self.side_length = side_length
        self.height = height

    @property
    def base_area(self):
        """
        Returns the base area of the Pyramid
        """
        return self.side_length ** 2

    @property
    def perimeter(self):
        """
        Returns the perimeter of the Pyramid
        """
        return 4 * self.side_length

    @property
    def volume(self):
        """
        Returns the volue of the Pyramid
        """
        return (1/3) * self.base_area * self.height

    @property
    def lsa(self):
        """
        Returns the LSA of the Pyramid
        """
        return self.side_length * math.sqrt(self.side_length**2 + 4*(self.height**2))

    @property
    def tsa(self):
        """
        Returns the TSA of the Pyramid
        """
        return 2*self.side_length*self.slant_height + self.side_length**2

    @property
    def slant_height(self):
        """
        Returns the Slant Height of the Pyramid
        """
        return math.sqrt((self.side_length / 2) ** 2 + self.height ** 2)

    def __str__(self):
        """
        Override str method of the function
        """
        return OUTPUT_FORMAT.format(
            side_length=self.side_length,
            height=self.height,
            base_area=self.base_area,
            perimeter=self.perimeter,
            volume=self.volume,
            lsa=self.lsa,
            tsa=self.tsa,
            slant_height=self.slant_height
        )


def main():
    """
    Ask user for the inputs and calculate stats for each SquarePyramid
    """
    print('The program prints the volume, LSA, TSA and slant height of a square pyramid\nwith height h being an odd number ranging from 1 to N and side length a.')

    N = int(input("Enter the value for N: "))
    side_length = int(input("Enter the length of side a: "))

    headers = ['Height', 'Volume', 'Letral Surface Area', 'Total Surface Area', 'Slant Height']
    data = []

    for h in range(1, N+1, 2):
        sp = SquarePyramid(side_length, h)
        data.append([
            f'{sp.height}',
            f'{sp.volume:.0f} m\N{SUPERSCRIPT THREE}',
            f'{sp.lsa:.3f} m\N{SUPERSCRIPT TWO}',
            f'{sp.tsa:.3f} m\N{SUPERSCRIPT TWO}',
            f'{sp.slant_height:.3f} m',
        ])
    print_table(headers, data)


if __name__ == '__main__':
    main()
