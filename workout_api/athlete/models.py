from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class AthleteModel(BaseModel):
    __tablename__ = 'athletes'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    id: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categorie: Mapped['CategorieModel'] = relationship(back_populates='athlete')
    categorie_id: Mapped[int] = mapped_column(ForeignKey('categories.pk_id'))
    training_center: Mapped['TrainingCenterModel'] = relationship(back_populates='athlete')
    categorie_id: Mapped[int] = mapped_column(ForeignKey('training_centers.pk_id'))