import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

Nvidia=yf.download('NVDA', start='2021-08-03')
Amd=yf.download('AMD',start='2021-08-03')

Nvidia.columns = Nvidia.columns.get_level_values(0)
Amd.columns = Amd.columns.get_level_values(0)



for stock in [Nvidia, Amd]:
    stock['MA50'] = stock['Close'].rolling(50).mean()
    stock['MA200'] = stock['Close'].rolling(200).mean()

for stock in [Nvidia, Amd]:

  
    stock['buy_signal'] = (
        (stock['MA50'] > stock['MA200']) &
        (stock['MA50'].shift(1) <= stock['MA200'].shift(1))
    )

    
    stock['sell_signal'] = (
        (stock['MA50'] < stock["MA200"]) &
        (stock['MA50'].shift(1) >= stock['MA200'].shift(1))
    )

def run_strategy(stock, company):
    stock = stock.dropna(subset=["MA50", "MA200"]).copy()

    balance = 1000
    position = None

    print(f'{company} ')

    for index, row in stock.iterrows():

      
        if position is None and row['buy_signal']:

            buy_price = row['Close']
            print(buy_price)
            usd_size = balance

            position = {
                'buy_price': buy_price,
                'usd_size': usd_size
            }

            print(f'{index.date()} | BUY  | ${buy_price:.2f}')

        
        elif position is not None and row['sell_signal']:

            sell_price = row['Close']

            trade_return = (
                (sell_price - position['buy_price'])
                / position['buy_price']
            )

            balance += trade_return * position['usd_size']

            print(
                f'{index.date()} | SELL | ${sell_price:.2f} | '
                f'Return: {trade_return*100:.2f}%'
            )

            position = None

    
    if position is not None:

        final_price = stock['Close'].iloc[-1]

        trade_return = (
            (final_price - position['buy_price'])
            / position['buy_price']
        )

        balance += trade_return * position['usd_size']

        print(
            f'{stock.index[-1].date()} | FINAL SELL | '
            f'${final_price:.2f}'
        )

    print(f'Final Balance: ${balance:.2f}')

    return balance



nvda_balance = run_strategy(Nvidia, 'NVIDIA')
amd_balance = run_strategy(Amd, 'AMD')




print('Strategy Comparison')

print(f'NVIDIA Final Balance : ${nvda_balance:.2f}')
print(f'AMD Final Balance    : ${amd_balance:.2f}')

if nvda_balance > amd_balance:
    print('\nNVIDIA strategy outperformed AMD.')
elif amd_balance > nvda_balance:
    print('\nAMD strategy outperformed NVIDIA.')
else:
    print('\nBoth strategies produced the same return.')


plt.figure(figsize=(12,6))

plt.plot(Nvidia.index, Nvidia['Close'], label='Close Price')
plt.plot(Nvidia.index, Nvidia['MA50'], label='50-Day MA')
plt.plot(Nvidia.index, Nvidia['MA200'], label='200-Day MA')

plt.scatter(
    Nvidia.index[Nvidia['buy_signal']],
    Nvidia["Close"][Nvidia['buy_signal']],
    marker='^',
    s=100,
    label="Buy Signal"
)

plt.scatter(
    Nvidia.index[Nvidia['sell_signal']],
    Nvidia['Close'][Nvidia['sell_signal']],
    marker='v',
    s=100,
    label="Sell Signal"
)

plt.title('NVIDIA Moving Average Strategy')
plt.legend()
plt.tight_layout()
plt.savefig('nvidia_strategy.png', dpi=300)
plt.show()



plt.figure(figsize=(12,6))

plt.plot(Amd.index, Amd['Close'], label='Close Price')
plt.plot(Amd.index, Amd['MA50'], label='50-Day MA')
plt.plot(Amd.index, Amd["MA200"], label='200-Day MA')

plt.scatter(
    Amd.index[Amd['buy_signal']],
    Amd['Close'][Amd['buy_signal']],
    marker="^",
    color='green',
    s=100,
    label='Buy Signal'
)

plt.scatter(
    Amd.index[Amd['sell_signal']],
    Amd['Close'][Amd['sell_signal']],
    marker='v',
    color="red",
    s=100,
    label='Sell Signal'
)

plt.title('AMD Moving Average Strategy')
plt.legend()
plt.tight_layout()
plt.savefig('amd_strategy.png', dpi=300)
plt.show()


print(f'NVIDIA Buy & Hold Return = 910% | Moving Average Strategy = 740% | Difference = -170%')










