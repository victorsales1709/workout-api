from datetime import datetime, timezone
from uuid import uuid4
from fastapi import APIRouter, Body, status
from pydantic import UUID4
from starlette.exceptions import HTTPException
from workout_api.athlete.models import AthleteModel
from workout_api.athlete.schemas import AthleteIn, AthleteOut, AthleteUpdate
from workout_api.categories.models import CategorieModel
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from workout_api.training_center.models import TrainingCenterModel

router = APIRouter()

@router.post('/', summary='Create a new athlete', status_code=status.HTTP_201_CREATED, response_model=AthleteOut)
async def post(db_session: DatabaseDependency, athlete_in: AthleteIn = Body(...)):
    categorie_name = athlete_in.categorie.name
    training_center_name = athlete_in.training_center.name

    categorie = (await db_session.execute(select(CategorieModel).filter_by(name=categorie_name))).scalars().first()

    if not categorie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Categorie not found: {categorie_name}')

    training_center = (await db_session.execute(select(TrainingCenterModel).filter_by(name=training_center_name))).scalars().first()

    if not training_center:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Training center not found: {training_center_name}')

    try:
        
        athlete_out = AthleteOut(id=uuid4(), created_at=datetime.now(timezone.utc).replace(tzinfo=None), **athlete_in.model_dump())
        athlete_model = AthleteModel(**athlete_out.model_dump(exclude={'categorie', 'training_center'}))
        
        athlete_model.categorie_id = categorie.pk_id
        athlete_model.training_center_id = training_center.pk_id

        db_session.add(athlete_model)
        await db_session.commit()
        
    except Exception as e:
        print(f"{e}") 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Error"
        )

    return athlete_out

@router.get('/', summary='Get all athletes', status_code=status.HTTP_200_OK, response_model=list[AthleteOut])
async def query(db_session: DatabaseDependency) -> list[AthleteOut]:
    result = await db_session.execute(
        select(AthleteModel).options(
            selectinload(AthleteModel.training_center)
        )
    )
    athletes = result.scalars().all()

    return [AthleteOut.model_validate(athlete) for athlete in athletes]

@router.get('/{id}', summary='Get an athlete by ID', status_code=status.HTTP_200_OK, response_model=AthleteOut,)
async def get(id: UUID4, db_session: DatabaseDependency) -> AthleteOut:
    athlete: AthleteModel = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()
    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Athlete not found: {id}')
    
    return athlete

@router.patch('/{id}', summary='Update an athlete by ID', status_code=status.HTTP_200_OK, response_model=AthleteOut)
async def get(id: UUID4, db_session: DatabaseDependency, athlete_up: AthleteUpdate = Body(...)) -> AthleteOut:
    athlete: AthleteModel = (await db_session.execute(select(AthleteModel).filter_by(id=id))).scalars().first()
    if not athlete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Athlete not found: {id}')
    athlete_update = athlete_up.model_dump(exclude_unset=True)
    for key, value in athlete_update.items():
        setattr(athlete, key, value)

    await db_session.commit()
    await db_session.refresh(athlete)

    return AthleteOut.model_validate(athlete)