import requests
import time
from bs4 import BeautifulSoup

# intro
print("Hello! Welcome to our stock screener. Let's take a look at your company...")
time.sleep(1)

# user inputs ticker
ticker = input("Please enter your stock ticker: ")

# pull data from Yahoo Finance, emnter a stock ticker in order to complete the URL and get its info
page = requests.get("https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker)
soup = BeautifulSoup(page.content, 'html.parser')

# save two lists for different data types pulled from website
valuation = soup.find_all(class_="Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)")
financials = soup.find_all(class_="Fw(500) Ta(end) Pstart(10px) Miw(60px)")

while financials == []:
        print("That company doesn't exist! Please try again!")
        ticker = input("Please enter your stock ticker: ")
        page = requests.get("https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker)
        soup = BeautifulSoup(page.content, 'html.parser')
        valuation = soup.find_all(class_="Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)")
        financials = soup.find_all(class_="Fw(500) Ta(end) Pstart(10px) Miw(60px)")

# saving all the valuation/financial metrics onto different variables
name = soup.find(class_="D(ib) Fz(18px)").get_text()
price = soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()
market_cap = valuation[0].get_text()
enterprise_value = valuation[1].get_text()
trailing_PE = (float(valuation[2].get_text()) if valuation[2].get_text() != "N/A" else 0)
forward_PE = (float(valuation[3].get_text()) if valuation[3].get_text() != "N/A" else 0)
Peg = (float(valuation[4].get_text()) if valuation[4].get_text() != "N/A" else 0)
price_sales = (float(valuation[5].get_text()) if valuation[5].get_text() != "N/A" else 0)
price_book = (float(valuation[6].get_text()) if valuation[6].get_text() != "N/A" else 0)
Ev_Revenue = (float(valuation[7].get_text()) if valuation[7].get_text() != "N/A" else 0)
Ev_EBITDA = (float(valuation[8].get_text()) if valuation[8].get_text() != "N/A" else 0)
current_ratio = (float(financials[46].get_text()) if financials[46].get_text() != "N/A" else 0)
# quick ratio
# debt to ebitda
# ROE
# ROIC
# Operating Margin
# Dividend growth
debt_equity = (float(financials[45].get_text()) if financials[45].get_text() != "N/A" else 0)

# Determine market cap of the company
letter1 = market_cap[-1]
market_cap = float(market_cap[:-1])

cap_size = ""
if letter1 == "M":
    cap_size = "SMALL CAP"
elif letter1 == "T":
    cap_size = "LARGE CAP"
    market_cap = market_cap * 1000
else:
    if market_cap < 2:
        cap_size = "SMALL CAP"
    elif market_cap > 2 and market_cap < 25:
        cap_size = "MID CAP"
    else:
        cap_size = "LARGE CAP"

letter2 = enterprise_value[-1]
enterprise_value = float(enterprise_value[:-1])

if letter2 == "T":
    enterprise_value = enterprise_value * 1000

# now we translate that data into how the user can see it
# NEED to find a way to loop bakc to beginnning if they enter an invalid ticker. HOW?????

""" ticker = input("Please enter your stock ticker: ")
while ticker != "AMD":
    print("We currently don't have that stock in the database, or that ticker doesn't exist. Try again!\n")
    ticker = input("Please enter your stock ticker: ")
else:"""

# Ask if they want to ssee the screener
show_metrics = input("Would you like to see the company's valuation metrics before continuing? (Y/N) ")
if (show_metrics == "N" or show_metrics == "n"):
    print("Moving on")
else:
    time.sleep(1)

    print()
    print("Company Name:                        ", name)
    print(ticker + "'s Price is:                    $", price)
    print(ticker + "'s Market cap is:               $", market_cap, ("Million" if letter1 == 'M' else "Billion"))
    print(ticker + "'s Enterprise Value is:         $", enterprise_value, ("Million" if letter2 == 'M' else "Billion"))
    print(ticker + "'s Trailing P/E ratio is:        ", trailing_PE)
    print(ticker + "'s Forward P/E ratio is:         ", forward_PE)
    print(ticker + "'s PEG ratio is:                 ", Peg)
    print(ticker + "'s Price/Sales ratio is:         ", price_sales)
    print(ticker + "'s Price/Book ratio is:          ", price_book)
    print(ticker + "'s Enterprise Value/Revenue is:  ", Ev_Revenue)
    print(ticker + "'s Enterprise Value/EBITDA is:   ", Ev_EBITDA)
    print(ticker + "'s Current ratio is:             ", current__ratio)
    print(ticker + "'s Debt-to-Equity ratio is:      ", debt_equity, "\n\n")

# Determining the vlauation of the stock based on cap size
time.sleep(4)
print("Since this is a " + cap_size + " company, we will use the following assumptions. Let's see if " + name + " is undervalued!\n\n")

score = 0
valued_as = ""

time.sleep(3)
print("We will generate a score based on some ratios. This determines the stock's value.\n")
time.sleep(1)

# Still need to adjust calculations for SMALL and MID CAP stocks!!!
if cap_size == "LARGE CAP":
    if forward_PE > 13 and forward_PE < 50:
        score += 1
        time.sleep(1)
        print("Price-to-Earnings seems alright...\n")
    if price_sales < 4:
        score += 1
        time.sleep(1)
        print("Price-to-Sales looks interesting...\n")
    if Peg < 1.5:
        score += 1
        time.sleep(1)
        print("The PEG ratio is great! Hmm...\n")
    if Ev_EBITDA < 14:
        score += 1
        time.sleep(1)
        print("EV/EBITDA looks promising...\n")
    if debt_equity < 2:
        score += 1
        time.sleep(1)
        print("The Debt-to-Equity ratio is good, stable company huh...\n")
    if current__ratio > 1.5:
        score += 1
        time.sleep(1)
        print("The Current ratio isn't bad...\n")
elif cap_size == "MID CAP":
    if forward_PE > 13 and forward_PE < 50:
        score += 1
        time.sleep(1)
        print("Price-to-Earnings seems alright...\n")
    if price_sales < 4:
        score += 1
        time.sleep(1)
        print("Price-to-Sales looks interesting...\n")
    if Peg < 1.5:
        score += 1
        time.sleep(1)
        print("The PEG ratio is great! Hmm...\n")
    if Ev_EBITDA < 14:
        score += 1
        time.sleep(1)
        print("EV/EBITDA looks promising...\n")
    if debt_equity < 2:
        score += 1
        time.sleep(1)
        print("The Debt-to-Equity ratio is good, stable company huh...\n")
    if current__ratio > 1.5:
        score += 1
        time.sleep(1)
        print("The Current ratio isn't bad...\n")
else:
    if forward_PE > 13 and forward_PE < 50:
        score += 1
        time.sleep(1)
        print("Price-to-Earnings seems alright...\n")
    if price_sales < 4:
        score += 1
        time.sleep(1)
        print("Price-to-Sales looks interesting...\n")
    if Peg < 1.5:
        score += 1
        time.sleep(1)
        print("The PEG ratio is great! Hmm...\n")
    if Ev_EBITDA < 14:
        score += 1
        time.sleep(1)
        print("EV/EBITDA looks promising...\n")
    if debt_equity < 2:
        score += 1
        time.sleep(1)
        print("The Debt-to-Equity ratio is good, stable company huh...\n")
    if current__ratio > 1.5:
        score += 1
        time.sleep(1)
        print("The Current ratio isn't bad...\n")

# Now we are determining whether these stocks are Overvalued, undervalued, or neither
if score < 2:
    valued_as = "OVERVALUED"
elif score >= 2 and score < 4:
    valued_as = "NEUTRAL"
elif score >= 4 and score < 5:
    valued_as = "SLIGHTLY UNDERVALUED"
elif score >= 5:
    valued_as = "UNDERVALUED"

# Results!
print(ticker + " has a score of:", score)
print("This stock is...")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".\n\n")
time.sleep(1)
print(valued_as + "!\n(according to our Valuation criteria :) ")
