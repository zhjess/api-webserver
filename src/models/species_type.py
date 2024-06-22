from init import db, ma
from marshmallow import fields
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class SpeciesType(db.Model):
    __tablename__ = 'species_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())

    species: Mapped['Species'] = relationship(back_populates='species_types')

class SpeciesTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')