from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from graphql_project.tracks.models import Track


def get_model_fields(model):
    return [field.name for field in model._meta.fields if field.name is not 'id']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Track)
    # search_fields = ["name"]
