from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class TrainingCenterIn(BaseSchema):
    name: Annotated[str, Field(description='TC Name', examples=['TC Alpha and Omega'], max_length=20)]
    adress: Annotated[str, Field(description='TC Adress', examples=['X Street, Q05'], max_length=60)]
    owner: Annotated[str, Field(description='TC Owner', examples=['Ronald'], max_length=30)]

class TrainingCenterAthlete(BaseSchema):
    id: Annotated[int, Field(description='Athlete ID', examples=[1])]
    name: Annotated[str, Field(description='Athlete Name', examples=['John Doe'], max_length=30)]

class TrainingCenterOut(TrainingCenterIn):
    id: Annotated[int, Field(description='TC ID', examples=[1])]