import threading
import socket
import _sqlite3

IP = '192.168.9.111'
PORT = 8888
db = '2025-11-27\\01.db'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#client.connect((IP,PORT))

class register:
    def __init__(self,m_db=db):
        self.db = m_db
        self.lock = threading.Lock()
        self._init_db()
    def _init_db(self):
        with _sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                user_id integer PRIMARY KEY AUTOINCREMENT,  
                user_name TEXT,            
                user_password TEXT  );     '''    
            )     
    def sign_in(self,user,pw):
        with self.lock:
            with _sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    '''
                    select user_password from user 
                    where user_name = ?
                ''',(user,)
                )
                password = cursor.fetchone()
                if password == None:
                    print('登陆失败')
                    return False
                if pw == password[0]:
                    print('登陆成功')
                    return True
                else:
                    print('登陆失败')
                    return False
    def sign_up(self,user,pw):
        with self.lock:
            with _sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute(
                '''
                select 1 from user where user_name = ?
                    ''' ,(user,)
                )
                result = cursor.fetchone()
                if not result:
                    cursor.execute(
                        '''
                        insert into user (user_name,user_password) values (?,?)
                        ''' , (user,pw)
                    )
                else:
                    print('重名')
                conn.commit()
def test():
    r =register()
    #r.sign_up('impha','sss')
    r.sign_in ('s','ss')
    r.sign_in ('impha','sss')
def clear():
    with _sqlite3.connect(db) as conn:
        cursor =conn.cursor()
        cursor.execute(
            '''
            SELECT 1 FROM sqlite_master 
            WHERE type = 'table' AND name = ?; 
            ''',('user',)
        )
        result = cursor.fetchone()
        if result:
            cursor.execute(
                '''
                drop table user
                '''
        )
clear()
test()
