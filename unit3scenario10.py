import csv
import sys

def read_file(fn):
    a = []
    with open(fn, "r") as f:
        r = csv.DictReader(f)
        for x in r:
            a.append(x)
    return a


def display(a):
    for x in a:
        print("ID:", x["Equipment ID"])
        print("Name:", x["Name"])
        print("Category:", x["Category"])
        print("Quantity:", x["Quantity"])
        print("Condition:", x["Condition"])
        print("Location:", x["Location"])
        print()


def search(a, y):
    for x in a:
        if x["Equipment ID"] == y:
            print("\nEquipment Found")
            print("ID:", x["Equipment ID"])
            print("Name:", x["Name"])
            print("Category:", x["Category"])
            print("Quantity:", x["Quantity"])
            print("Condition:", x["Condition"])
            print("Location:", x["Location"])
            return

    print("Equipment not found")


if len(sys.argv) != 2:
    print("Enter filename as command line argument")
    sys.exit()

fn = sys.argv[1]

a = read_file(fn)

print("Sports Equipment Details\n")
display(a)

y = input("Enter Equipment ID to search: ")
search(a, y)