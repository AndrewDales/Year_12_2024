from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Person, Activity

# Connect to the activities database
engine = create_engine('sqlite:///activities.sqlite', echo=True)

sess = Session(engine)
persons = sess.scalars(select(Person)).all()
vera = sess.scalars(select(Person).where(Person.first_name == 'Vera')).first()
for person in persons:
    person.greeting()
persons[0].last_name = "Smith"
new_person = Person(first_name='Bob', last_name='Jones')
# sess.add(new_person)
sess.commit()

person_1 = sess.scalars(select(Person)).first()