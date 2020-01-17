import sqlalchemy as db

class Database():
    
    engine = db.create_engine('postgresql://alexandercawood:1234@localhost/lang_db')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")
    
    def fetchByQuery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        data_list = []
        for data in fetchQuery.fetchall():
            data_list.append(data)
        
        return data_list
    
    def saveData(self, Lang):
        self.connection.execute(f"""INSERT INTO lang VALUES('{Lang.lang}', '{Lang.abbr}')""")
    
    def add_abbr(self, abbr):
        
        code_l = self.fetchByQuery('language_code')
        id = code_l[-1][0]
        id = int(id)+1
        self.connection.execute(f"""INSERT INTO language_code VALUES('{id}', '{abbr}')""")
    
    def deleteData(self, lang, abbr):
        self.connection.execute(f"""DELETE FROM lang WHERE lan_abbr like '{abbr}' AND lan_language like '{lang}' """)
    
    def executeQuery(self, query, values=""):
        self.connection.execute(f"""{query}""",values)