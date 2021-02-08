from flask import jsonify, request
from flask_restful import Resource
from api.services.MongoManagerService import MongoManagerService as mms
class ApiBaseResource(Resource):
    def get(self):
        return jsonify({'status': 200, 'message': 'Api base resource has been hit'})

class ApiBuildingResource(Resource):
    def get(self):
        response = mms().collect_all_buildings()
        return response

class ApiRoomResource(Resource):
    def get(self, building, room):
        response = mms().collect_all_entries_by_room(building, room)
        return response

class ApiUpdateResource(Resource):
    def post(self):
        response = mms().insert_entry_by_room(request.json)
        return response