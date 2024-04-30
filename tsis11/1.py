import psycopg2




conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="Aida2006"
)

cur = conn.cursor()

def queryData():
    cur.execute("SELECT * FROM get_recods_by_pattern('felix')")
    data = cur.fetchall()

    for row in data:
        print(row)

def insertData():
    personName = input('Input new username: ')
    phoneNumber = input('Input new phone number: ')
    conn.autocommit = True 
    cur.execute("CALL insert_data(%s, %s);", (personName, phoneNumber))




def deleteDataWithNameOrPhone(): 
    mode = ''
    x = input("With what parameter you want to delete the person from phonebook?\n1 - with username\n2 - with number\n")
    if(x == '1'):
        mode = 'username'
        name = input('Input the username: ')
        cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", (str(mode), str(name)))
    if(x == '2'):
        mode = 'phone'
        number = input('Input the phone number: ')
        cur.execute("CALL delete_data_by_username_or_phone(%s, %s);", (str(mode), str(number)))



print("What do you want to do?\n\
      1. Return data from the table\n\
      2. Insert contact\n\
      3. Delete with user name or number")
x = input("Enter number 1-5\n")
if(x == '1'):
    queryData()
elif(x == '2'):
    insertData()
elif(x == '3'):
    deleteDataWithNameOrPhone()
conn.commit()
    
cur.close()
conn.close()
# cur.execute(' DELETE FROM postgres.public.phone_book ')

