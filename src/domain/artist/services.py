import logging

from domain.artist.schemas import ArtistSchema
from domain.artist.repositories import ArtistRepository
from domain.artist.data import ArtistData, ArtistFilters

logger = logging.getLogger("AZ_LYRICS")

class ArtistService:

    def __init__(self, artist_repository: ArtistRepository):
        self.artist_repository = artist_repository

    def create_multiple_artists(self, artists: list):
        """Creates a new artist register.

        Args:
            artists: ArtistSchema object.

        Returns:
            ArtistSchema object.
        """
        logging.info("Creating multiple artists.")
        new_artists = self.artist_repository.create_multiple_artists(artists=artists)

        return new_artists

    def get_artists(self) -> ArtistData:
        """Retrieves multiple artists registers.

        Returns:
            artists: List of ArtistData objects.
        """
        logging.info("Retrieving all artists.")
        artists = self.artist_repository.get_artists()

        return artists

    def get_artist_by_id(self, artist_id: int) -> ArtistData:
        """Retrieves an artist by its id.

        Args:
            artist_id: artist's unique identifier.

        Returns:
            ArtistData object.
        """
        logging.info(f"Retrieving artist by id: {artist_id}")
        artist = self.artist_repository.get_artist_by_id(artist_id=artist_id)

        if not artist:
            raise Exception(f"Artist id: {artist_id} not found.")

        return artist

    def get_artists_filtered(self, filters: list) -> [ArtistData, int]:
        """Retrieves artists filtered by params.

        Args:
            filters: list with filters and orders.

        Returns:
            artists: List of ArtistData objects
            count: total number of registers.
        """
        try:
            logging.info(f"Retrieving artists filtered by: {filters}")

            artists, count = self.artist_repository.get_artists_filtered(
                filters=filters
            )

            return artists, count

        except Exception:
            raise Exception("Something happened while retrieving artists filtered.")
