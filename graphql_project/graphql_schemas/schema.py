import graphene
from graphql_project.tracks.schemas.schema_track_list import TrackListQuery
from graphql_project.tracks.schemas.schema_like_list import LikeListQuery
from graphql_project.tracks.schemas.schema_create_track import CreateTrackMutation
from graphql_project.tracks.schemas.schema_update_track import UpdateTrackMutation
from graphql_project.tracks.schemas.schema_delete_track import DeleteTrackMutation
from graphql_project.tracks.schemas.schema_create_like import CreateLikeMutation
from graphql_project.users.schemas.schema_create_user import CreateUserMutation
from graphql_project.users.schemas.schema_user_detail import UserDetailQuery
from graphql_project.users.schemas.schema_jwt import JWTMutation


class Query(
    TrackListQuery,
    UserDetailQuery,
    LikeListQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    CreateTrackMutation,
    UpdateTrackMutation,
    DeleteTrackMutation,
    CreateUserMutation,
    CreateLikeMutation,
    JWTMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
