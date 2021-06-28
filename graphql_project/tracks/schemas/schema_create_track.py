import graphene
from graphql import GraphQLError
from graphql_project.tracks.models import Track
from graphql_project.tracks.schemas.schema import TrackType


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Must be logged in')
        track = Track.objects.create(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            url=kwargs.get('url'),
            posted_by=user
        )
        return CreateTrack(track=track)


class CreateTrackMutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
