import graphene
from graphql_project.tracks.models import Like
from graphql_project.tracks.schemas.schema import LikeType


class LikeListQuery(graphene.ObjectType):
    likes = graphene.List(LikeType)

    def resolve_likes(self, info):
        return Like.objects.all()
