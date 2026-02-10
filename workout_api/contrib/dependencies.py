from workout_api.configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]