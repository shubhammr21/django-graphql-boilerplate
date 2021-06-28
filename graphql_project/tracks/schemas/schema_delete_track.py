import graphene
from graphql import GraphQLError
from graphql_project.tracks.models import Track


class DeleteTrack(graphene.Mutation):
    track_id = graphene.Int()

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Must be logged in')

        track = Track.objects.get(
            id=kwargs.get('track_id')
        )
        if track.posted_by != user:
            raise GraphQLError('You are not permitted to delete this track')
        track.delete()
        return DeleteTrack(track_id=kwargs.get('track_id'))


class DeleteTrackMutation(graphene.ObjectType):
    delete_track = DeleteTrack.Field()
