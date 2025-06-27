import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.ext.associationproxy import association_proxy

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
class Base(so.DeclarativeBase):
    pass

edges_table = sa.Table('edges',
                       Base.metadata,
                       sa.Column('node_left', sa.ForeignKey('nodes.id'), primary_key=True),
                       sa.Column('node_right', sa.ForeignKey('nodes.id'), primary_key=True),
                       )

class Node(Base):
    __tablename__ = 'nodes'
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    name: so.Mapped[str]
    right_nodes: so.Mapped[list['Node']] = so.relationship(
        "Node",
        secondary=edges_table,
        primaryjoin=(id == edges_table.c.node_left),
        secondaryjoin=(id == edges_table.c.node_right),
        back_populates="left_nodes",
    )
    left_nodes: so.Mapped[list['Node']] = so.relationship(
        'Node',
        secondary=edges_table,
        primaryjoin=(id == edges_table.c.node_right),
        secondaryjoin=(id == edges_table.c.node_left),
        back_populates="right_nodes",
    )
    is_router: so.Mapped[bool] = so.mapped_column(default=False)

    def __repr__(self):
        return f"Node({self.name})"

    @property
    def connected_nodes(self):
        return set(self.left_nodes) | set(self.right_nodes)
