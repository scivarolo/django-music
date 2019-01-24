from django_seed import Seed
from history.models import Artist, Song, Album
import random

class SeedHistory():

    def execute(self):
        seeder = Seed.seeder()

        # seeder.add_entity(Artist, 5)
        # seeder.add_entity(Album, 10)
        # seeder.add_entity(Song, 50)

        seeder.add_entity(Artist, 20, {
            'name': lambda x: ' '.join(seeder.faker.words(nb=random.randint(1,4))),
            'num_of_members': lambda x: random.randint(1,5)
            })

        seeder.add_entity(Album, 60, {
            'title': lambda x: ' '.join(seeder.faker.words(nb=random.randint(1,6))),
            'release_year': lambda x: random.randint(1990, 2019)})

        seeder.add_entity(Song, 500, {
            'title': lambda x: ' '.join(seeder.faker.words(nb=random.randint(1,7)))
            })

        seeder.execute()