import random

from flask import Blueprint, jsonify, request, abort
from .utils import *

from app.models import *

shows = Blueprint("shows", __name__)


@shows.route("/shows", methods=["GET"])
def get_shows():
    """handles GET requests for getting questions questions. Results are paginated in groups of 10 questions.
    @rtype: JSON object
    """
    error = False
    # try:
    all_shows, num_shows = query_shows(request)
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


@shows.route("/shows", methods=["POST"])
def create_show():
    """ handles creating new shows with a post request.
    @rtype: JSON object
    """
    data = get_request_data_or_400(request)
    show_ins = Show()
    attrs = dir(show_ins)
    # set attrs values of new_question instance from given request data
    new_show = set_attributes_all_required(show_ins, attrs, data)

    error = False
    try:
        new_show.insert()
        show = new_show.format()
    except Exception as e:
        error = True
        db.session.rollback()
    finally:
        db.session.close()

    # raise exception (Unprocessable Request), if error is True
    abort_error_if_any(error, 422)
    return jsonify({
        'success': True,
        'show': show
    })


