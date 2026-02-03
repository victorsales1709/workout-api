from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    name: Annotated[str, Field(description='Categorie Name', examples='Scale', max_length=10)]