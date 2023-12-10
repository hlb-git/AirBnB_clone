#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
import models
from models.base_model import BaseModel


class State(BaseModel):
    """State class handles all application states"""
    name = ''
