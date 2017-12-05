import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from sqlalchemy.orm import sessionmaker
from database import db_session, Person as PersonModel

class Persons(SQLAlchemyObjectType):
	class Meta:
	    model = PersonModel
	    interfaces = (relay.Node, )

class PersonType(graphene.ObjectType):
	name = 'Person'
	description = 'Person Model'

	first_name = graphene.String()
	last_name = graphene.String()
	gender = graphene.String()
	country = graphene.String()
	friends = graphene.List(lambda: PersonType)

	def resolve_friends(person, args, context, info):
		query = Persons.get_query(context)
		return [query.filter(PersonModel.id == f.friend_id).first() for f in person.friends]

class Query(graphene.ObjectType):
	node = relay.Node.Field()
	find_person = graphene.Field(
		PersonType,
		id = graphene.String()
	)

	def resolve_find_person(self, args, context, info):
		print(context)
		query = Persons.get_query(context)
		id = args.get('id')
		return query.filter(PersonModel.id == id).first()

schema = graphene.Schema(query=Query, types=[Persons])
