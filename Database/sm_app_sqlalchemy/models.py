import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped

Base = so.declarative_base()

# Define the likes table as a secondary table
likes_table = sa.Table(
    'likes',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
    sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id'))
)

class User(Base):
    __tablename__ = 'users'
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    age: so.Mapped[int]
    gender: so.Mapped[str]
    nationality: so.Mapped[str]
    posts: so.Mapped[list['Post']] = so.relationship(back_populates='user')
    liked_posts: so.Mapped[list['Post']] = so.relationship(secondary=likes_table, back_populates='liked_by_users')
    comments_made: so.Mapped[list['Comment']] = so.relationship(back_populates='user')

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, gender='{self.gender}', nationality='{self.nationality}')"

class Post(Base):
    __tablename__ = 'posts'
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    title: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    description: so.Mapped[str] = so.mapped_column(sa.Text, nullable=False)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('users.id'))
    user: Mapped["User"] = so.relationship('User', back_populates='posts')
    liked_by_users = so.relationship('User', secondary=likes_table, back_populates='liked_posts')
    comments = so.relationship('Comment', back_populates='post')

    def __repr__(self):
        return f"Post(title='{self.title}', description='{self.description}', user_id={self.user_id})"

class Comment(Base):
    __tablename__ = 'comments'
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    post_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('posts.id'), nullable=False)
    comment: so.Mapped[str] = so.mapped_column(sa.Text, nullable=False)
    post = so.relationship('Post', back_populates='comments')
    user = so.relationship('User', back_populates='comments_made')

    def __repr__(self):
        return f"Comment(user_id={self.user_id}, post_id={self.post_id}, comment='{self.comment}')"