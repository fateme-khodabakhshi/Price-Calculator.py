# https://github.com/fateme-khodabakhshi/Price-Calculator.py

def calculate_price(price, tax_rate=0.1):
    return price * (1 + tax_rate)


def main():
    price = float(input())

    try:
        tax_rate = float(input())
        result = calculate_price(price, tax_rate)
    except EOFError:
        result = calculate_price(price)

    print(result)


main()
