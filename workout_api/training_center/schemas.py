from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description='TC Name', examples=['TC Alpha and Omega'], max_length=20)]
    adress: Annotated[str, Field(description='TC Adress', examples=['X Street, Q05'], max_length=60)]
    owner: Annotated[str, Field(description='TC Owner', examples=['Ronald'], max_length=30)]