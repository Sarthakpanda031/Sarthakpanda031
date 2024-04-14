"""A 32 BIT SIGNED numberBER WILL BE GIVEN 
    WE NEED TO FND THE REVERSE OF THE GIVEN numberBER """

print("\n\n\t............START OF PROGRAM.........\n\n\t")

number=int(input("Enter A numberber: "))
maxi=2**31-1
mini=-2**31
rev=0
sign=1 if number>0 else -1
number=abs(number)
while(number>0):
    rem=number%10
    if rev>(maxi-rem)//10:
        print(0)
    rev=rev*10+rem
    number//=10
print(f"\nReversed of the Number is: {rev*sign}\t\t")

print("\n\t.............ENDED..........\n\t")
