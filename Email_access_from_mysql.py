import pymysql as ms
import os
from dotenv import load_dotenv
def email_retrival():
    load_dotenv()
    Data_base_Name = os.getenv('Data_Base_Name')
    User = os.getenv('User')
    db_password = os.getenv('Mysql_password')

    conn = ms.connect(
                    db = Data_base_Name,
                    host = 'localhost',
                    port = 3306,
                    user = User,
                    passwd= db_password
                    )

    cur = conn.cursor()

    cur.execute('''SELECT email FROM data_info''')
    conn.commit()

    list_of_emails = cur.fetchall()

    cur.close()
    conn.close()

    sorted_list_emails = [row[0] for row in list_of_emails if row[0] is not None]

