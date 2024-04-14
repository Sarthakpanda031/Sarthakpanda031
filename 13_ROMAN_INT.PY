""" ROMAN NUMBERS WILL BE GIVEN TO YOU 
    AND WE HAVE TO CONVERT IT TO EQUIVALENT DECIML."""


# BY USING PYTHON LIBRARY FUNCTION:-
import roman
print("\n-------------DECIMAL TO ROMAN---------------\n")
num=int(input("Enter the number to be converted to roman"))
romn=roman.toRoman(num)
print(romn)

print("\n\n-------------ROMAN TO DECIMAL-----------------\n\n")
romn2=input("ENter any roman number:")
decimal=roman.fromRoman(romn2)
print(decimal)

# BY USING MANUAL METHOD

I=1
v=5
x=10
L=50
C=100
M=1000
IV=4
IX=9
XL=40
XC=90
CD=400
CM=900

