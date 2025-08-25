from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, foreign
from sqlalchemy import String, ForeignKey

class RoomsOrm(Base):
    __tablename__ = "rooms"

    id:Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels_id"))
    title: Mapped[String]
    description: Mapped[String | None]
    price: Mapped[int]
    quantity:Mapped[int]

