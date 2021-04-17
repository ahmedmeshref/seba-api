from sqlalchemy.orm import joinedload
from sqlalchemy import join, func, outerjoin

from app.utils import *
from app.models import *


def query_shows(request, venue_id=None):
    if venue_id:
        shows = db.session.query(Show).join(Venue, Venue.id == Show.venue_id).filter(
            Venue.id == venue_id).all()
    else:
        shows = db.session.query(Show).all()
    return format_selection(request, shows)
