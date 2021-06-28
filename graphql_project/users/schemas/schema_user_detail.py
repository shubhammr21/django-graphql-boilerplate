import graphene
from graphql import GraphQLError
from graphql_project.users.schemas.schema import UserType, User


class UserDetailQuery(graphene.ObjectType):
    user = graphene.Field(UserType, pk=graphene.Int(required=True))
    me = graphene.Field(UserType)

    def resolve_user(self, info, pk):
        return User.objects.get(pk=pk)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Not logged in!')
        return user
