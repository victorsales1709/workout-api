from typing import Annotated, Optional, Literal
from pydantic import BaseModel, Field, PositiveFloat

from workout_api.categories.schemas import CategorieIn
from workout_api.contrib.schemas import OutMixin
from workout_api.training_center.schemas import BaseSchema, TrainingCenterAthlete

class Athlete(BaseSchema):
    name: Annotated[str, Field(description='Athlete name', example='John', max_length=50)]
    athlete_id: Annotated[str, Field(description='Athlete id', example='43267895401', max_length=11)]
    age: Annotated[int, Field(description='Athlete age', example=25)]
    weight: Annotated[PositiveFloat, Field(description='Athlete weight', example=75.5)]
    height: Annotated[PositiveFloat, Field(description='Athlete height', example=1.75)]
    sex: Annotated[str, Field(description='Athlete sex', example='M', max_length=1)]
    categorie: Annotated[CategorieIn, Field(description='Athlete categorie')]
    training_center: Annotated[TrainingCenterAthlete, Field(description='Athlete training center')]

class AthleteIn(Athlete):
    pass

class AthleteOut(AthleteIn, OutMixin):
    pass

class AthleteUpdate(BaseSchema):
    name: Annotated[Optional[str], Field(None, description='Athlete name', example='John', max_length=50)]
    age: Annotated[Optional[int], Field(None, description='Athlete age', example=25)]

class AthleteQuery(BaseModel):
    name: Optional[str] = Field(None, description="Filter by athlete name")

    sort: Optional[Literal["name_asc", "name_desc"]] = Field(
        "name_asc",
        description="Sort athletes by name"
    )

    page: int = Field(1, ge=1, description="Page number")
    limit: int = Field(10, ge=1, le=100, description="Items per page")