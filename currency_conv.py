from currency_converter import CurrencyConverter

# Create an instance of the CurrencyRates class
c = CurrencyConverter()

# Input the amount and currencies
amount = input("Enter the amount: ")
from_currency = input("From Currency ").upper()
to_currency = input("To Currency ").upper()

# Convert the currency
result = c.convert(amount,from_currency, to_currency)

# Display the result
print(result)