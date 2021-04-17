from flask import Blueprint, jsonify, request, abort
from app.shows.utils import *

from app.models import *

users = Blueprint("users", __name__)


@users.route("/users/<user_id>/shows", methods=["GET"])
def shows_per_user(user_id):
    """handles GET requests for getting questions questions. Results are paginated in groups of 10 questions.
    @rtype: JSON object
    """
    error = False
    # try:
    # get venues created by the user
    venue = db.session.query(Venue).filter(Venue.user_id == user_id).first()
    if venue:
        venue_id = venue.format()['id']
        all_shows, num_shows = query_shows(request, venue_id)
    else:
        all_shows, num_shows = [], 0
    # except Exception as e:
    #     error = True
    # finally:
    #     db.session.close()

    # raise internal server error if error is True
    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'shows': all_shows,
        'number_shows': num_shows
    })
