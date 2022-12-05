import pymysql
import datetime as dt

db = pymysql.connect(host='192.168.155.101', user='hypark',
                     password='parkhy0115!', port=3308, db='sleep', charset='utf8')

cursor = db.cursor()

while 1:
    print("\n\n-------------------------------------------")
    print("[2020069022]------------[Hyeong-Yeong Park]")
    print("[-------Sleep Time & Condition Diary--------]")
    print("[-----------View all sleep data-------------]")
    print("[1] Sign in")
    print("[2] Sleep Time Record")
    print("[3] Sleep Condition Survey")
    print("[4] View Weekly Report")
    print("[5] View Montly Report")
    print("[6] View all sleep data")
    print("[7] Exit")
    menu = int(input())
    if menu == 1:
        print("[------------------Sign in------------------]")
        sql = "INSERT INTO USER (Fname, Lname, Name, ID, Password, Bdate, Sex) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        print(
            "Input your personal information (Fname, Lname, Name, ID, Passwrod, Bdate, Sex)")
        print("What is your First name?")
        Fname = str(input())
        print("What is your Last name?")
        Lname = str(input())
        Name = Fname + " " + Lname
        print("Your ID: ")
        ID = str(input())
        print("Password: ")
        Password = str(input())
        print("What is your Birth-day?")
        Bdate = str(input())    # DATE datatype으로 받아오는 수정 필요
        print("What is your sex? (Male/Female)")
        Sex = str(input())
        print("Name: ", Name, "\nID: ", ID, "\nB-Day: ", Bdate, "\nSex: ", Sex)
        cursor.execute(sql, (Fname, Lname, Name, ID, Password, Bdate, Sex))
    elif menu == 2:
        print("[-------------Sleep Time Record-------------]")
        sql = "INSERT INTO SLEEP TIME (UserID, Snumber, Date, Stime, Etime, Time) VALUES (%s, %s, %s, %s, %s, %s)"
        # sql = "DELETE FROM Book WHERE bookname = %s"
        print("Inpute your ID: ")
        UserID = str(input())
        print("Input the record number: ")
        Snumber = int(input())
        print("Inpute the date: ")
        Date = str(input())   # DATE datatype으로 받아오는 수정 필요
        print("Input the time when you start sleep: ")
        Stime = str(input())    # TIME datatype으로 받아오는 수정 필요
        print("Input the time when you wake up: ")
        Etime = str(input())    # TIME datatype으로 받아오는 수정 필요
        Time = Stime - Etime - 12
        cursor.execute(sql, UserID, Snumber, Date, Stime, Etime, Time)
        # db.commit()
    elif menu == 3:
        print("[----------Sleep Condition Survey-----------]")
        print("Did you sleep well?\n1. Very Good\n2. So so\n3. Bad\n")
        s1 = int(input())
        print("Did you have a nightmare?\n1. Yes\n2. No\n")
        s2 = int(input())
        # Calculate the sleep condition score
        score = 0
        if s1 == 1:
            score += 5
        elif s1 == 2:
            score += 3
        elif s1 == 3:
            score += 1
        if s2 == 1:
            score += 1
        elif s2 == 2:
            score += 5
        
        if score > 7:
            condition = "Good"
        elif score > 4:
            condition = "So so"
        else:
            condition = "Bad"
        print("Condition : ", condition)
        cursor.execute(sql, searchBook)
        result = cursor.fetchall()
        for data in result:
            print(data)
    elif menu == 4:
        print("[------------View Montly Report-------------]")
        print("Select the week")
        sql = "SELECT * FROM Book"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
    elif menu == 5:
        print("[------------View Montly Report-------------]")
    elif menu ==6:
        print("[-----------View all sleep data-------------]")
        sql = "SELECT * FROM SLEEP_TIME"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
    elif menu == 7:
        break


    db.commit()
