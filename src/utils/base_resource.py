from flask_restful import Resource

from src.utils.exception_handle import exception_handle


class BaseResource(Resource):
    base_decorators = [exception_handle]
