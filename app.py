from models import Database, Lang
from flask import Flask,request,render_template,redirect

app = Flask(__name__)
db = Database()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        
        lang = request.form['lang']
        abbr = request.form['abbr']
        if len(abbr) == 2:
            languages = Lang(lang, abbr) 
            db.saveData(languages)
            return redirect("/")
        else:
            print("Please enter a language code of 2 characters")
            return redirect("/")
    
    elif request.method == "GET":
        results = db.fetchByQuery('lang')
        lang_code = db.fetchByQuery('language_code')
        return render_template("index.html", results=results,lang_code=lang_code)


@app.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_lang = request.form['lang_to_delete']
        delete_abbr = request.form['abbr_to_delete']
        db.deleteData(delete_lang,delete_abbr)
        return redirect("/delete")

    elif request.method == "GET":
        results = db.fetchByQuery('lang')
        return render_template("delete.html", results=results)

@app.route('/add_abbr', methods=['POST','GET'])
def add_abbr():
    if request.method == "POST":
        abbr = request.form['abbr']
        db.add_abbr(abbr)
        return redirect("/add_abbr")

    elif request.method == "GET":
        results = db.fetchByQuery('language_code')
        return render_template("add_abbr.html", abbr_r=results)



if __name__ == '__main__':
    app.run()