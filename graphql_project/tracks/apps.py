from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TracksConfig(AppConfig):
    name = "graphql_project.tracks"
    verbose_name = _("Tracks")

    def ready(self):
        try:
            import graphql_project.tracks.signals  # noqa F401
        except ImportError:
            pass
