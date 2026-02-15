from django.core.management.base import BaseCommand
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        User.objects.bulk_create([
            User(name="Iron Man", email="ironman@marvel.com", team="Marvel"),
            User(name="Captain America", email="cap@marvel.com", team="Marvel"),
            User(name="Batman", email="batman@dc.com", team="DC"),
            User(name="Wonder Woman", email="wonderwoman@dc.com", team="DC")
        ])

        Team.objects.bulk_create([
            Team(name="Marvel", members=["Iron Man", "Captain America"]),
            Team(name="DC", members=["Batman", "Wonder Woman"])
        ])

        Activity.objects.bulk_create([
            Activity(user="Iron Man", activity="Running", duration=30),
            Activity(user="Batman", activity="Cycling", duration=45)
        ])

        Leaderboard.objects.bulk_create([
            Leaderboard(team="Marvel", points=100),
            Leaderboard(team="DC", points=90)
        ])

        Workout.objects.bulk_create([
            Workout(user="Wonder Woman", workout="Yoga", duration=60),
            Workout(user="Captain America", workout="Weightlifting", duration=40)
        ])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
