import requests
import time
from bs4 import BeautifulSoup

# intro
print("Hello! Welcome to our stock screener. Let's take a look at your company...")
time.sleep(1)

# user inputs ticker (1 variable)
# FIXME: CREATE TICKER INPUT VARIBALE

# pull data from Yahoo Finance, emnter a stock ticker in order to complete the URL and get its info
page = requests.get("https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker)
soup = BeautifulSoup(page.content, 'html.parser')

# save a list for different metrics pulled from website (1 list)
valuation = soup.find_all(class_="Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor)")

# saving all the valuation/financial metrics onto different variables (~5-6 VARIABLES)
# FIXME: USE THE NEWLY CREATED LIST THAT YOU MADE ABOVE^ TO STORE VALUES IN UNIQUE VARIABLES
# you might need to test different index values and see which one is which
#
# hint: the list is already created, you just need to find the index of whatever value you are trying to save
# ex:   list = [10, 6, 5, 64] -> this is already set in stone
#       market_cap = list[0]
#       enterprice_value = list[1]
#       market_cap is now 10, enterprice_value is now 6
#

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
    # FIXME: COMPLETE THE IF ELSE STATEMENT TO DETERMINE WHAT SIZE THE MARKET CAP IS FOR A COMPANY (use if, elif, else)
    # hint: use market_cap and compare it to what we determined befor ewe created this program
        # Small cap is when market_cap < 2 billion
        # Mid cap is when market_cap > 2 billion and < 25 billion
        # Large cap is when market_cap > 25 billion
    # our goal is to modify cap_size

letter2 = enterprise_value[-1]
enterprise_value = float(enterprise_value[:-1])

if letter2 == "T":
    enterprise_value = enterprise_value * 1000

# now we translate that data into how the user can see it
# Ask if they want to see the screener

show_metrics = input("Would you like to see the company's valuation metrics before continuing? (Y/N) ")
if (show_metrics == "N" or show_metrics == "n"):
    print("Moving on")
else:
    # FIXME: PRINT OUT ALL THE VARIABLES YOU GOT IN THE 2ND FIXME. (~5-6 VARIBALES)

# Determining the vaLuation of the stock based on cap size
time.sleep(4)
print("Since this is a " + cap_size + " company, we will use the following assumptions. Let's see if " + name + " is undervalued!\n\n")

score = 0
valued_as = ""

time.sleep(3)
print("We will generate a score based on some ratios. This determines the stock's value.\n")
time.sleep(1)

# Still need to adjust calculations for SMALL and MID CAP stocks!!!
if cap_size == "LARGE CAP":
    # FIXME: ADD A POINT TO THE SCORE (LINE 60) EVERY TIME A METRIC IS WITHIN THE EPARAMETERS OF A "BUY" OR "UNDERVALUED"
    # Hint: remember our rules we made before we created the program:
        # Forward pe > 13 sell or pe < 100 is a buy
        # PEG < 1 is a buy
        # EV/EBITDA < 14 is a buy
        # DEBT/Equity < 1 is bad
    # Add 1 to the score variable everytime each of these^ is a buy

elif cap_size == "MID CAP":
    # FIXME: for now, just copy and paste the code you just created^ into here
else:
    # FIXME: for now, just copy and paste the code you just created^ into here

# Now we are determining whether these stocks are Overvalued, undervalued, or neither
if score < 2:
    valued_as = "OVERVALUED"
elif score >= 2 and score =< 3:
    valued_as = "NEUTRAL"
else:
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
