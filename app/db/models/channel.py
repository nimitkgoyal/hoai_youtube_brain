from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Channel(Base):
    __tablename__ = "channels"

    channel_id: Mapped[str] = mapped_column(String(100), primary_key = True)
    title: Mapped[str] = mapped_column(String(255), nullable = False)
    description: Mapped[str | None] = mapped_column(String(1000))
    Country: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime | None] = mapped_column(DateTime(timezone = True))
    thumbnail_url: Mapped[str | None] = mapped_column(String(500))
    subscriber_count: Mapped[int | None] = mapped_column(Integer)
    video_count: Mapped[int | None] = mapped_column(Integer)
    view_count: Mapped[int | None] = mapped_column(Integer)

    videos = relationship(
        "Video",
        back_populates = "channel",
        cascade = "all, delete-orphan",
    )