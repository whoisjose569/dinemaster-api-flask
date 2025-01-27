import sqlalchemy as sa
from .base import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.sql import func

class Orders(db.Model):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    restaurant_table_id: Mapped[int] = mapped_column(ForeignKey("restaurant_table.id"), nullable=True)
    create_at: Mapped[datetime] = mapped_column(sa.DateTime, server_default=func.now())
    order_status: Mapped[str] = mapped_column(sa.String(20), default="Em preparo")
    delivery_type: Mapped[str] = mapped_column(sa.String(20), nullable=True)
     
    restaurant_table: Mapped["RestaurantTable"] = relationship(back_populates="orders", lazy="joined")