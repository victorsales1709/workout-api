from uuid import uuid4
from fastapi import APIRouter, Body, status
from workout_api.categories.models import CategorieModel
from workout_api.categories.schemas import CategorieIn, CategorieOut
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', summary='Create a new categorie', status_code=status.HTTP_201_CREATED, response_model=CategorieOut,)
async def post(db_session: DatabaseDependency, categorie_in: CategorieIn = Body(...)) -> CategorieOut:
    categorie_out = CategorieOut(id=uuid4(), **categorie_in.model_dump())
    categorie_model = CategorieModel(**categorie_out.model_dump())

    db_session.add(categorie_model)
    await db_session.commit()
    return categorie_out