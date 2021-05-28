import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_three.settings')
import django
django.setup()

import random
from faker import Faker
from users.models import UserProfile

fake_data=Faker()

def populate(N=5):
    for entry in range(N):
        fake_first_name=fake_data.first_name()
        fake_last_name=fake_data.last_name()
        fake_email=fake_data.free_email()
        fname=UserProfile.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
      

if __name__=="__main__":
    print("populating scrip!")
    populate(10)
    print("populating complete!")



