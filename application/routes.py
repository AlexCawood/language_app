from database import Database
from flask import Flask,request,render_template,redirect
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Language, Lang, Language_code

db1 = Database()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        
        lang = request.form['lang']
        abbr = request.form['abbr']
        if len(abbr) == 2:
            languages = Language(lang, abbr) 
            db.session.add(languages)
            db.session.commit()
            return redirect("/")
        else:
            print("Please enter a language code of 2 characters")
            return redirect("/")
    
    elif request.method == "GET":
        results = Language.query.all()
        print(results)
        lang_code = db1.fetchByQuery('language_code')
        return render_template("index.html", results=results,lang_code=lang_code)


@app.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_lang = request.form['lang_to_delete']
        delete_abbr = request.form['abbr_to_delete']
        to_del = Language.query.filter(Language.language == delete_lang and Language.code == delete_abbr).delete()
        db.session.commit()
        # db1.deleteData(delete_lang,delete_abbr)
        return redirect("/delete")

    elif request.method == "GET":
        results = Language.query.all()
        return render_template("delete.html", results=results)

@app.route('/add_abbr', methods=['POST','GET'])
def add_abbr():
    if request.method == "POST":
        abbr = request.form['abbr']
        if len(abbr) == 2:
            db1.add_abbr(abbr)
            return redirect("/add_abbr")
        else:
            print("Please enter a language code of 2 characters")
            return redirect("/add_abbr")

    elif request.method == "GET":
        results = db1.fetchByQuery('language_code')
        return render_template("add_abbr.html", abbr_r=results)



if __name__ == '__main__':
    app.run()