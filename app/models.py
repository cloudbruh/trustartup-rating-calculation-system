from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class Like(BaseModel):
    id: int
    user_id: int
    created_at: datetime

class Comment(BaseModel):
    id: int
    user_id: int
    text: str
    replied_id: int | None = None
    updated_at: datetime
    created_at: datetime

class Post(BaseModel):
    id: int
    startup_id: int
    header: str
    text: str
    comments: list[Comment]
    likes: list[Like]
    updated_at: datetime
    created_at: datetime

class Follow(BaseModel):
    id: int
    user_id: int
    startup_id: int
    created_at: datetime

class Startup(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    ending_at: datetime
    funds_goal: Decimal
    rating: float
    posts: list[Post]
    comments: list[Comment]
    follows: list[Follow]
    likes: list[Like]
    updated_at: datetime
    created_at: datetime

class StartupRating(BaseModel):
    id: int
    rating: float
