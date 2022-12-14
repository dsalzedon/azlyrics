from marshmallow import Schema, fields, post_load

from domain.artist.data import ArtistData, ArtistFiltersData


class ArtistSchema(Schema):
    """Schema to serialize and deserialize Artist objects."""

    id = fields.Int(attribute="id")
    url_name = fields.Str(attribute="url_name")
    name = fields.Str(attribute="name")

    @post_load
    def make_artist(self, data, **kwargs):
        """Creates an ArtistData object from a dictionary."""
        return ArtistData(**data)


class ArtistFiltersSchema(Schema):
    """Schema to serialize Artist objects."""

    field = fields.Str(attribute="field")
    operator = fields.Str(attribute="operator")
    value = fields.Str(attribute="value")
    offset = fields.Int(attribute="offset")
    limit = fields.Int(attribute="limit")

    @post_load
    def make_artist_filters(self, data, **kwargs):
        """Creates an ArtistFiltersData object from a dictionary."""
        return ArtistFiltersData(**data)
