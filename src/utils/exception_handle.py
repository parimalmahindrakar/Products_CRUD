from functools import wraps
from flask import current_app as app
from webargs.flaskparser import abort
from werkzeug.exceptions import UnprocessableEntity

from extensions import db


def exception_handle(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)

        except ValueError as val_err:
            app.logger.error(val_err, exc_info=True)
            db.session.rollback()
            return abort(400, message=str(val_err))

        except UnprocessableEntity as e:
            db.session.rollback()

            messages = e.data["messages"]
            if "querystring" in messages:
                msg = messages.get("querystring")
            elif "form" in messages:
                msg = messages.get("form")
            else:
                msg = messages.get("json")
            return abort(400, message=str(msg))

        except Exception as exc:
            app.logger.critical(exc)
            db.session.rollback()
            return abort(500, message=str(exc))

    return wrapper
