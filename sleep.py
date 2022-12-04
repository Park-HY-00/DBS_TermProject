import pymysql

db = pymysql.connect(host='192.168.155.101', user='hypark', password='parkhy0115!', port=3308, db='sleep', charset='utf8')

cursor = db.cursor()

while 1:
    print("-------------------------------------------")
    print("[2020069022]------------[Hyeong-Yeong Park]")
    print("[-------Sleep Time & Condition Diary--------]")
    print("[1] Sign in")
    print("[2] Sleep Time Record")
    print("[3] Sleep Condition Survey")
    print("[4] View Weekly Report")
    print("[5] View Montly Report")
    print("[6] Exit")
    menu = int(input())
    if menu == 1:
        sql = "INSERT INTO USER (Fname, Lname, Name, ID, Password, Bdate, Sex) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        print("Input your personal information (Fname, Lname, Name, ID, Passwrod, Bdate, Sex)")
        Fname = str(input())
        Lname = str(input())
        Name = str(input())
        ID = str(input())
        Password = str(input())
        Bdate = str(input())    # DATE datatype으로 받아오는 수정 필요
        Sex = str(input())
        cursor.execute(sql, (Fname, Lname, Name, ID, Password, Bdate, Sex))
    elif menu == 2:
        sql = "DELETE FROM Book WHERE bookname = %s"
        print("Input the book's name that you want to delete: ")
        deleteBookname = str(input())
        cursor.execute(sql, deleteBookname)
        db.commit()
    elif menu == 3:
        sql = "SELECT * FROM Book WHERE bookname = %s"
        print("Search for (book's name) :")
        searchBook = str(input())
        cursor.execute(sql, searchBook)
        result = cursor.fetchall()
        for data in result:
            print(data)
    elif menu == 4:
        sql = "SELECT * FROM Book"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row_data in result:
            print(row_data)
    elif menu == 5:
        break

    db.commit()