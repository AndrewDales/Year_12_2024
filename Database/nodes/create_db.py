import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.log import echo_property

from models import Base, Node

# Create an engine
engine = sa.create_engine('sqlite:///:memory:', echo=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Add some nodes
nodes = [Node(name=str(i)) for i in range(5)]
# nodes[0].is_router = True

# Add some edges
edges = [(0, 1),
         (0, 3),
         (0, 4),
         (1, 2),
         (1, 4),
         (2, 3),
]

for i, j in edges:
    nodes[i].right_nodes.append(nodes[j])

with so.Session(bind=engine) as session:
    session.add_all(nodes)
    session.commit()
    import sqlalchemy as sa
    import sqlalchemy.orm as so
    from sqlalchemy.log import echo_property

    from models import Base, Node

    # Create an engine
    engine = sa.create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Add some nodes
    nodes = [Node(name=str(i)) for i in range(5)]
    # nodes[0].is_router = True

    # Add some edges
    edges = [(0, 1),
             (0, 3),
             (0, 4),
             (1, 2),
             (1, 4),
             (2, 3),
             ]

    for i, j in edges:
        nodes[i].right_nodes.append(nodes[j])

    with so.Session(bind=engine) as session:
        session.add_all(nodes)
        session.commit()

        for node in nodes:
            print(node)
            print("Connected nodes:")
            for cnode in node.connected_nodes:
                print(cnode)
            print()
        print(node)
        print("Connected nodes:")
        for cnode in node.connected_nodes:
            print(cnode)
        print()