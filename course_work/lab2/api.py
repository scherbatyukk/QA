from flask import Flask, request, jsonify
from directory import Directory


app = Flask(__name__)

root = Directory('root', 100)
deleted_list = []

@app.route('/directory', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def directory():
   if request.method == 'POST':
      if any(x.name == request.args.get('name') for x in root.list) or request.args.get('name') == 'root':
         return jsonify({
         "message": "Directory already exists.",
      }), 400
      dir = Directory(request.args.get('name'), request.args.get('max_elems'), root)
      return jsonify({
         "message": "Directory created successfully.",
         "directory": {
            "parent": str(dir.parent),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)     
         }
      }), 201
      
   elif request.method == 'GET':
      if any(dir.name == request.args.get('name') for dir in root.list) or request.args.get('name') == 'root':
         if request.args.get('name') == 'root':
            dir = root
         else:
            dir = next(x for x in root.list if x.name == request.args.get('name'))
         return jsonify({
         "message": "Directory was read successfully.",
         "directory": {
            "parent": str(dir.parent),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)  
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400

   elif request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.list):
         dir = next(x for x in root.list if x.name == request.args.get('name'))
         dir.move(root)
         return jsonify({
         "message": "Directory moved successfully.",
         "directory": {
            "parent": str(dir.parent.name),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)    
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400 

   else:
      if request.args.get('name') not in deleted_list and any(dir.name == request.args.get('name') for dir in root.list):
         dir = next(x for x in root.list if x.name == request.args.get('name'))
         del dir
         deleted_list.append(request.args.get('name'))
         return jsonify({
         "message": "Directory deleted successfully.",
         }), 200
      return jsonify({
         "message": "Directory was not deleted.",
         }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')