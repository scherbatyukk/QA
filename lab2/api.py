from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class BinaryApi(Resource):
    def get(self):
        return {'hello': 'world'}

class BufferApi(Resource):
    def get(self):
        return {'hello': 'world'}

class DirectoryApi(Resource):
    def get(self):
        return {'hello': 'world'}

class LogTextApi(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(BinaryApi, '/binaryfile')
api.add_resource(BufferApi, '/buferfile')
api.add_resource(DirectoryApi, '/directory')
api.add_resource(LogTextApi, '/logtextfile')

if __name__ == '__main__':
    app.run(debug = True)