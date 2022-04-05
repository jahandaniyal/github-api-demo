from flask_marshmallow import Schema
from marshmallow.fields import Integer


class PopularitySchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["forks", "stars"]
        strict = True

    forks = Integer(data_key="forks_count")
    stars = Integer(data_key="stargazers_count")
