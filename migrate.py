import sqlalchemy as db
class Database():
    
    engine = db.create_engine('postgresql://alexandercawood:1234@localhost/lang_db')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")
        
        self.connection.execute(f"""DROP TABLE language_code""")
        create_table = ''' 
            CREATE TABLE language_code(
                id int NOT NULL PRIMARY KEY,
                code VARCHAR(255) NOT NULL
            );
            '''
        self.connection.execute(f"""{create_table}""")
        print("created table")

        c_list = ["R","ZH","TH","KO","RO","SL","HR","MS","UK",
        "ETS","AR",'HE',"CS","DE","EN","FR","EL","HU","IT","JA",
        "DA","PL","ZF","NL","NO","PT","SK","RU","ES","TR","FI",
        "SV","BG","LT","LV","Z1","AF","IS","CA","SH","ID"]

        id = 0
        for x in c_list:
            id +=1
            self.connection.execute(f'''INSERT INTO language_code(id,code) VALUES({id},'{x}') ''')
            print("inserted: " + x)

Database()
        