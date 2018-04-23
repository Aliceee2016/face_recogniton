import pymysql

db = pymysql.connect(
    host = "115.159.71.166",
    user = "root",
    password = "root",
    database = "Intelligent_office",
    charset = 'utf8')
cursor = db.cursor()

def select(sql):
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		return results
	except:
		print("Error: unable to fetch data")
	db.close()

# insert、update、delete
def operate(sql):
	try:
		cursor.execute(sql)
		db.commit()
		print("success")
	except:
		print("fail")
		db.rollback()
	db.close()



