import sqlite3
import task

conn = sqlite3.connect('task_database.db')
cur = conn.cursor()

taak = task.task(1, "testtaak", "False","een test taak","","een dag","nog niet klaar",2,1,"morgen")

print(taak.new_task_to_tuple())

cur.execute('''INSERT INTO Tasks VALUES(NULL,?,?,?,?,?,?,?,?,?)''', taak.new_task_to_tuple())

conn.commit()
conn.close()






