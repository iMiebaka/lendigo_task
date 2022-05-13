import uuid
import random
from datetime import datetime, timedelta
from core import db
import ast


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    by = db.Column(db.String(150))
    descendants = db.Column(db.Integer)
    public_id = db.Column(db.Integer, db.ForeignKey('post_id.id'))
    # kids = db.Column(db.Integer, db.ForeignKey('kids.id'))
    custom = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer)
    time = db.Column(db.Integer)
    title = db.Column(db.String(150))
    text = db.Column(db.Text)
    type = db.Column(db.Integer, db.ForeignKey('type.id'))
    url = db.Column(db.String(150))
    created_on = db.Column(db.DateTime, default=datetime.now())

    @property
    def sheetSummary(self):
        trans = {}
        trans["by"] = self.by
        trans["descendants"] = self.descendants 
        trans["public_id"] = self.public_id 
        trans["kids"] = self.get_kids_short
        trans["score"] = self.score
        trans["title"] = self.title
        if self.title != "":
            trans["title"] = self.title
        trans["type"] = self.get_type

        if self.url != "":
            trans["url"] = self.url

        return trans
    @property
    def get_kids_short(self):
        comments = Comments.query.filter_by(parent_id=self.id).order_by(Comments.created_on.desc())\
        .all()
        kids = []
        for _ in comments:
            kids.append(_.public_id)
        return kids

    @property
    def get_type(self):
        type = Type.query.filter_by(id = self.type).first()
        if type is not None:
            return type.name

        
class PostId(db.Model):
    __tablename__ = "post_id"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    custom = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, default=datetime.now())

# class Kids(db.Model):
#     __tablename__ = "kids"
#     id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, db.ForeignKey('post_id.id'))
#     public_id = db.Column(db.Integer)
#     created_on = db.Column(db.DateTime, default=datetime.now())

class Comments(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    by = db.Column(db.String(150))
    public_id = db.Column(db.Integer)
    kid = db.Column(db.Boolean, default=False)
    replied = db.Column(db.Boolean, default=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    time = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.now())

       

class Type(db.Model):
    __tablename__ = "type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.now())
    