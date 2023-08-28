symbol=input("The stock symbol:\n")
nshares=int(input("Number of shares:\n"))
bprice=float(input("The stock buying price:\n"))
sprice=float(input("The stock selling price:\n"))
print()

total_bprice=nshares*bprice
total_sprice=nshares*sprice
commission_buying=float(total_bprice*0.03)
commission_selling=float(total_sprice*0.03)
total_commission=commission_selling+commission_buying
profit_loss=(total_sprice-total_bprice)-total_commission

print (f"Transactions for stock: {symbol}")
print (f"Bought {nshares} shares @ {bprice}")
print (f"Paid {round(total_bprice,2)}")
print (f"Commission when buying: {round(commission_buying,2)}")
print (f"Sold {nshares} shares @ {sprice}")
print (f"Received {round(total_sprice,2)}")
print (f"Commission when selling: {round(commission_selling,2)}")
print (f"Profit or loss: {round(profit_loss,2)}")


