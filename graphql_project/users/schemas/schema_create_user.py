import graphene
from graphql_project.users.schemas.schema import UserType, User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        user = User.objects.create_user(
            name=kwargs.get('name'),
            username=kwargs.get('username'),
            email=kwargs.get('email'),
            password=kwargs.get('password')
        )
        return CreateUser(user=user)


class CreateUserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
