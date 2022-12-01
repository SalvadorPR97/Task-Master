from django.core.management.base import BaseCommand
from tasks.models import Task
import datetime
from tqdm import tqdm

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        hoy = datetime.datetime.today()
        hoy_pero_hace_siete_dias = hoy - datetime.timedelta(days=7)
        tareas = (
            Task.objects
            .exclude(priority='H')
            .exclude(finished=True)
            .filter(due_date__gte=hoy_pero_hace_siete_dias)
            .filter(due_date__lte=hoy_pero_hace_siete_dias)
        )
        for t in tqdm(tareas):
            t.priority = 'H'
            t.save()
            print(t)