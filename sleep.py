import pymysql

db = pymysql.connect(host='192.168.155.101', user='hypark', password='parkhy0115!', port=4567, db='sleep', charset='utf8')

cursor = db.cursor()

print("DB connected!")