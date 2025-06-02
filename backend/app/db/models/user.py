# app/db/models/user.py

# =======================================================================================================
# --- Importações ---                                                                               #####
# =======================================================================================================

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from app.db.base_class import Base 

if TYPE_CHECKING:
    from .agricultural_area import AgriculturalArea

# =======================================================================================================
# --- Classe Base de Usuário ---                                                                    #####
# =======================================================================================================
class User(Base):
    """
    Modelo de tabela para os usuários.
    Esta tabela armazena informações sobre os usuários, incluindo email, senha,
    nome completo, status de atividade e permissões de superusuário.
    Relaciona-se com a tabela de áreas agrícolas, permitindo que um usuário possua várias áreas.
    A tabela também define o relacionamento com a tabela de áreas agrícolas,
    permitindo operações de cascata como exclusão em massa.
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True) 
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    agricultural_areas: Mapped[List["AgriculturalArea"]] = relationship(
        "AgriculturalArea", back_populates="owner", cascade="all, delete-orphan")
