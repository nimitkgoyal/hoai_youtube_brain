from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Video(Base):
    __tablename__ = "videos"

    video_id: Mapped[str] = mapped_column(String(100), primary_key = True)

    channel_id: Mapped[str] = mapped_column(
        ForeignKey("channels.channel_id"),
        nullable = False,
    )

    url: Mapped[str | None] = mapped_column(String(500))
    title: Mapped[str] = mapped_column(String(255), nullable = False)
    description: Mapped[str | None]

    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone = True))
    thumbnail_url: Mapped[str | None] = mapped_column(String(500))

    duration: Mapped[str | None] = mapped_column(String(50))

    view_count: Mapped[int | None] = mapped_column(Integer)
    like_count: Mapped[int | None] = mapped_column(Integer)
    comment_count: Mapped[int | None] = mapped_column(Integer)

    tags: Mapped[str | None]
    Category: Mapped[str | None]
    Language: Mapped[str | None]

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone = True))

    channel = relationship(
        "Channel",
        back_populates = "videos",
    )