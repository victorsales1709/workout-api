from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from workout_api.categories.models import CategorieModel
from workout_api.categories.schemas import CategorieIn, CategorieOut
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post('/', summary='Create a new categorie', status_code=status.HTTP_201_CREATED, response_model=CategorieOut,)
async def post(db_session: DatabaseDependency, categorie_in: CategorieIn = Body(...)) -> CategorieOut:
    categorie_out = CategorieOut(id=uuid4(), **categorie_in.model_dump())
    categorie_model = CategorieModel(**categorie_out.model_dump())

    db_session.add(categorie_model)
    await db_session.commit()
    return categorie_out

@router.get('/', summary='Get all categories', status_code=status.HTTP_200_OK, response_model=list[CategorieOut])
async def query(db_session: DatabaseDependency) -> list[CategorieOut]:
    categories = list[CategorieOut] = (await db_session.execute(select(CategorieModel))).scalars().all()
    return categories

@router.get('/id', summary='Get a categorie by ID', status_code=status.HTTP_200_OK, response_model=CategorieOut)
async def query(id: UUID4, db_session: DatabaseDependency) -> CategorieOut:
    categorie: CategorieOut = (await db_session.execute(select(CategorieModel).filter_by(id=id))).scalars().first()
    if not categorie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Categorie not found: {id}')
    
    return categorie