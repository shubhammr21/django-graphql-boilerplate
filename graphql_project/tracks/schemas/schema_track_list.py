import graphene
from graphql_project.tracks.models import Track
from graphql_project.tracks.schemas.schema import TrackType


class TrackListQuery(graphene.ObjectType):
    tracks = graphene.List(TrackType, search=graphene.String())

    def resolve_tracks(self, info, search=None):
        if search:
            return Track.objects.search(query=search)
        return Track.objects.all()
