# coding=utf-8

# represent the entity

from sqlalchemy import String, Column

from .entity import Base, Entity

from marshmallow import Schema, fields

# class called Exam that inherits from Entity and from Base
class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
# using the Schema class of marshmallow to define a new class called ExamSchema. 
# We will use this class to transform instances of Exam into JSON objects.
class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
