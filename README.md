# Currency Converter

This is a simple Python-based currency converter application that allows users to convert amounts between three currencies: USD, EUR, and CAD.

## Features

- Convert between USD, EUR, and CAD.
- Handles invalid inputs for amounts and currencies gracefully.
- Provides accurate conversion rates.

## How to Use

1. Run the script `app.py`.
2. Enter the amount you want to convert.
3. Specify the source currency (USD, EUR, or CAD).
4. Specify the target currency (USD, EUR, or CAD).
5. The application will display the converted amount.

## Conversion Rates

The application uses the following predefined conversion rates:

| From/To | Rate  |
| ------- | ----- |
| USD/EUR | 0.92  |
| EUR/USD | 1.087 |
| USD/CAD | 1.44  |
| CAD/USD | 0.694 |
| EUR/CAD | 1.56  |
| CAD/EUR | 0.641 |

## Example

```plaintext
Enter the amount: 100
Source currency (USD/EUR/CAD): USD
Target currency (USD/EUR/CAD): EUR
100.00 USD is equal to 92.00 EUR
```

## Requirements

- Python 3.x

## Running the Application

1. Save the `app.py` file to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `app.py`.
4. Run the script using the command:

   ```bash
   python app.py
   ```

## Notes

- The application only supports USD, EUR, and CAD.
- Conversion rates are hardcoded and may not reflect real-time rates.
