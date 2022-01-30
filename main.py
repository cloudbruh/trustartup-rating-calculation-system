from fastapi import FastAPI

from rating_calculation.models import Startup, StartupRating
from rating_calculation.global_rating import calculate_global_rating
from rating_calculation.user_rating import calculate_user_rating

app = FastAPI()

@app.get("/global")
async def global_rating(startup: Startup) -> StartupRating:
    return calculate_global_rating(startup)

@app.get("/user")
async def user_rating(user_id: int, startups: list[Startup]) -> StartupRating:
    return calculate_user_rating(startups)
