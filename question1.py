"""
Question 1
"""
import math
from prettytable import PrettyTable

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

    table = PrettyTable(['Height', 'Volume', 'Letral Surface Area', 'Total Surface Area', 'Slant Height'], align="l")

    for h in range(1, N+1, 2):
        sp = SquarePyramid(side_length, h)
        table.add_row([
            f'{sp.height}',
            f'{sp.volume:.0f} m\N{SUPERSCRIPT THREE}',
            f'{sp.lsa:.3f} m\N{SUPERSCRIPT TWO}',
            f'{sp.tsa:.3f} m\N{SUPERSCRIPT TWO}',
            f'{sp.slant_height:.3f} m',
        ])
    print(table)


if __name__ == '__main__':
    main()
