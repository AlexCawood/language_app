from models import Database, Lang

db = Database()
# language = input('Enter Language: ' )
# abbr = input('Enter Abbriviation: ')

# lang = Lang(language, abbr)
# db.saveData(lang)
print('Successfully added')
check_db = input('input db: ')
results = db.fetchByQuery(check_db)
print(results)
print('Success')