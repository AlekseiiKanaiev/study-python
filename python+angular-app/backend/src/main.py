# coding=utf-8
#!/usr/bin/python3.5

# import Session, engine, and Base from the .entities.entity module.
from entities.entity import Base, Session, engine

# import the Exam class from the .entities.exam module.
from entities.exam import Exam

# create database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data and query all instances of Exam.
exams = session.query(Exam).all()


if exams == 0:
    # create and persist dummy exam
    python_exam = Exam('SQLAlchemy Exam', 'Test your knowledge about SQLAlchemy.', 'script')
    session.add(python_exam)
    session.commit()
    session.close()

    # reload exams
    exams = session.query(Exam).all()

# Show existing exams
print('### Exams: ')
# print the exams retrieved from the database.
for ex in exams:
    print('({}). {} - {}'.format(ex.id, ex.title, ex.description))