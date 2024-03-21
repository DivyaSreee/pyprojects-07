from currency_converter import CurrencyConverter
import tkinter as tk
c = CurrencyConverter()

# print(c.convert(10,'USD','INR'))

window = tk.Tk()
window.geometry('500x360')
window.title('Currency Converter')

def clicked():
    amount = int(entry1.get())
    currency1 = entry2.get()
    currency2 = entry3.get()
    result = c.convert(amount,currency1,currency2)
    res_label = tk.Label(window, text=result, font= 'Times 20 bold').place(x = 130, y = 250)



label = tk.Label(window,text='Currency Convertor',font='Times 20 bold').pack() # can use place() as place(x=100, y= 40)
# need 3 user inputs so defining all these inputs as lables in windows

label1 = tk.Label(window,text='Enter Amount : ',font='Times 14 bold').place(x = 30, y = 50 )
entry1 = tk.Entry(window)

label2 = tk.Label(window,text='Enter Currency : ',font='Times 14 bold').place(x = 30, y = 90 )
entry2 = tk.Entry(window)

label3 = tk.Label(window,text='Enter Desired Currency : ',font='Times 14 bold').place(x = 30, y = 130 )
entry3 = tk.Entry(window)

button = tk.Button(window, text='Click',font='Times 14 bold',command=clicked).place(x = 200, y= 180)
entry1.place(x = 260 , y = 57)
entry2.place(x = 260 , y = 97)
entry3.place(x = 260 , y = 135)
window.mainloop()
