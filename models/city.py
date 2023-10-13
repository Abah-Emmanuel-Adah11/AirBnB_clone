#!/usr/bin/python3
"""This defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """This represent a city.

    Attributes are:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
