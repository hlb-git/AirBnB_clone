#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """City class handles all application cities"""

        state_id = ''
        name = ''
