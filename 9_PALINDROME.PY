""" DETERMINE WHETHER AN INTEGER GIVEN IS PALINDROME OR NOT"""

print("\n..........PROGRAM STARTED...........\n")

num=int(input("Enter any number:"))
nm1=num
num2=0
while(num>0):
    rem=num%10
    num=num//10
    num2=num2*10+rem
if(nm1==num2):
    print("You Entered a Palinsrome number.")
else:
    print("The Number is not a Palindrome.")
print("\n.......FINISHED SUCCESSFULLY........\n")

#---------------------------------------------------------------------------------------#

print("\t\n.........For STRING..........\n\t")

st1=str(input("Enter the string to be checked."))
str2=reversed(st1)
if list(st1)==list(str2):
    print("This is a Palindrome String.")
else:
    print("This String is not a Palindrome.")

print("\n\n.............END.............\n\n")