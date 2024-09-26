#Adding dictionary items in test

inventory = { 
    'Apple' : 20,
    'Bananas' : 40,
    'Oranges' : 50
}


request = input("What would you like to buy ?")

if request == 'Apple':
    print("The price of the Apple comes to:", inventory ["Apple"])

elif request == 'Bananas':
    print("The price of Bananas comes to:", inventory ['Bananas'])

elif request == 'Oranges':
    print("The price of Oranges comes to", inventory ['Oranges'])

else:
    print("Your order has not been recognised.")