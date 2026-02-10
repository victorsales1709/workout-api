from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema

class CategorieIn(BaseSchema):
    name: Annotated[str, Field(description='Categorie Name', example='Scale', max_length=10)]

class CategorieOut(CategorieIn):
    id: Annotated[UUID4, Field(description='Categorie id', example='43267895401', max_length=11)]