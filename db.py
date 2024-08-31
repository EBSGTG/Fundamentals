import psycopg2

conn = psycopg2.connect(database="test",
                        host="localhost",
                        user="postgres",
                        password="1809",
                        port="5432")
conn.autocommit = True
cursor = conn.cursor()

# cursor.execute('''Insert into test(id, time, description, category, summa) values (1,'2','3','4','5')''')
