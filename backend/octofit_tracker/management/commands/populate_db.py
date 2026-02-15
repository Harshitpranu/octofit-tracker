from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = "Populate octofit_db with test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating octofit_db with test data...")

        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create users
        user1 = User.objects.create(name="Iron Man", email="ironman@marvel.com", team="Marvel")
        user2 = User.objects.create(name="Captain America", email="cap@marvel.com", team="Marvel")
        user3 = User.objects.create(name="Batman", email="batman@dc.com", team="DC")
        user4 = User.objects.create(name="Wonder Woman", email="wonderwoman@dc.com", team="DC")

        # Create teams
        team1 = Team.objects.create(name="Marvel", members=[user1.name, user2.name])
        team2 = Team.objects.create(name="DC", members=[user3.name, user4.name])

        # Create activities
        Activity.objects.create(user=user1.name, activity="Running", duration=30)
        Activity.objects.create(user=user3.name, activity="Cycling", duration=45)

        # Create workouts
        Workout.objects.create(user=user4.name, workout="Yoga", duration=60)
        Workout.objects.create(user=user2.name, workout="Weightlifting", duration=40)

        # Create leaderboard
        Leaderboard.objects.create(team="Marvel", points=100)
        Leaderboard.objects.create(team="DC", points=90)

        self.stdout.write(self.style.SUCCESS("octofit_db populated successfully!"))
