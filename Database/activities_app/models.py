from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
class Base(DeclarativeBase):
    pass


# Sets up a Person table
class Person(Base):
    __tablename__ = 'persons'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)

    # Gives a representation of a Person (for printing out)
    def __repr__(self):
        return f"<Person({self.id=}, {self.first_name=}, {self.last_name=})>"

    # Include a method:
    def greeting(self):
        print(f'{self.first_name} says "hello"!')

