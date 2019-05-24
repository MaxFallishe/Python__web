import config
import sqlite3



conn = sqlite3.connect('TZ_base.db')
cursor = conn.cursor()



cursor.execute("SELECT questionTEXT FROM First_4_questions")

results = cursor.fetchall()
for i in results:
    print(i[0])


conn.close()
