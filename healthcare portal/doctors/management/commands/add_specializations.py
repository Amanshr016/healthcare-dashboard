from django.core.management.base import BaseCommand
from doctors.models import Specialization

class Command(BaseCommand):
    help = 'Add default medical specializations'

    def handle(self, *args, **kwargs):
        specializations = [
            {'name': 'Cardiology', 'description': 'Heart and cardiovascular system specialists'},
            {'name': 'Neurologist', 'description': 'Brain and nervous system specialists'},
        ]
        
        for spec in specializations:
            obj, created = Specialization.objects.get_or_create(
                name=spec['name'],
                defaults={'description': spec['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added specialization: {spec["name"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Specialization already exists: {spec["name"]}'))
        
        self.stdout.write(self.style.SUCCESS('\nSuccessfully updated specializations!'))
