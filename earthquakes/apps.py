from django.apps import AppConfig
from django.core.management import call_command
import threading

class EarthquakesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'earthquakes'

    def ready(self):
        # Start the background daemon thread
        daemon_thread = threading.Thread(target=self.start_daemon)
        daemon_thread.daemon = True 
        daemon_thread.start()

    def start_daemon(self, *args, **kwargs):
        call_command('daemon')