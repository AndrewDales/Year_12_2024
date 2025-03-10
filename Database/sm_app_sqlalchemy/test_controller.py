import pytest
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.exc import IntegrityError

from Database.sm_app_sqlalchemy.models import User, Comment, Post, Base
from Database.sm_app_sqlalchemy.write_to_db import write_initial_data
from Database.sm_app_sqlalchemy.controller import Controller

# test_db_location = 'sqlite:///:memory:'
test_db_location = 'sqlite:///test_sm.db'

@pytest.fixture(scope="module")
def db_session():
    engine = sa.create_engine(test_db_location, echo=False)
    Base.metadata.create_all(engine)
    session = so.Session(bind=engine)
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(engine)


class TestDataBase:
    def test_valid_user(self, db_session):
        """ Checks that a User can be added and retrieved from the database"""
        user = User(name = "Bob Dylan", age=81, gender="male")
        db_session.add(user)
        db_session.commit()
        qry = sa.select(User).where(User.name=="Bob Dylan")
        bob = db_session.scalar(qry)
        assert bob.name == "Bob Dylan"
        assert bob.age == 81
        assert bob.gender == "male"
        assert bob.nationality is None


    def test_invalid_user(self, db_session):
        """ Checks that a User missing a name can not be added"""
        user = User(age=7, nationality='British')
        db_session.add(user)
        with pytest.raises(IntegrityError):
            db_session.commit()



class TestController:
    @pytest.fixture(scope="class", autouse=True)
    def test_db(self):
        engine = sa.create_engine(test_db_location, echo=False)
        Base.metadata.create_all(engine)
        write_initial_data(engine)
        yield
        # After the fixture is used drop the data from database in memory
        Base.metadata.drop_all(engine)

    @pytest.fixture(scope="class")
    def controller(self):
        control = Controller(db_location=test_db_location)
        return control

    def test_set_current_user_from_name(self, controller):
        controller.set_current_user_from_name('Alice')
        assert controller.current_user.name == 'Alice'
        assert controller.current_user.age == 30

    def test_get_user_names(self, controller):
        names = controller.get_user_names()
        assert names == ['Alice', 'Bob', 'Charlie', 'Diana']


    def test_create_user(self):
        assert False

    def test_get_posts(self):
        assert False

    def test_get_comments(self):
        assert False

    def test_add_post(self):
        assert False

    def test_like_post(self):
        assert False
