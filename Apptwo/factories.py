from factory.django import DjangoModelFactory
from django_faker import Faker

from . models import Topic,WebPage,AccessRecord

class TopicFactory(DjangoModelFactory):
    class Meta:
        model=Topic

    topic_name=Faker("text")

u=TopicFactory()
print(u.topic_name)
