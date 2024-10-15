from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/')
def index():
    return render_template('index.html')

@task_blueprint.route('/tasks/update', methods=['POST'])
def update_task():
    data = request.form
    task_id = data.get('id')
    name = data.get('name')
    description = data.get('description')

    if not task_id or not name:
        return jsonify({'error': 'ID and Name are required'}), 400

    updated_task = TaskService.update_task(task_id, name, description)

    if updated_task:
        return redirect(url_for('tasks.index'))
    else:
        return jsonify({'error': 'Task not found'}), 404