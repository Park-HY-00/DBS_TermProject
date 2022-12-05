import pymysql

db = pymysql.connect(host='192.168.155.101', user='hypark',
                     password='parkhy0115!', port=3308, db='sleep', charset='utf8')

cursor = db.cursor()

while 1:
    print("-------------------------------------------")
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
        Fname = str(input())
        Lname = str(input())
        Name = str(input())
        ID = str(input())
        Password = str(input())
        Bdate = str(input())    # DATE datatype으로 받아오는 수정 필요
        Sex = str(input())
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
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("Search for (book's name) :")
        searchBook = str(input())
        cursor.execute(sql, searchBook)
        result = cursor.fetchall()
        for data in result:
            print(data)
    elif menu == 4:
        print("[------------View Montly Report-------------]")
        sql = "SELECT * FROM Book"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
    elif menu == 5:
        print("[------------View Montly Report-------------]")
    elif menu ==6:
        print("[-----------View all sleep data-------------]")
    elif menu == 7:
        break


    db.commit()
