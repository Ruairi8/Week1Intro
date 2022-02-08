# Author: Ruairi McCool

convert = float(input("Please enter an amount: "))
convertedNumber = abs(convert * 100)

print("That amount in cents is :{:.0f}".format(convertedNumber))