"""
Django command t wait for the datbase to be available 

"""
import time
from django.core.management.base import BaseCommand

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error

class Command(BaseCommand):
    """  Django command to wiat for database"""
    ## we have to build the testcase which we have then 
    ## makes this function passes it
    def handle(self, *args, **options):
        print("wait for database")
        self.stdout.write('waiting for database...')
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
