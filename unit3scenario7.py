import csv
import sys
import re

def read_file(filename):
    customers = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for customer in reader:
            customers.append(customer)

    return customers


def display_customers(customers):
    for customer in customers:
        print("Account Number:", customer["Account Number"])
        print("Name:", customer["Name"])
        print("Address:", customer["Address"])
        print("Phone:", customer["Phone"])
        print("Balance:", customer["Balance"])
        print()


def search_customer(customers, account_number):

    if not re.match(r"^[0-9]{10}$", account_number):
        print("Invalid Account Number")
        return

    for customer in customers:
        if customer["Account Number"] == account_number:
            print("\nCustomer Found")
            print("Account Number:", customer["Account Number"])
            print("Name:", customer["Name"])
            print("Address:", customer["Address"])
            print("Phone:", customer["Phone"])
            print("Balance:", customer["Balance"])
            return

    print("Customer not found")


if len(sys.argv) != 2:
    print("Enter filename as command line argument")
    sys.exit()

filename = sys.argv[1]

customers = read_file(filename)

print("Bank Customer Details\n")
display_customers(customers)

account_number = input("Enter Account Number to search: ")
search_customer(customers, account_number)