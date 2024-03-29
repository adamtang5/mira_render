from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Issue, User, db
from app.forms import EditUserForm
from .validation import validation_errors_to_error_messages

user_routes = Blueprint('users', __name__)


# GET /api/users/
@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# GET /api/users/:id
@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict_full_details()


# PUT /api/users/:id
@user_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_user(id):
    form = EditUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User.query.get(id)
        user.display_name = form.data['display_name'] or user.display_name
        user.avatar_url = form.data['avatar_url'] or user.avatar_url
        db.session.commit()
        return user.to_dict()
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


##############


# GET /api/users/:id/projects/
@user_routes.route('/<int:id>/projects/')
@login_required
def get_all_projects_by_user(id):
    user = User.query.get(id)
    return jsonify([project.to_dict() for project in user.projects])


# GET /api/users/:id/assigned_issues/
@user_routes.route('/<int:id>/assigned_issues/')
@login_required
def get_assigned_issues_by_user(id):
    user = User.query.get(id)
    return jsonify([issue.to_dict() for issue in user.assigned_issues])


# GET /api/users/:id/submitted_issues/
@user_routes.route('/<int:id>/submitted_issues/')
@login_required
def get_submitted_issues_by_user(id):
    user = User.query.get(id)
    return jsonify([issue.to_dict() for issue in user.submitted_issues])
