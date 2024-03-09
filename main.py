from flask import Flask, request, abort, jsonify
import uuid

app = Flask(__name__)

kanban = {
    "todo" : [],
    "inprogress" :[],
    "done" :[]
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/kanban", methods=['GET'])
def view_kanban():
    """ return the kanban board """
    if request.method == 'GET':
        return kanban

@app.post('/create-job')
def create_job():
    """ create the job """
    data = request.get_json()
    """ probably perform some validation here """
    # we want the message and which stage of progress it is
    message = data["message"]
    if "progress" in data:
        progress = data["progress"]
        new_job = {
        "id": uuid.uuid1(),
        "progress" : progress,
        "message" : message
        }
        kanban[progress].append(new_job)
        return jsonify(kanban)
    else:
        abort(403, description="no progress given for job")

@app.route('/job', methods=['PUT', 'DELETE'])
def modify_job():
    if request.method == 'PUT': # handle get requests
        data = request.get_json()
        print("data: ", data)
        id = data["id"]
        progress = data["progress"]
        # if its the same, then do not do anything
        # remove any previous job in another category

        # if progress not in keys then return error

        if progress not in kanban:
            abort(403, description="Invalid progress value")

        for key in kanban:
            category = kanban[key]
            print(kanban)
            for item in category:
                print("item: ", item, " did it ever complete")
                print("convered to string: ", str(item["id"]))
                # match by id
                if str(item["id"]) == id:
                    category.remove(item)
                    # there will only be one of this so we can perform an early exit
                    kanban[progress].append(data)
                    return jsonify(kanban)
        # if we didn't find it then return error
        abort(404, description="job not found!")
    else: # handle delete
        data = request.get_json()
        print("data: ", data)
        id = data["id"]
        progress = data["progress"]
        category = kanban[progress]
        for item in category:
            if str(item["id"]) == id:
                # remove the item
                category.remove(item)
                # return
                return jsonify(kanban)
        abort(404, description="job not be found!")
        


