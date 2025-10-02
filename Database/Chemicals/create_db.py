import sqlalchemy as sa
from Database.Chemicals.models import Base

# Create an engine
def construct_db():
    engine = sa.create_engine('sqlite:///chemicals.db', echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    construct_db()