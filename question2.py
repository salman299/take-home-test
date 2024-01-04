import math

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

class CountryEconomicIndicator:
    """
    Represents a Country with economic indicators and provides methods to calculate
    and analyze economic statistics.

    Attributes:
    - country_name (str): The name of the country.
    - initial_gdp_value (float): The initial Gross Domestic Product (GDP) value for the country.
    - yearly_gdp_values (list): List of yearly GDP values for the country.
    - growth_rates (list): List of growth rates calculated based on yearly GDP values.
    - rankings (list): Rankings determined based on growth rates.
    - average_growth_rate (float): The average growth rate.
    - compound_growth_rate (float): The compound growth rate.
    - standard_deviation (float): The standard deviation of growth rates.
    """

    def __init__(self, initial_gdp_value, yearly_gdp_values, country_name='A'):
        """
        Initialize a CountryEconomicIndicator object.

        Parameters:
        - initial_gdp_value (float): The initial Gross Domestic Product (GDP) value for the country.
        - yearly_gdp_values (list): A list of yearly GDP values for the country.
        - country_name (str, optional): The name of the country. Default is 'A'.
        """
        if len(yearly_gdp_values) == 0:
            raise ValueError(
                "The yearly_gdp_values should atleast contains one value")

        self.country_name = country_name
        self.initial_gdp_value = initial_gdp_value
        self.yearly_gdp_values = yearly_gdp_values
        self.gdp_values = [initial_gdp_value] + yearly_gdp_values
        self.evaluate()

    def evaluate(self):
        """
        Calculate and store various economic indicators in the Country object.

        This method performs the following calculations and updates the object attributes:
        - Calculate growth rates based on GDP values.
        - Determine rankings based on growth rates.
        - Calculate the average growth rate.
        - Calculate the compound growth rate.
        - Calculate the standard deviation of growth rates.
        """
        self.growth_rates = self.calculate_growth_rates(self.gdp_values)
        self.rankings = self.find_rankings(self.growth_rates)
        self.average_growth_rate = sum(self.growth_rates) / len(self.growth_rates)
        self.compound_growth_rate = self.calculate_compound_growth_rate(
            self.initial_gdp_value, self.yearly_gdp_values[-1], len(self.yearly_gdp_values),
        )
        self.standard_deviation = self.calculate_standard_deviation(
            self.growth_rates)

    @staticmethod
    def find_rankings(growth_rates):
        """
        Determine rankings based on growth rates.

        Rankings are assigned as follows:
        - 'Exceptional' for growth rates greater than 25.
        - 'Good' for growth rates greater than 0.
        - 'Poor' for growth rates less than 0.

        Parameters:
        - growth_rates (list): List of growth rates for which rankings are determined.

        Returns:
        list: A list of strings representing the rankings for each corresponding growth rate.
        """
        return ['Exceptional' if rate > 25 else 'Good' if rate > 0 else 'Poor' for rate in growth_rates]

    @staticmethod
    def calculate_growth_rate(gdp_start, gdp_end):
        """
        Calculate the growth rate between two GDP values.

        Parameters:
        - gdp_start (float): Initial GDP value.
        - gdp_end (float): Final GDP value.

        Returns:
        float: The calculated growth rate
        """
        return 100*(gdp_end - gdp_start)/gdp_start

    @staticmethod
    def calculate_growth_rates(gdp_values):
        """
        Calculate growth rates based on a list of GDP values.

        Parameters:
        - gdp_values (list): List of GDP values for which growth rates are calculated.

        Returns:
        list: A list of growth rates between consecutive GDP values.
        """
        return [CountryEconomicIndicator.calculate_growth_rate(gdp_values[i], gdp_values[i + 1]) for i in range(len(gdp_values) - 1)]

    @staticmethod
    def calculate_compound_growth_rate(initial_gdp_value, ending_gdp_value, number_of_years):
        """
        Calculate the compound growth rate between an initial and ending GDP value over a specified number of years.

        Parameters:
        - initial_gdp_value (float): Initial GDP value.
        - ending_gdp_value (float): Ending GDP value.
        - number_of_years (int): Number of years over which the growth occurs.

        Returns:
        float: The calculated compound growth rate, rounded to 2 decimal places.
        """
        return 100*((ending_gdp_value / initial_gdp_value) ** (1 / number_of_years) - 1)

    @staticmethod
    def calculate_standard_deviation(growth_rates):
        """
        Calculate the standard deviation of a list of growth rates.

        Parameters:
        - growth_rates (list): List of growth rates for which the standard deviation is calculated.

        Returns:
        float: The calculated standard deviation.
        """
        average_growth_rate = sum(growth_rates)/len(growth_rates)
        return round(math.sqrt(sum((rate - average_growth_rate) ** 2 for rate in growth_rates) / (len(growth_rates) - 1)), 3)

    def get_stats(self):
        """
        Retrieve statistical information about the Country object.

        Returns a dictionary containing various economic indicators and attributes of the CountryEconomicIndicator object:
        - 'country_name': The name of the country.
        - 'initial_gdp_value': The initial Gross Domestic Product (GDP) value for the country.
        - 'yearly_gdp_values': List of yearly GDP values for the country.
        - 'growth_rates': List of growth rates calculated based on the GDP values.
        - 'rankings': Rankings determined based on growth rates.
        - 'average_growth_rate': The average growth rate.
        - 'compound_growth_rate': The compound growth rate.
        - 'standard_deviation': The standard deviation of growth rates.

        Returns:
        dict: A dictionary containing statistical information about the CountryEconomicIndicator object.
        """
        return {
            "country_name": self.country_name,
            "initial_gdp_value": self.initial_gdp_value,
            "yearly_gdp_values": self.yearly_gdp_values,
            "growth_rates": self.growth_rates,
            "rankings": self.rankings,
            "average_growth_rate": self.average_growth_rate,
            "compound_growth_rate": self.compound_growth_rate,
            "standard_deviation": self.standard_deviation,
        }

    def print_stats(self):
        """
        Print statistical information in a tabular format.

        Displays a table containing information such as Year, GDP Value, Growth Rate, and Ranking for each year.
        Additionally, prints the Average Annual Growth Rate, Compound Annual Growth Rate, and Standard Deviation.
        """
        headers = ['Year', 'GDP Value', 'Growth Rate', 'Ranking']
        title = f'Country {self.country_name}'
        data = []
        for i in range(len(self.yearly_gdp_values)):
            data.append([
                f'{i+1}',
                f'${self.yearly_gdp_values[i]:,.2f}',
                f'{self.growth_rates[i]:.2f}%',
                f'{self.rankings[i]}',
            ])

        print_table(headers, data, name=title)
        print(f'Average Annual Growth Rate: {self.average_growth_rate:.2f}%')
        print(f'Compound Annual Growth Rate: {self.compound_growth_rate:.2f}%')
        print(f'Standard Deviation: {self.standard_deviation:.3f}')


def compare_economy_volatility(country_std_dev):
    """
    Compare the volatility of economies based on standard deviation values.

    This function takes a dictionary containing standard deviation values for multiple countries.
    It identifies the country with the minimum standard deviation, indicating the most stable economy.
    If the minimum standard deviation is less than 25, it is considered stable; otherwise, it is deemed risky.

    Parameters:
    - country_std_dev (dict): A dictionary where keys are country names and values are their corresponding standard deviations.
    """
    if not country_std_dev:
        print("No data provided.")
        return

    min_std_dev = min(country_std_dev.values())

    for country, std_dev in country_std_dev.items():
        if std_dev == min_std_dev:
            if min_std_dev < 25:
                print(f"The Country {country}'s economy is most stable.")
            else:
                print(f"The Country {country}'s economy is least risky.")


def main():
    """
    Main function
    """
    no_of_countries = int(input("Enter the number of countries: "))
    no_of_years = int(input("Enter the number of years: "))

    country_economic_indicators = []
    country_std_dev = {}

    for i in range(1, no_of_countries+1):
        country_name = input(f"Enter the name of country {i}: ")
        print(f'\nCountry {country_name}')
        print('-'*50)
        initial_gdp_value = int(input("Enter the beginning GDP value: "))
        yearly_gdp_values = []
        for j in range(1, no_of_years+1):
            year_end_value = int(input(f"Enter the end of year {j} GDP value: "))
            yearly_gdp_values.append(year_end_value)
        country_economic_indicator = CountryEconomicIndicator(initial_gdp_value, yearly_gdp_values, country_name)
        country_economic_indicators.append(country_economic_indicator)
        country_std_dev[country_name] = country_economic_indicator.standard_deviation
        print('\n')

    for economic_indicator in country_economic_indicators:
        economic_indicator.print_stats()
        print('\n')

    print('\n')
    compare_economy_volatility(country_std_dev)


if __name__ == '__main__':
    main()
