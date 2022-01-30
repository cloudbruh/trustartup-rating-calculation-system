from datetime import timedelta, timezone
import datetime
from math import log

from .global_rating import calculate_global_rating
from ..models import Startup, StartupRating

def calculate_user_rating(user_id: int, startups: list[Startup]) -> list[StartupRating]:
    ratings: list[StartupRating] = list()

    for startup in startups:
        startup_rating = calculate_global_rating(startup)

        for like in startup.likes:
            if like.user_id != user_id:
                continue

            time_passed: timedelta = datetime.utcnow().replace(tzinfo=timezone.utc) - like.created_at
            startup_rating.rating += 1 / log(time_passed.total_seconds() / 86400 + 2)
        
        for comment in startup.comments:
            if comment.user_id != user_id:
                continue

            time_passed: timedelta = datetime.utcnow().replace(tzinfo=timezone.utc) - comment.created_at
            startup_rating.rating += 2 / log(time_passed.total_seconds() / 86400 + 2)
        
        for post in startup.posts:
            for like in post.likes:
                if like.user_id != user_id:
                    continue

                time_passed: timedelta = datetime.utcnow().replace(tzinfo=timezone.utc) - like.created_at
                startup_rating.rating += 1 / log(time_passed.total_seconds() / 86400 + 2)
            
            for comment in post.comments:
                if comment.user_id != user_id:
                    continue

                time_passed: timedelta = datetime.utcnow().replace(tzinfo=timezone.utc) - comment.created_at
                startup_rating.rating += 2 / log(time_passed.total_seconds() / 86400 + 2)
        
        ratings.append(startup_rating)
    
    return ratings
