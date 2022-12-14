import inspect
from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class AlbumData:
    """Album dataclass."""

    name: str
    id: int = None
    artist_id: int = None

    @classmethod
    def from_dict(cls, env):
        """Creates a AlbumData object from a dictionary."""
        return cls(**{k: v for k, v in env.items() if k in inspect.signature(cls).parameters})


@dataclass
class AlbumFiltersData:
    """Album filters dataclass."""

    field: Literal["id", "artist_id", "name"] = None
    operator: Literal[
        "equals",
        "not_equals",
        "greater_than",
        "less_than",
        "less_equals_than",
        "greater_equals_than",
        "like",
        "ilike",
        "not_ilike",
        "in",
        "not_in",
    ] = None
    value: Union[str, int] = None
    offset: int = 0
    limit: int = 50
