import random

from flask import Blueprint, jsonify, request, abort
from .utils import *

from app.models import *

venues = Blueprint("venues", __name__)

# # enable CORS for questions
# cors = CORS(venues, resources={r"/question/*": {"origins": "*"}})


# # CORS Headers
# @venues.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
#     return response


@venues.route("/venues", methods=["GET"])
def get_questions():
    """handles GET requests for getting questions questions. Results are paginated in groups of 10 questions.
    @rtype: JSON object
    """
    error = False
    try:
        venues, num_venues = query_venues(request)
    except Exception as e:
        error = True
    finally:
        db.session.close()

    # raise internal server error if error is True
    abort_error_if_any(error, 500)
    return jsonify({
        'success': True,
        'venues': venues,
        'number_venues': num_venues
    })


@venues.route("/venues", methods=["POST"])
def create_question():
    """ handles creating new venues with a post request.
    @rtype: JSON object
    """
    data = get_request_data_or_400(request)
    venue_ins = Venue()
    attrs = dir(venue_ins)
    # set attrs values of new_question instance from given request data
    new_venue = set_attributes_all_required(venue_ins, attrs, data)

    error = False
    venue_details = {}
    try:
        new_venue.insert()
        venue = db.session.query(Venue).get(new_venue.id).all()
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    # raise exception (Unprocessable Request), if error is True
    abort_error_if_any(error, 422)
    return jsonify({
        'success': True,
        'venues': venue
    })