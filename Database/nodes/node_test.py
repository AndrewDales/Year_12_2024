from sqlalchemy import Column, Integer, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the association table for many-to-many relationships
NodeRelation = Table('node_relation', Base.metadata,
    Column('node_id_a', Integer, ForeignKey('node.id')),
    Column('node_id_b', Integer, ForeignKey('node.id')),
)

# Define the Node model
class Node(Base):
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define the self-reference relationship to other nodes
    related_nodes = relationship(
        "Node",
        secondary=NodeRelation,
        primaryjoin=id == NodeRelation.c.node_id_a,
        secondaryjoin=id == NodeRelation.c.node_id_b
    )

# Create the database and tables
engine = create_engine('sqlite:///:memory:')  # Use an in-memory SQLite database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example usage: create and connect some nodes
node1 = Node(name="Node 1")
node2 = Node(name="Node 2")
node3 = Node(name="Node 3")

session.add_all([node1, node2, node3])
session.commit()

# Connect node1 to node2 and node3 (undirected)
node1.related_nodes.extend([node2, node3])
session.commit()

# Retrieve and verify the connections
print(node1.name, "is connected to:", [n.name for n in node1.related_nodes])
print(node2.name, "is connected to:", [n.name for n in node2.related_nodes])

# Inspect the table
inspector = inspect(engine)
print(inspector.get_table_names())