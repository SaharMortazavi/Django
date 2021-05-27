import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project_two.settings')
import django
django.setup()

# fake pop script
import random
from Apptwo.models import AccessRecord,WebPage,Topic
from faker import Faker

faker_data=Faker()
topics=['Search','Social','MarketPlace','News','Games']
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    #get the topic for the entry 
    for entry in range(N):
        top=add_topic()
        #create the fake data for that entry
        fake_url=faker_data.url()
        fake_date=faker_data.date()
        fake_name=faker_data.company()

        webpg=WebPage.objects.get_or_create(topic=top, url=fake_url,name=fake_name)[0]
        #create fake access record for webpage
        acc_rec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ =="__main__":
    print("populating scrip!")
    populate(20)
    print("populating complete!")


