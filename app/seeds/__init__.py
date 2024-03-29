from flask.cli import AppGroup
from .users import seed_users, undo_users
from .projects import seed_projects, undo_projects
from .issue_types import seed_issue_types, undo_issue_types
from .statuses import seed_statuses, undo_statuses
from .issues import seed_issues, undo_issues
from .status_changes import seed_status_changes, undo_status_changes


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_projects()
    seed_issue_types()
    seed_statuses()
    seed_issues()
    seed_status_changes()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_status_changes()
    undo_issues()
    undo_statuses()
    undo_issue_types()
    undo_projects()
    undo_users()
    # Add other undo functions here
