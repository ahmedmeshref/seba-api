from flask import abort
from sqlalchemy.orm import joinedload
from sqlalchemy import join, func, outerjoin
from time import time

from app.models import *


def get_item_or_404(db_table, id):
    return db.session.query(db_table).get_or_404(id)


def get_request_data_or_400(request):
    data = request.get_json()
    if not data:
        # If request body is empty, raise 400 (Bad Request) error.
        abort(400)
    return data


def abort_error_if_any(error, error_code=500):
    """
    @type error: bool
    @param error
    @type error_code: int
    @param error_code: code for specifying the error to be raised
    @return: raise error_code if error is True, otherwise None
    """
    if error:
        abort(error_code)


PAG_PER_PAGE = 10


def pagination(request, selection):
    page = request.args.get("page", 1, type=int)
    if page > (len(selection) / PAG_PER_PAGE) + 1:
        # if Requested page is greater than total pages in db, then start from first element
        start = 0
    else:
        start = (page - 1) * PAG_PER_PAGE
    end = start + PAG_PER_PAGE
    formatted_data = [record.format() for record in selection[start:end]]
    return formatted_data


def format_selection(request, selection):
    formatted_questions = pagination(request, selection)
    return [formatted_questions, len(selection)]


def set_attributes_all_required(instance, attrs, res):
    """strictly sets all given attributes on a given instance from a given dictionary. If any attribute value is
        missing, raise exception (Bad Request).
    @type instance: object
    @param instance: A class instance
    @type attrs: list
    @param attrs: A list of attributes
    @type res: dict
    @param attrs: dict {"attribute": value}
    @rtype: object
    @returns: a list of strings representing the header columns
    """
    for attr in attrs:
        attr_val = res.get(attr)
        # all attributes are required
        if not attr_val:
            print(attr)
            abort(400)
        setattr(instance, attr, attr_val)
    return instance
