import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os


sp500 = yf.download("^GSPC", start="2021-01-01")
ftse = yf.download("^FTSE", start="2021-01-01")

prices = pd.DataFrame({
    "S&P 500": sp500["Close"].iloc[:, 0],
    "FTSE 100": ftse["Close"].iloc[:, 0]
})

print(prices.head())



normalised = prices / prices.iloc[0] * 100

plt.figure(figsize=(12,6))

for market in normalised.columns:
    plt.plot(normalised.index,
             normalised[market],
             label=market)

plt.title("Stock Market Performance (Base = 100)")
plt.xlabel("Date")
plt.ylabel("Indexed Price")
plt.legend()
plt.tight_layout()

plt.savefig("market_performance.png", dpi=300)
plt.show()
plt.close()


returns = prices.pct_change().dropna()

print("\nDaily Returns")
print(returns.head())



annual_returns = returns.mean() * 252 * 100

print("\nAnnual Returns (%)")
print(annual_returns)

ax = annual_returns.plot(
    kind="bar",
    figsize=(8,6),
    title="Annualised Returns"
)

ax.set_ylabel("Return (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("annual_returns.png", dpi=300)
plt.show()
plt.close()



annual_volatility = returns.std() * (252**0.5) * 100

print("\nAnnual Volatility (%)")
print(annual_volatility)

ax = annual_volatility.plot(
    kind="bar",
    figsize=(8,6),
    title="Annualised Volatility"
)

ax.set_ylabel("Volatility (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("annual_volatility.png", dpi=300)
plt.show()
plt.close()



correlation = returns.corr()

print("\nCorrelation Matrix")
print(correlation)


prices.to_csv("market_data.csv")
returns.to_csv("returns_data.csv")

print("\nCurrent Folder:")
print(os.getcwd())

print("\nFiles saved successfully!")