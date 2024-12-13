import sqlalchemy as sa
from .base import db
from sqlalchemy.orm import Mapped, mapped_column

class RestaurantTable(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    table_number: Mapped[int] = mapped_column(sa.Integer, unique=True)
    table_status: Mapped[str] = mapped_column(sa.String)
    
    