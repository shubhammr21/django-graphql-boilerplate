import graphene
from graphql import GraphQLError
from graphql_project.tracks.models import Track
from graphql_project.tracks.schemas.schema import TrackType


class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Must be logged in')

        track = Track.objects.get(
            id=kwargs.get('track_id')
        )
        if track.posted_by != user:
            raise GraphQLError('You are not permitted to update this track')
        if kwargs.get('title'):
            track.title = kwargs.get('title')
        if kwargs.get('description'):
            track.description = kwargs.get('description')
        if kwargs.get('url'):
            track.url = kwargs.get('url')
        track.save()
        return UpdateTrack(track=track)


class UpdateTrackMutation(graphene.ObjectType):
    update_track = UpdateTrack.Field()
