import logging
from datetime import datetime

from flask import Flask, jsonify
from sqlalchemy import MetaData

from database.session import engine
from domain.album.routes import album_blueprint
from domain.artist.routes import artist_blueprint
from domain.song.routes import song_blueprint
from settings import settings

logger = logging.getLogger("AZ_LYRICS")

def init_db():
    from domain.album.models import Album
    from domain.artist.models import Artist
    from domain.song.models import Song

    meta = MetaData()

    try:
        logger.info("Creating tables again")
        meta.create_all(engine)

    except Exception:
        logger.exception("Couldn't create db tables.")

    logger.info("Db tables created successfully.")


init_db()
app = Flask(__name__)


app.register_blueprint(blueprint=artist_blueprint, url_prefix="/artist")
app.register_blueprint(blueprint=album_blueprint, url_prefix="/album")
app.register_blueprint(blueprint=song_blueprint, url_prefix="/song")


@app.route("/")
def health():
    """Health check endpoint."""
    logger.info(f"Health check endpoint called on: {datetime.now()}.")
    return jsonify({"status": "ok", "timestamp": datetime.now()})




if __name__ == "__main__":

    app.run(host=settings.host, port=settings.port, debug=settings.debug)
