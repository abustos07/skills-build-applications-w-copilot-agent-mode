from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Users
        ironman = User.objects.create(username='ironman', email='ironman@marvel.com', first_name='Tony', last_name='Stark', team='Marvel')
        cap = User.objects.create(username='cap', email='cap@marvel.com', first_name='Steve', last_name='Rogers', team='Marvel')
        thor = User.objects.create(username='thor', email='thor@marvel.com', first_name='Thor', last_name='Odinson', team='Marvel')
        hulk = User.objects.create(username='hulk', email='hulk@marvel.com', first_name='Bruce', last_name='Banner', team='Marvel')
        superman = User.objects.create(username='superman', email='superman@dc.com', first_name='Clark', last_name='Kent', team='DC')
        batman = User.objects.create(username='batman', email='batman@dc.com', first_name='Bruce', last_name='Wayne', team='DC')
        wonderwoman = User.objects.create(username='wonderwoman', email='wonderwoman@dc.com', first_name='Diana', last_name='Prince', team='DC')
        flash = User.objects.create(username='flash', email='flash@dc.com', first_name='Barry', last_name='Allen', team='DC')

        # Activities
        Activity.objects.create(user='ironman', type='run', duration=30, calories=300, date='2025-11-01')
        Activity.objects.create(user='cap', type='cycle', duration=45, calories=400, date='2025-11-02')
        Activity.objects.create(user='thor', type='swim', duration=60, calories=500, date='2025-11-03')
        Activity.objects.create(user='hulk', type='lift', duration=90, calories=600, date='2025-11-04')
        Activity.objects.create(user='superman', type='fly', duration=120, calories=700, date='2025-11-05')
        Activity.objects.create(user='batman', type='run', duration=40, calories=350, date='2025-11-06')
        Activity.objects.create(user='wonderwoman', type='cycle', duration=50, calories=420, date='2025-11-07')
        Activity.objects.create(user='flash', type='run', duration=20, calories=250, date='2025-11-08')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=1800, rank=1)
        Leaderboard.objects.create(team='DC', points=1720, rank=2)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy', duration=10)
        Workout.objects.create(name='Sprints', description='Run 5 sprints', difficulty='Medium', duration=20)
        Workout.objects.create(name='Deadlift', description='Lift heavy weights', difficulty='Hard', duration=30)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
