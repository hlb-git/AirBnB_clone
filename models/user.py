#!/usr/bin/python3
"""
User Class from Models Module
"""
from models.base_model import BaseModel
import os


class User(BaseModel):
    """
    User Class handles all application users
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
