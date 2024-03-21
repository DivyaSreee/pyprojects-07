from datetime import datetime

name = input('Please Enter your name : ')
print(f'Welcome to the store...{name} Happy Shopping !!')

# LIst of item displayed
list = '''
Rice - Rs 20/kg
Salt - Rs 30/kg
Sugar - Rs 25/kg
Oil - Rs 80/liter
Maggie - Rs 10/each
Boost - Rs 45/kg
Colgate - Rs 30/each
'''

price = 0
pricelist = []
total_price = 0
final_price = 0
item_list = []
quantity_list = []
price_list = []

# prices for items 


items={'Rice':20,
       'Salt':30,
       'Sugar':25,
       'Oil':80,
       'Maggie':10,
       'Boost':45,
       'Colgate':30}

option = int(input("1 - to show list of items / 2 - exit : "))
if option == 1:
    print(list)
for i in range(len(items)):
    inp = int(input("1 - to buy / 2 - exit : "))
    if inp == 2:
        break
    if inp == 1:
        item_inp = input('Item : ')
        quantity_inp = int(input('Item Quantity : '))
        if item_inp in items.keys():
            price = quantity_inp*(items[item_inp])
            pricelist.append((item_inp,quantity_inp,items,price))
            total_price += price
            item_list.append(item_inp)
            quantity_list.append(quantity_inp)
            price_list.append(price)
            Gst = (total_price * 5 )/100
            final_price = Gst + total_price
        else:
            print('Sorry! Item is not available.')
    else:
        print('Opps!! Please enter the correct option... :  ')

    inp_1 = input('Yes - to bill / No - exit : ')
    if inp_1 == 'Yes':
        pass
        if final_price != 0:
            print(26*'-','Mini SuperMarket',35*'-')
            print(28*' ','Bangalore')
            print('Name :',name,30*' ','Date: ',datetime.now())
            print(80*'-')
            print('S.no',8*" ",'Items',8*' ','Quantity',8*' ','Price')
            for i in range(len(price_list)):
                print(i,11*" ",item_list[i],12*' ',quantity_list[i],12*' ',price_list[i])
            print(80*'-')
            print(50*' ','Total Amount : Rs ',total_price)
            print(50*' ','Gst Amount   : Rs ', Gst)
            print(80*'-')
            print(50*' ','Final Amount : Rs ',final_price)
            print(80*'-')
            print(25*' ', 'Thanks for visiting :>')
            print(80*'-')






