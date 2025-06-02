# app/db/models/__init__.py

from .user import User
from .agricultural_area import AgriculturalArea

__all__ = ["User", "AgriculturalArea"]

_ = User
_ = AgriculturalArea
