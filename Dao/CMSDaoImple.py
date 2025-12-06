from Dao.AbstractCMSDao import CMSDaoService
from DbConnection.ConnectionDB import ConnectionDB
from pymysql.cursors import DictCursor
from models.user import user
from typing import List

class CMSDaoImplementation(CMSDaoService):

    SEARCH_USER_PASS_RESULT = """ SELECT * FROM user WHERE username = %s AND password = %s
"""

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    def verification_login(self, username, password):
        try:
            cursor = self.conn.cursor(DictCursor)  #cursor open to db
            cursor.execute(self.SEARCH_USER_PASS_RESULT, (username, password))
            row = cursor.fetchone()

            if not row:
                raise Exception("Invalid username or password!")

            logged_user = user(
                user_id=row['user_id'],
                username=row['username'],
                password=row['password'],
                role_id=row['role_id']
            )

            # role based navigation
            match logged_user.role_id:
                case 1:
                    print("Admin login successful")
                case 2:
                    print("Receptionist login successful")
                case 3:
                    print("Doctor login successful")
                case 4:
                    print("Pharmacist login successful")
                case _:
                    print("Unknown role")

            return logged_user

        except Exception as e:
            print("Login Error:", e)

        finally:
            cursor.close()
