from flask import Flask, request, abort, jsonify
import uuid

""" 
Project One
In Memory Kanban
Welcome to project 1, first you're going to be dealing with an inmemory kanban
this means there is no database stuff just yet, we're going to keep it very simple for now

What we're interested in right now is setting up a REST API which performs CRUD operations

C - Create a specific task for the kanban board, the shape of the task should be

{
id: 'give it a unique uuid using the uuid import'
progress: 'give it a progress which can be either 'todo', 'inprogress' or 'done'
message: 'give it a message which represents what job it is for example 'taking out the trash''
}

R - Read the current state of the kanban board, this is self explanatory, it should just display the current state of the kanban board

U - Update the job, this should update the currently stored job on the kanban board regardless of its position, given the id

D - Delete the job, this should delete the currently stored job on the kanban board given the id

"""
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

@app.post('/create-job')
def create_job():
    """ create the job """

    """ README: perform a CREATE of the item here"""

@app.route('/job', methods=['PUT', 'DELETE'])
def modify_job():
    if request.method == 'PUT': # handle put requests
        """ README: perform an UPDATE of the item here"""
    else: # handle delete requests
        """ README: perform a DELETE of that item here """


