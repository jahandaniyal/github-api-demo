# -*- coding: utf-8 -*-
"""
Defines a schema class called PopularitySchema.
"""

from flask_marshmallow import Schema
from marshmallow.fields import Integer


class PopularitySchema(Schema):
    """
    This schema is used for serialising and deserialising GitHub API's JSON response object.
    """
    class Meta:
        """
        Attributes:
        fields -- [forks, stars]
        strict -- True
        """
        # Fields to expose
        fields = ["forks", "stars"]
        strict = True

    forks = Integer(data_key="forks_count")
    stars = Integer(data_key="stargazers_count")
