# coding=utf-8
#!/usr/bin/python3.5

# import Session, engine, and Base from the .entities.entity module.
from .entities.entity import Base, Session, engine

# import the Exam class from the .entities.exam module.
from .entities.exam import Exam, ExamSchema

from flask import Flask, jsonify, request

# create database schema
Base.metadata.create_all(engine)

app = Flask(__name__)

# if len(exams) == 0:
#     # create and persist dummy exam
#     python_exam = Exam('SQLAlchemy Exam', 'Test your knowledge about SQLAlchemy.', 'script')
#     session.add(python_exam)
#     session.commit()
#     session.close()

#     # reload exams
#     exams = session.query(Exam).all()

# Show existing exams
# print('### Exams: ')
# print the exams retrieved from the database.
# for ex in exams:
#     print('({}). {} - {}'.format(ex.id, ex.title, ex.description))

@app.route('/exams')
def get_exams():
    # start session
    session = Session()

    # check for existing data and query all instances of Exam.
    exams_obj = session.query(Exam).all()

    # transforming into JSON-serializable objects
    schema = ExamSchema(many = True)
    exams = schema.dump(exams_obj)

    # serializing into JSON
    session.close()
    return jsonify(exams.data)

@app.route('/exams', methods = ['POST'])
def add_exams():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())
    exam = Exam(**posted_exam.data, created_by = 'HTTP post request')

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema.dump(exam).data
    session.close()
    return jsonify(new_exam), 201
