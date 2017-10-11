import pymysql
import regex
# Open database connection
db = pymysql.connect("localhost","root","","phone" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# add new contact
def ADD():
    AddName = input("Enter the Name:")
    AddPhone = input("Enter the phone number:")
    regName = regex.compile("(^[A-Z]\'?[A-Z]?[a-z]*\,?\s?[A-Z]?\'?[A-Z]?[a-z]*\-?\s?[A-Z]?[a-z]*\.?$)")
    regPhone = regex.compile("(^\+?\d{0,3}\s?\(?\d{0,5}(\)?[-.\s]?\d{3}[-.\s]?\d{4})?$)")
    matchName = regex.search(regName, AddName)
    match = regex.search(regPhone, AddPhone)
    if match and matchName:
        sql = "insert into PhoneDir(Name, Phone_Number) VALUES(%s, %s)"
        cursor.execute(sql, (AddName, AddPhone))
        print("Contact has been added successfully.")
    else:
        print("Contact is unacceptable.")

# delete contact using name
def DeleteByName():
    DelName = input("Enter Name:")
    sql = "delete from PhoneDir WHERE Name = %s"
    cursor.execute(sql, DelName)

# delete contact using phone number
def DeleteByNumber():
    DelNumber = "'" + input("Enter Number:") + "'"
    cursor.execute("delete from PhoneDir WHERE Phone_Number = "+ DelNumber +";")

# show all contacts
def ShowAll():
    cursor.execute("select * from PhoneDir;")
    all = cursor.fetchall()
    for row in all:
        print(row)

print("1: Add contact")
print("2: Delete contact by name")
print("3: Delete contact by Phone number")
print("4: Show all contacts")
Choice = int(input("Enter your choice:"))

if (Choice == 1):
    ADD()
elif (Choice == 2):
    DeleteByName()
elif (Choice == 3):
    DeleteByNumber()
elif (Choice == 4):
    ShowAll()

db.commit()
# disconnect from server
db.close()