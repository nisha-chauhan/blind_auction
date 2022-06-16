import os
from unicodedata import name
from auction_logo import logo
print(logo)

bid_dict={}
def higest_bidding(bidding_dict):
    higest_amt=0
    winner="bidder"
    for bidder in bidding_dict:
        bidding_amt=bidding_dict[bidder]
        if bidding_amt>higest_amt:
            higest_amt=bidding_amt
            winner=bidder
    # print(higest_amt)
    print(f"The winner is {winner} with a bid of Rs.{higest_amt}")

contest_closed=False
while not contest_closed:

    name=input("Enter your name:\n")
    price=int(float(input("Enter your bid ammount$:\n")))
    bid_dict[name]=price
    inning=input("Is there anyone left? Type 'yes'or 'no'\n")
    if inning =="no":
        contest_closed=True
        higest_bidding(bidding_dict=bid_dict)

        # print("you choose 'no' and the final result is:\n")
    elif inning=="yes":
        os.system('cls')
           

    
    
            
