# app/db/models/agricultural_area.py

# =======================================================================================================
# --- Importações ---                                                                               #####
# =======================================================================================================

from sqlalchemy import Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from geoalchemy2 import Geometry

from app.db.base_class import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

# =======================================================================================================
# --- Classe Base de Usuário ---                                                                    #####
# =======================================================================================================

class AgriculturalArea(Base):
    """
    Modelo de tabela para áreas agrícolas.
    Esta tabela armazena informações sobre áreas agrícolas, incluindo geometria, área em hectares,
    e a relação com o usuário proprietário.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    
    geometry: Mapped[Geometry] = mapped_column(
        Geometry(geometry_type='POLYGON', srid=4326, spatial_index=True, from_text='ST_GeomFromEWKT', name='geometry'),
        nullable=False
    )

    area_hectares: Mapped[float | None] = mapped_column(Float, nullable=True)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    owner: Mapped["User"] = relationship(back_populates="agricultural_areas")

    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)