#!/usr/bin/python3
"""defining the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """representing a city.

    Attributes are:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
