

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



Boeing = yf.download('BA', start='2021-01-01')
Airbus = yf.download('AIR.PA', start='2021-01-01')
Lockheed_Martin = yf.download('LMT', start='2021-01-01')
RTX = yf.download('RTX', start='2021-01-01')
Northrop_Grumman = yf.download('NOC', start='2021-01-01')

prices = pd.concat([
    Boeing["Close"].iloc[:, 0],
    Airbus["Close"].iloc[:, 0],
    Lockheed_Martin["Close"].iloc[:, 0],
    RTX["Close"].iloc[:, 0],
    Northrop_Grumman["Close"].iloc[:, 0]
], axis=1)

prices.columns = [
    "Boeing",
    "Airbus",
    "Lockheed Martin",
    "RTX",
    "Northrop Grumman"
]



normalised = prices / prices.iloc[0] * 100

plt.figure(figsize=(12, 6))

for company in normalised.columns:
    plt.plot(normalised.index,
             normalised[company],
             label=company)

plt.title('Aerospace Stock Performance (Base = 100)')
plt.xlabel('Date')
plt.ylabel('Indexed Price')
plt.legend()
plt.tight_layout()

plt.savefig('aerospace_performance.png')
plt.show()



returns = prices.pct_change().dropna()



annual_returns = returns.mean() * 252 * 100

print('\nAnnual Returns (%)')
print(annual_returns)

plt.figure(figsize=(10, 6))

annual_returns.plot(kind='bar')

plt.title('Annualised Returns')
plt.ylabel('Return (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('annual_returns.png')
plt.show()



annual_volatility = returns.std() * (252 ** 0.5) * 100

print('\nAnnual Volatility (%)')
print(annual_volatility)

plt.figure(figsize=(10, 6))

annual_volatility.plot(kind='bar')

plt.title('Annualised Volatility')
plt.ylabel('Volatility (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('annual_volatility.png')
plt.show()
