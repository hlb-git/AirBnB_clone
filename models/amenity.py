#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""
    name = ''
