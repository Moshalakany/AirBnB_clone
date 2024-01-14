#!/usr/bin/python3
"""import neaded classes."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state class.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
