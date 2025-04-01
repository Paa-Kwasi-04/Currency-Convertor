def convertor(source, target, amount):
    rates = {
        'USD/EUR': 0.92, 'EUR/USD': 1/0.92,
        'USD/CAD': 1.44, 'CAD/USD': 1/1.44,
        'EUR/CAD': 1.56, 'CAD/EUR': 1/1.56
    }
    if source == target:
        return amount

    return amount * rates[f'{source}/{target}']


def get_amount():

    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD):').upper()
        if currency not in currencies:
            print('Invalid currency')
        else:
            return currency


def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')

    final_amount = convertor(source_currency, target_currency, amount)
    print(f'{amount:.2f} {source_currency} is equal to {final_amount:.2f} {target_currency}')


if __name__ == '__main__':
    main()
