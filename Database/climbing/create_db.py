import sqlalchemy as sa
from Database.climbing.models import Base

# Create an engine
def construct_db():
    engine = sa.create_engine('sqlite:///climbing.db', echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    construct_db()