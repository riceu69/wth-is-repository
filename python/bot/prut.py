a="Make a lot of money"
b="buy now"
c="subscribe this"
d="click this"

e=input("enter the email: ")

if(a in e or b in e or c in e or d in e):
    print("spam email")
else:
    print("safe email")

