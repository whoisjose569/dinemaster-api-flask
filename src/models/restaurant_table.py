import sqlalchemy as sa
from .base import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.orders import Orders

class RestaurantTable(db.Model):
    __tablename__ = "restaurant_table"
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    table_number: Mapped[int] = mapped_column(sa.Integer, unique=True)
    table_status: Mapped[str] = mapped_column(sa.String(20), default="livre")
    
    orders: Mapped[list["Orders"]] = relationship(back_populates="restaurant_table", lazy="select")
    
    