![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Banking Management System

## 🛠️ Description

This Python script is a simple console-based application for a bank management system. It connects to a MySQL database and provides several functionalities:

#   1. Create a New Account: 
        This function asks the user for their name, account number, date of birth, address, contact number, and opening balance. It then inserts these details into the ACCOUNT_DETAILS and AMOUNT tables in the database.
#   2. Deposit: 
        This function asks the user for the account number and the amount they want to deposit. It then updates the balance in the AMOUNT table for the given account number.
#   3. Withdraw: 
        This function asks the user for the account number and the amount they want to withdraw. It then updates the balance in the AMOUNT table for the given account number.
#   4. Balance Enquiry: 
        This function asks the user for the account number and then fetches and displays the balance from the AMOUNT table for the given account number.
#   5. Display Customer Details: 
        This function asks the user for the account number and then fetches and displays all the details from the ACCOUNT_DETAILS table for the given account number.
#   6. Close an Account: 
        This function asks the user for the account number and then deletes the corresponding records from the ACCOUNT_DETAILS and AMOUNT tables in the database.

The menu function displays these options to the user and calls the appropriate function based on the user’s choice. The menu will keep displaying until the user chooses to exit.

 - The `ACCOUNT_DETAILS` table is expected to have columns for name, account number, date of  birth, address, contact number, and opening balance. 
 - The `AMOUNT` table is expected to have columns for name, account number, and balance.

## ⚙️ Modules Used

Modules required are `mysql.connector` and `getpass`. 
Use the below command to install these dependencies.

```pip install mysql-connector-python```
```pip install getpass```

## Steps to be taken care before executing the script

- Make Sure MySQL server is running on the same machine (localhost), and there’s a MySQL database named `Bank_Management` with the necessary tables and columns. 
- The MySQL server should allow connections from the Python script with the `username`, `root` and the `password` *******,
- Replace these values with the actual values from your MySQL server setup. 
- Be sure to keep your MySQL server credentials secure and avoid hardcoding them into your script.

 
## 🌟 How to run

- Running the script is really simple! Just open a terminal in the folder where your script is located and run the following command:

```sh
python main.py
```

