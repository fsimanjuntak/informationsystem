from graphene import ObjectType, List
from schema import User, Listing, Review

class Query(ObjectType):
    reviews = List(Review, id=Int(required=True))
