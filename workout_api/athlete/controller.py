from datetime import datetime, timezone
from uuid import uuid4
from fastapi import APIRouter, Body, status
from starlette.exceptions import HTTPException
from workout_api.athlete.models import AthleteModel
from workout_api.athlete.schemas import AthleteIn, AthleteOut
from workout_api.categories.models import CategorieModel
from workout_api.contrib.dependencies import DatabaseDependency
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