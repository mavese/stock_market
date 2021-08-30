import yfinance as yf
import sys

def get_tickers(tickersStr):
	tickers = yf.Tickers(tickersStr)
	for ticker in tickers.tickers.items():
		print(f"Ticker {ticker[0]} hourly info for today:")
		print(ticker[1].history(period="1d", interval="60m"))

def main():
	tickersStr = " ".join(sys.argv[1:])
	get_tickers(tickersStr)

if __name__ == '__main__':
	main()