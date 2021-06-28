import graphene
from graphql import GraphQLError
from graphql_project.tracks.schemas.schema import TrackType, Track, Like
from graphql_project.users.schemas.schema import UserType


class CreateLike(graphene.Mutation):
    user = graphene.Field(UserType)
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Must be logged in to like this track')
        track = Track.objects.get(
            id=kwargs.get('track_id')
        )
        if not track:
            raise GraphQLError('Cannot find track with given track id')
        if Like.objects.filter(user=user, track=track).exists():
            raise GraphQLError('You already liked this track.')
        Like.objects.create(
            user=user,
            track=track
        )
        return CreateLike(track=track, user=user)


class CreateLikeMutation(graphene.ObjectType):
    create_like = CreateLike.Field()
