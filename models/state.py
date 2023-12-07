#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class handles all application states"""
    name = ''
