from fastapi import APIRouter
from workout_api.training_center.controller import router as training_center
from workout_api.categories.controller import router as categories
from workout_api.athlete.controller import router as athlete
api_router = APIRouter()
api_router.include_router(athlete, prefix='/athletes', tags=['athletes'])
api_router.include_router(categories, prefix='/categories', tags=['categories'])
api_router.include_router(training_center, prefix='/training_centers', tags=['training_centers'])