from flask_restful import Resource
from flask import request, jsonify
from flask_login import login_required
from additionalFunc import requires_roles

class LoginCheked(Resource):

    @login_required
    @requires_roles("SUPERUSER", "USER")
    def get(self):
        return "True", 200