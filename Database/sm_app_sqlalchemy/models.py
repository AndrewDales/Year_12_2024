import sqlalchemy as sa
import sqlalchemy.orm as so

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
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    name: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    age: so.Mapped[int] = so.mapped_column(sa.Integer)
    gender: so.Mapped[str] = so.mapped_column(sa.String)
    nationality: so.Mapped[str] = so.mapped_column(sa.String)
    posts: so.Mapped[list['Post']] = so.relationship('Post', back_populates='user')
    liked_posts: so.Mapped[list['Post']] = so.relationship('Post', secondary=likes_table, back_populates='liked_by_users')

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age}, gender={self.gender}, nationality={self.nationality})"

class Post(Base):
    __tablename__ = 'posts'
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    title: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    description: so.Mapped[str] = so.mapped_column(sa.Text, nullable=False)
    user_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('users.id'))
    user = so.relationship('User', back_populates='posts')
    liked_by_users = so.relationship('User', secondary=likes_table, back_populates='liked_posts')
    comments = so.relationship('Comment', back_populates='post')

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, description={self.description}, user_id={self.user_id})"

class Comment(Base):
    __tablename__ = 'comments'
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    post_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('posts.id'), nullable=False)
    comment: so.Mapped[str] = so.mapped_column(sa.Text, nullable=False)
    post = so.relationship('Post', back_populates='comments')

    def __repr__(self):
        return f"Comment(id={self.id}, user_id={self.user_id}, post_id={self.post_id}, comment={self.comment})"