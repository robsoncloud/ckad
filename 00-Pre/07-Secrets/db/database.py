import psycopg2


class DatabaseHandler:
    def __init__(self, dbname, username, password, host, port):
        self.dbname = dbname
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.__conn = None
        self.__cur = None
    
    def connect(self):
        try:
            self.__conn = psycopg2.connect(dbname=self.dbname,user=self.username, password=self.password, host=self.host, port=self.port)
            self.__cur = self.__conn.cursor()
            print("Connection to database has been established")
        except Exception as e:
            print(f"An issue occurred while connecting ${e}")
            raise
            
    def execute_query(self, query):
        try:
            if self.__conn is None:
                return
            self.__cur.execute(query)
            rows = self.__cur.fetchall()
            return rows
        except Exception as e:
            print(f"An issue occurred while executing query ${e}")
            raise
            

    def close(self):
        try:
            if self.__conn is None:
                return
            self.__cur.close()
            self.__conn.commit()
            self.__conn.close()
            print("Connection to the database has been closed")
        except Exception as e:
            print(f"An issue occured while closing the connection - ${self.host} - error: ${e}")
            raise