import datetime
import re
import mysql.connector

demodb = mysql.connector.connect(
    host='localhost', user='root', passwd='12345678')
democursor = demodb.cursor()
democursor.execute("create database if not exists ssbs")
demodb.commit()

demodb = mysql.connector.connect(
    host='localhost', user='root', passwd='12345678', database='ssbs')
democursor = demodb.cursor()
democursor.execute(
    "create table if not exists user(user varchar(30), password varchar(30))")
demodb.commit()
democursor.execute(
    "create table if not exists event(id int primary key auto_increment, name varchar(30), date date, location varchar(30), price int, seats int)")
demodb.commit()
democursor.execute("create table if not exists seat(id int, ename varchar(30),uname varchar(30),e_date varchar(30),b_date varchar(30),no_of_seat int,price int)")


def login():
    l = []
    print("################Login to Your Account################")
    user = str(input('Enter username: '))
    user = user.upper()
    password = str(input('Enter password: '))
    democursor.execute("select user from user")
    for i in democursor:
        l.append(i[0].upper())
    if user in l:
        democursor.execute("select password from user where user='"+user+"'")
        for i in democursor:
            pas = i[0]
        if password == pas:
            print("Login Successful")
            return 1, user
        else:
            print("Invalid Password")
            return 0, user
    else:
        print("User Not Found")
        return 0, user


def craccount():
    l = []

    print("################ Create Your Account ################")
    user = str(input('Enter username: '))
    user = user.upper()
    democursor.execute("select user from user")
    for i in democursor:
        l.append(i[0].upper())
    if user in l:
        print("User already exists")
        craccount()
        return 0
    else:
        pass
    password = str(input('Enter password: '))
    democursor.execute("insert into user values('"+user+"','"+password+"')")
    demodb.commit()
    print("Account Created")


def disevent(user):
    print("Event List::")
    democursor.execute("select * from event")
    for i in democursor:
        id = str(i[0])
        name = str(i[1])
        date1 = str(i[2])
        location = str(i[3])
        price = str(i[4])
        seat = str(i[5])
        print("ID: "+id+"\nName: "+name+"\nDate: "+date1 +
              "\nLocation: "+location+"\nPrice: "+price+"\nSeats: "+seat)


def add(user):
    print("################ Add Event ################")
    name = input('Name of the event: ')
    date = input('Enter Date of the event(YYYY-MM-DD): ')
    location = input('Enter Location of the event: ')
    price = int(input('Enter Price of the ticket: '))
    seats = int(input('Enter Number of seats: '))

    democursor.execute("insert into event(name,date,location,price,seats) values('" +
                       name+"','"+date+"','"+location+"',"+str(price)+","+str(seats)+")")
    demodb.commit()
    



def remove(user):
    print("################ Remove Event ################")
    democursor.execute("select * from event")
    for i in democursor:
        print("Event ID:"+str(i[0]))
        print("Event Name:"+str(i[1]))
    id = int(input('Enter ID of the event to be removed: '))
    
    democursor.execute("delete from event where id='"+str(id)+"'")
    demodb.commit()

    print("Event Delete Successfully!")

def edit(user):
    print("################ Edit Event ################")
    disevent(user)
    id = int(input('Enter ID of the event to be edited: '))
    name = input('New Name of the event: ')
    date = input('New Date of the event(YYYY-MM-DD): ')
    location = input('New Location of the event: ')
    price = int(input('New Price of the ticket: '))
    seats = int(input('New Number of seats: '))

    democursor.execute("update event set name='"+name+"', date='"+date+"', location='" +
                       location+"', price="+str(price)+", seats="+str(seats)+" where id="+str(id))
    demodb.commit()


def select(user):
    disevent(user)
    # democursor.execute("select * from event where")
    sel_event = input("Select Event ID : ")
    max_seat = 0
    democursor.execute("select seats from event where id="+str(sel_event))
    for i in democursor:
        max_seat += int(i[0])
        
    democursor.execute("select name from event where id="+str(sel_event))
    for i in democursor:
        name = i[0]
        
    democursor.execute("select date from event where id="+str(sel_event))
    for i in democursor:
        edate = i[0]
        
    democursor.execute("select price from event where id="+str(sel_event))
    for i in democursor:
        price = i[0]
        
    bdate = str(datetime.date.today())
        
    print("Maximum Seats Available : "+str(max_seat))
    no_s = int(input("Enter Number of Seats to be booked : "))
    if no_s <= max_seat:
        new_seat = max_seat - no_s
        democursor.execute("update event set seats="+str(new_seat) +
                           " where id="+str(sel_event))
        demodb.commit()
        
        democursor.execute("insert into seat values(%s,%s,%s,%s,%s,%s,%s)",(sel_event,name,user,edate,bdate,no_s,price))
        demodb.commit()
        
        print("Seats Booked Successfully")
        print("Receipt")
        print("User ID: "+str(user))
        print("Event Name "+str(name)+" and ID "+str(sel_event))
        print("Event Date: "+str(edate))
        print("Booking Date: "+str(bdate))
        print("NO of Seats Book: "+str(no_s))
        print("Ticket Price: "+str(price))
        print("")
    else:
        print("No of Seats Exceeded")


def user1(user):

    print("\nStadium Seat Booking System")
    print("--------------------------")
    print("1. Display event list")
    print("2. Select seat")
    print("0. Go Back to Login")

    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        disevent(user)
        user1(user)
    elif choice2 == 2:
        select(user)
        user1(user)
    elif choice2 == 0:
        return 0


def eventmanager(user):

    print("\nStadium Seat Booking System")
    print("--------------------------")
    print("1. Display event list")
    print("2. Add event")
    print("3. Remove event")
    print("4. Edit event details")
    print("5. Select seat")
    print("0. Go Back to Login")

    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        disevent(user)
        eventmanager(user)
    elif choice1 == 2:
        add(user)
        eventmanager(user)
    elif choice1 == 3:
        remove(user)
        eventmanager(user)
    elif choice1 == 4:
        edit(user)
        eventmanager(user)
    elif choice1 == 5:
        select(user)
        eventmanager(user)
    elif choice1 == 0:
        return 0


def main():
    a,user =login()
    if a == 0:
        craccount()
        main()
        return 0
    else:
        pass
    print("""Choose an option:
1.User
2.Event Manager
3.Exit""")
    ch = int(input("->"))
    if ch == 1:
            user1(user)
    elif ch == 2:
            eventmanager(user)
    elif ch==3:
            return 0
    else:
            print("Invalid Choice")
    main()
main()