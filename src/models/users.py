import sqlalchemy as sa
from .base import db
from sqlalchemy.orm import Mapped, mapped_column

class Users(db.Model):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(sa.String(10), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    
