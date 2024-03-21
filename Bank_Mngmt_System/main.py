import mysql.connector
from getpass import getpass


def connect_to_db():
    while True:
        try:
            password = getpass('Enter password to connect to the database[Bank_Management]:')
            mydb = mysql.connector.connect(host='localhost', user='root', password=password, database='Bank_Management')
            print('Connencted to Database Successfully...')
            return mydb
        except mysql.connector.Error as err:
            print(f'Something went wrong: {err}')
            print('Invalid password!!!... Please try again : ')

mydb = connect_to_db()

def CreateAccount():
    name = input('Enter your Name : ')
    Acc_no = input('Enter Account Number : ')
    dob = input('Enter Your Date of Birth : ')
    Address = input('Enter your Address : ')
    Contact_no = int(input('Enter your Contact Num : '))
    Opening_bal = int(input('Enter the amount for the opening balance : '))
    data1=(name,Acc_no,dob,Address,Contact_no,Opening_bal)
    data2=(name,Acc_no,Opening_bal)
    sql1 = ('insert into ACCOUNT_DETAILS values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into AMOUNT values (%s,%s,%s)')
    x = mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print('Data entered sucessfully...')
    menu()


def Deposit():
    Amount = int(input('Enter the amount you want to deposit : '))
    Acc_no = input('Enter Account Number : ')
    a = 'select BALANCE from AMOUNT where ACC_NO=%s'
    data = (Acc_no,)
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    # print(result)
    total = result[0]+ Amount
    sql = 'update AMOUNT set BALANCE=%s where ACC_NO=%s'
    b = (total,Acc_no)
    x.execute(sql,b)
    mydb.commit()
    print('Amount Rs',Amount, 'is Deposited Sucessfully...')
    print('The toal balance is : ',total)
    menu()


def Withdraw():
    Amount = int(input('Enter the amount you want to Withdraw : '))
    Acc_no = input('Enter Account Number : ')
    a = 'select BALANCE from AMOUNT where ACC_NO=%s'
    data = (Acc_no,)
    x = mydb.cursor()
    x.execute(a,data)
    result = x.fetchone()
    #print(result)
    total = result[0] - Amount
    sql = 'update AMOUNT set BALANCE=%s where ACC_NO=%s'
    b = (total,Acc_no)
    x.execute(sql,b)
    mydb.commit()
    print('Amount Rs',Amount, 'is Withdrawed Sucessfully...')
    print('The toal balance is : ',total)
    menu()


def BalanceEnquiry():
    Acc_no = input('Enter Account Number : ')
    bal =  'select * from AMOUNT where ACC_NO=%s'
    data = (Acc_no,)
    x = mydb.cursor()
    x.execute(bal,data)
    result = x.fetchone()
    print('Balance for Account_num',Acc_no, 'is : ', result[-1])
    menu()


def DisplayDetails():
    Acc_no = input('Enter Account Number : ')
    bal =  'select * from ACCOUNT_DETAILS where ACC_NO=%s'
    data = (Acc_no,)
    x = mydb.cursor()
    x.execute(bal,data)
    result = x.fetchone()
    print('Details of the Account_num ',Acc_no,'are :')
    for i in result:
        print(i,end=', ')
    menu()


def CloseAccount():
    Acc_no = input('Enter Account Number : ')
    sql1 = 'delete from ACCOUNT_DETAILS where ACC_NO=%s'
    sql2 = 'delete from AMOUNT where ACC_NO=%s'
    data = (Acc_no,)
    x = mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print('Account ',Acc_no, 'is closed Sucessfully !!')
    menu()


def menu():
    print('''
            1. Create a New Account
            2. Deposit
            3. Withdraw
            4. Balance Enquiry
            5. Display Customer Details
            6. Close an Account  
             ''')      
    while True:
        choice = input("Please choose the option to perform (or 'Exit/exit' to Quit): ")
        if choice == 'exit' or choice == 'Exit':
            break
        elif choice == '1':
            CreateAccount()
        elif choice == '2':
            Deposit()
        elif choice == '3':
            Withdraw()
        elif choice == '4':
            BalanceEnquiry()
        elif choice == '5':
            DisplayDetails()
        elif choice == '6':
            CloseAccount()
        else:
            print('Oops!! Invalid Option, -- Please choose the correct option : ')
            menu()

menu()