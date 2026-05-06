from typing import Annotated

from pydantic import ConfigDict, Field, UUID4
from workout_api.contrib.schemas import BaseSchema

class TrainingCenterIn(BaseSchema):
    name: Annotated[str, Field(description='TC Name', examples=['TC Alpha and Omega'], max_length=20)]
    address: Annotated[str, Field(description='TC Address', examples=['X Street, Q05'], max_length=60)]
    owner: Annotated[str, Field(description='TC Owner', examples=['Ronald'], max_length=30)]

class TrainingCenterAthlete(BaseSchema):
    name: Annotated[str, Field(description='TC Name', examples=['TC Alpha and Omega'], max_length=20)]

class TrainingCenterOut(TrainingCenterIn):
    name: str
    model_config = ConfigDict(from_attributes=True)