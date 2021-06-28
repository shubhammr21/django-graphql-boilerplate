from graphene_django import DjangoObjectType
from graphql_project.tracks.models import Track, Like


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class LikeType(DjangoObjectType):
    class Meta:
        model = Like
