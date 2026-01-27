from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Athlete(BaseModel):
    name: Annotated[str, Field(description='Athlete name', examples='John', max_length=50)]
    id: Annotated[str, Field(description='Athlete id', examples='43267895401', max_length=11)]
    age: Annotated[str, Field(description='Athlete age', examples=25)]
    weight: Annotated[PositiveFloat, Field(description='Athlete weight', examples=75.5)]
    height: Annotated[PositiveFloat, Field(description='Athlete height', examples=1.75)]
    sex: Annotated[str, Field(description='Athlete sex', examples='M', max_length=1)]