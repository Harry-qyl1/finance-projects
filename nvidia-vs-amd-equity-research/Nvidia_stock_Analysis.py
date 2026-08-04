import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

Nvidia=yf.download('NVDA', start='2021-08-03')
Amd=yf.download('AMD',start='2021-08-03')

prices = pd.DataFrame({
    "Nvidia": Nvidia["Close"].iloc[:, 0],
    "Amd": Amd["Close"].iloc[:, 0]
})
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

plt.savefig("market_performance_NVIDIA_AMD.png", dpi=300)
plt.show()

Nvidia['ma50']=Nvidia['Close'].rolling(50).mean()
Nvidia['ma200']=Nvidia['Close'].rolling(200).mean()
Amd['ma50']=Amd['Close'].rolling(50).mean()
Amd['ma200']=Amd['Close'].rolling(200).mean()

Moving_avarages={ 
    'N_ma50':Nvidia['ma50'],
    'N_ma200':Nvidia['ma200'],
    'A_ma50':Amd['ma50'],
    'A_ma200':Amd['ma200']}

plt.figure(figsize=(12, 6))

for label, series in Moving_avarages.items():
    plt.plot(series, label=label)

plt.title('NVDA vs AMD Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.savefig('Moving_averages_Nvidia_AMD.png', dpi=300)
plt.show()



returns = prices.pct_change().dropna()

annual_returns = returns.mean() * 252 * 100

print(f"Annual Returns (%)")
print(annual_returns)

ax = annual_returns.plot(
    kind="bar",
    figsize=(8,6),
    title='Annualised Returns'
)

ax.set_ylabel("Return (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('annual_returns_Nvida_AMD.png', dpi=300)
plt.show()


annual_volatility=returns.std()*(252**0.5)*100


print(f'Annual Volatility (%)')
print(annual_volatility)

ax = annual_volatility.plot(
    kind="bar",
    figsize=(8,6),
    title='Annualised Volatility'
)

ax.set_ylabel('Volatility (%)')
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('annual_volatility_Nvidia_AMD.png', dpi=300)
plt.show()

correlation = returns.corr()

print(f'Correlation Matrix')
print(correlation)

sharpe = (annual_returns - 4.5) / annual_volatility
print(sharpe)

prices.to_csv("market_data.csv")
returns.to_csv("returns_data.csv")