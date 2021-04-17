from sqlalchemy.orm import joinedload
from sqlalchemy import join, func, outerjoin

from app.utils import *
from app.models import *


def query_venues(request, text=None, cat_id=None):
    if text:
        venues = db.session.query(Venue).filter(
            Venue.question.ilike(f"%{text}%")).all()
    else:
        venues = db.session.query(Venue).outerjoin(Show).group_by(
            Venue.id).order_by(db.desc(func.count(Show.id))).all()
    return format_selection(request, venues)
