from schema import User, Listing, Review
import json2obj

class Query(ObjectType):
    reviews = List(Review, id=Int(required=True))

    def resolve_reviews(self, args, context, info):
        reviews = api_call(args.get("id"))["reviews"]
        return json2obj(json.dumps(reviews))
