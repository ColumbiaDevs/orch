from haystack.indexes import *
from haystack import site
from orch.events.models import Location, Event

class LocationIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name')
    city = CharField(model_attr='city')
    
site.register(Location, LocationIndex)

class EventIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name')
    date = DateTimeField(model_attr='date')
    description = CharField(model_attr='description')
    
site.register(Event, EventIndex)


