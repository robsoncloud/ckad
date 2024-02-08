import psycopg2

class Database:
    def __init__(self, dbname, user, host, password, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.__conn = None
        self.__cur = None
        
    def connect(self):
        try:
            self.__conn = psycopg2.connect(database=self.dbname, user=self.user, host=self.host, password=self.password, port=self.port)
            self.__cur = self.__conn.cursor()
            print("Database connection established")
        except Exception as e:
            print("An error occurred while connecting to the database")
            raise
    def execute_query(self, query):
        try:
            if self.__conn is None:
                return
            self.__cur.execute(query)
            rows = self.__cur.fetchall()
            return rows
        except Exception as e:
            print("An error occurred while executing a query")
            raise
    def close(self):
        if self.__conn:
            self.__cur.close()
            self.__conn.commit()
            self.__conn.close()
            print("Database connection closed")
        
        