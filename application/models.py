from . import db


class Language(db.Model):
    """Model for user accounts."""

    __tablename__ = 'language_new'

    language = db.Column(db.String(255),
                        primary_key=True,
                         index=False,
                         unique=True,
                         nullable=False)
    
    code = db.Column(db.String(2),
                         index=False,
                         unique=True,
                         nullable=False)

    def __init__(self, language,code):
        self.language = language
        self.code = code

class Lang():
    def __init__(self,lang, abbr):
        self.lang = lang
        self.abbr = abbr

class Language_code():
    def __init__(self,id, code):
        self.id = id
        self.code = code