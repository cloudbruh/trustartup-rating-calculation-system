from datetime import datetime, timedelta
from math import log
from .models import Startup, StartupRating

def calculate_global_rating(startup: Startup) -> StartupRating:
    rating: float = 0

    for post in startup.posts:
        post_rating: float = 0
        post_rating += len(post.likes)
        post_rating += len(post.comments)

        time_passed: timedelta = datetime.now() - post.created_at
        post_rating *= 1 / log(time_passed.total_seconds / 86400 + 2)

        rating += post_rating
    
    rating += len(startup.comments)
    rating += len(startup.follows)
    rating += len(startup.likes)

    return StartupRating(id=startup.id, rating=rating)
