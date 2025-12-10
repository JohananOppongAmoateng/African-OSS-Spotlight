from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
import random

from creators.models import Creator
from projects.models import Project


class Command(BaseCommand):
    help = 'Populate database with dummy creators and projects'

    def add_arguments(self, parser):
        parser.add_argument('--creators', type=int, default=200, help='Number of creators to create')
        parser.add_argument('--projects', type=int, default=1200, help='Number of projects to create')
        parser.add_argument('--clear', action='store_true', help='Delete existing creators and projects first')

    def handle(self, *args, **options):
        faker = Faker()
        num_creators = options['creators']
        num_projects = options['projects']
        clear = options['clear']

        if clear:
            self.stdout.write('Clearing existing projects and creators...')
            Project.objects.all().delete()
            Creator.objects.all().delete()

        self.stdout.write(f'Creating {num_creators} creators...')
        creators = []
        for _ in range(num_creators):
            name = faker.name()
            job_title = faker.job()
            bio = faker.paragraph(nb_sentences=3)
            website_url = faker.url()
            tech_stack = ', '.join(faker.words(nb=4))
            country = faker.country() or "Ghana"
            skills_and_interests = faker.sentence(nb_words=8)
            followers_count = random.randint(0, 20000)
            is_verified = random.random() < 0.1
            social_links = {
                'github': f'https://github.com/{faker.user_name()}',
                'twitter': f'https://twitter.com/{faker.user_name()}',
                'linkedin': f'https://www.linkedin.com/in/{faker.user_name()}'
            }

            creators.append(Creator(
                name=name,
                job_title=job_title,
                bio=bio,
                website_url=website_url,
                tech_stack=tech_stack,
                country=country,
                skills_and_interests=skills_and_interests,
                followers_count=followers_count,
                is_verified=is_verified,
                social_links=social_links
            ))

        with transaction.atomic():
            Creator.objects.bulk_create(creators)

        created_creators = list(Creator.objects.all())

        self.stdout.write(f'Creating {num_projects} projects...')
        projects = []
        for _ in range(num_projects):
            name = faker.sentence(nb_words=3).rstrip('.')
            about = faker.sentence(nb_words=6)
            description = faker.paragraph(nb_sentences=4)
            repository_url = f'https://github.com/{faker.user_name()}/{faker.word()}'
            tech_stack = ', '.join(faker.words(nb=5))
            live_demo_url = faker.url() if random.random() < 0.3 else None
            creator = random.choice(created_creators)
            is_verified = random.random() < 0.05

            projects.append(Project(
                name=name,
                about=about,
                description=description,
                repository_url=repository_url,
                tech_stack=tech_stack,
                live_demo_url=live_demo_url,
                creator=creator,
                is_verified=is_verified
            ))

        with transaction.atomic():
            Project.objects.bulk_create(projects)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_creators} creators and {num_projects} projects'))
