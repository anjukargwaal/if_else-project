print("Choose your cuisine")
print("1. Chinease\n2. Indian \n3. Deserts")
a=int(input("Enter you item number: "))
if a==1:
    print("Chinese Menu\n1. Noodles \n2. Maggie \n3. Soup")
    b=int(input("enter your item number: "))
    if b==1:
        print("Price of noodles is 120")
    elif b==2:
        print("price of maggie is 150")
    elif b==3:
        print("price of soup is 140")
elif a==2:
    
    print("Indian Menu\n1. Rajma Chawal\n2. Daal Makhani \n3. Matar Panner")
    c=int(input("enter your item number: "))
    if c==1:
            print("price of rajma chawal is 300")
    elif c==2:
            print("price of dal makhni is 400")
    elif c==3:
            print("price of matar panner is 500")
elif a==3:
    
    print("Desert Menu \n1. Jalebi\n2. Pista\n3. Barfi")
    d=int(input("enter the item number: "))
    if d==1:
            print("price of jalebi si 400")
    elif d==2:
            print("price of pista is 200")
    elif d==3:
            print("price of barfi is 350")
menu=float(input("enter your billing amount: "))
pc=input("Enter your promocode:")

if pc=="zom50":
    print("You will get 50% off")
    menu=menu*50/100
    print("final billing amount is: ",menu,"\nThank you! visit again")
elif pc=="zom40":
    print("you will get 40% off")
    menu=menu*40/100
    print("final billing amount is: ",menu,"\nThank you! visit again")
else:
    print("not a valid promo code, Thank you visit again\n your final amount is : ",menu)

print("Choose your service: ")
print("1. Self Service\n2. Home delivery")
ser=int(input("enter the number of preference: "))
if ser==1:
    print("Thank you! visit again")
elif ser==2:
    name=input("enter your name: ")
    address=input("enter your adress: ")
    print("Thank you for service")
else:
    print("choose something or get out")
