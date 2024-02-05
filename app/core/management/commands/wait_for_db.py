"""
Django command to wait DB available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for DB"""
    #  funtion to Handle database  connection errors and retry after a short delay avoiding  server unresponsive errors on startup

    def handle(self, *args, **options):
        """Entrypoint for commands. Wait until the database is up and running."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                # it checks if the connection is available
                self.check(databases=['default'])
                db_up = True
                # this will rise an exception  if something goes wrong with the connection
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR(
                    'Database unavailable, waiting 1 second...'))
                # wait for 1 second before trying again
                time.sleep(1)
        # if the  loop ends normally, it means that everything went fine and we can close the app
        self.stdout.write(self.style.SUCCESS(
            'Database available. Proceeding with startup.'))
