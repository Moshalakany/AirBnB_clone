#!/usr/bin/python3
"""import neaded classes."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review class.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
