
print("km  to mile cinverter")
unit = input ("km or mile: ")
amount = float(input("Amount: "))

if unit == "km":
  print (amount / 1.6)

elif unit == "mile":
  print (amount * 1.6)

else:
  print("Error")
