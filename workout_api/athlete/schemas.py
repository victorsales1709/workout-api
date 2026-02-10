from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

from workout_api.contrib.schemas import OutMixin

class Athlete(BaseModel):
    name: Annotated[str, Field(description='Athlete name', example='John', max_length=50)]
    id: Annotated[str, Field(description='Athlete id', example='43267895401', max_length=11)]
    age: Annotated[str, Field(description='Athlete age', example=25)]
    weight: Annotated[PositiveFloat, Field(description='Athlete weight', example=75.5)]
    height: Annotated[PositiveFloat, Field(description='Athlete height', example=1.75)]
    sex: Annotated[str, Field(description='Athlete sex', example='M', max_length=1)]

class AthleteIn(Athlete):
    pass

class AthleteOut(AthleteIn, OutMixin):
    pass