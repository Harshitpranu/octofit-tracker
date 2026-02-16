from django.core.management.base import BaseCommand
from djongo import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        users = db['users']
        teams = db['teams']
        activities = db['activities']
        leaderboard = db['leaderboard']
        workouts = db['workouts']

        # Clear collections
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Insert sample users
        users.insert_many([
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"}
        ])

        # Insert sample teams
        teams.insert_many([
            {"name": "Marvel", "members": ["Iron Man", "Captain America"]},
            {"name": "DC", "members": ["Batman", "Wonder Woman"]}
        ])

        # Insert sample activities
        activities.insert_many([
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Batman", "activity": "Cycling", "duration": 45}
        ])

        # Insert sample leaderboard
        leaderboard.insert_many([
            {"team": "Marvel", "points": 100},
            {"team": "DC", "points": 90}
        ])

        # Insert sample workouts
        workouts.insert_many([
            {"user": "Wonder Woman", "workout": "Yoga", "duration": 60},
            {"user": "Captain America", "workout": "Weightlifting", "duration": 40}
        ])

        # Create unique index on email for users
        users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
