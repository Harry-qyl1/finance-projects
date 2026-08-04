# NVIDIA vs AMD Equity Research Report

## Project Overview

This project compares **NVIDIA (NVDA)** and **Advanced Micro Devices (AMD)** to determine which company represents the stronger long-term investment opportunity.

The analysis combines traditional equity research with quantitative analysis using Python. It includes financial statement analysis, discounted cash flow (DCF) valuation, historical stock performance, technical analysis and a moving average trading strategy.

The aim of the project is to demonstrate how qualitative research and quantitative analysis can be combined to support an investment recommendation.

---

## Project Objectives

- Compare NVIDIA and AMD's financial performance
- Build discounted cash flow (DCF) valuation models for both companies
- Analyse historical stock performance using Python
- Compare annual returns and volatility
- Calculate correlation and Sharpe ratios
- Implement and backtest a moving average crossover trading strategy
- Produce a final investment recommendation based on the combined analysis

---

## Technologies Used

- Python
- Pandas
- yfinance
- Matplotlib
- Microsoft Excel

---

## Project Structure

```
nvidia-vs-amd-equity-research/
│
├── final_report.pdf
├── financial_model.xlsx
├── stock_analysis.py
├── trading_strategy.py
├── requirements.txt
│
├── images/
│   ├── market_performance.png
│   ├── annual_returns.png
│   ├── annual_volatility.png
│   ├── moving_averages.png
│   ├── nvidia_strategy.png
│   └── amd_strategy.png
│
└── README.md
```

---

## Analysis Performed

### Financial Analysis

- Revenue Growth
- Operating Margins
- Profitability
- Business Segments
- Competitive Position
- Industry Analysis

### Valuation

A discounted cash flow (DCF) model was built for both companies using forecast revenue growth, operating margins, free cash flow and terminal value assumptions.

The resulting intrinsic values were compared with current market prices to assess whether each company appeared overvalued or undervalued.

### Python Analysis

Historical market data was downloaded using **yfinance** and analysed using Python.

The analysis includes:

- Historical stock price comparison
- 50-Day Moving Average
- 200-Day Moving Average
- Annualised Returns
- Annualised Volatility
- Correlation Analysis
- Sharpe Ratio
- Buy-and-Hold Performance

### Trading Strategy

A simple moving average crossover strategy was implemented and backtested.

**Buy Signal**

- 50-Day Moving Average crosses above the 200-Day Moving Average (Golden Cross)

**Sell Signal**

- 50-Day Moving Average crosses below the 200-Day Moving Average (Death Cross)

The strategy simulated trades from an initial investment of **$1,000** and compared the performance of NVIDIA and AMD over the testing period.

---

## Key Findings

- NVIDIA delivered stronger historical returns than AMD.
- NVIDIA produced a higher Sharpe ratio, indicating superior risk-adjusted performance.
- Both companies exhibited a positive correlation, reflecting their exposure to the semiconductor industry.
- The DCF analysis suggested stronger intrinsic value for NVIDIA under the assumptions used.
- The moving average strategy demonstrated how technical indicators can be used to create systematic trading rules.

Overall, the analysis supported **NVIDIA** as the stronger long-term investment opportunity.

---

## Skills Demonstrated

- Equity Research
- Financial Statement Analysis
- Industry Analysis
- Financial Forecasting
- Discounted Cash Flow (DCF) Valuation
- Python Programming
- Data Analysis
- Data Visualisation
- Technical Analysis
- Trading Strategy Backtesting

---

## Future Improvements

Potential extensions to this project include:

- Monte Carlo DCF sensitivity analysis
- Relative valuation using comparable companies
- Three-statement financial modelling
- Portfolio optimisation using Modern Portfolio Theory
- Additional technical indicators (RSI, MACD and Bollinger Bands)
- Performance comparison against the S&P 500 Semiconductor Index

---

## Disclaimer

This project was completed for educational purposes to develop financial modelling, equity research and Python programming skills. It should not be considered financial or investment advice.
