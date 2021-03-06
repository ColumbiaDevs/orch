from orch.roster.models import OrchestraMember
from orch.events.models import Event
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime
import random
from django.core.cache import cache
from orch.events.views import get_current_season

# Create your views here.

CACHE_TIME = 300

def home(request):
    '''get an event and member to display on the homepage. objects cached for an hour'''
   
    disp_season = False

    m = get_member()
    p = get_primary()
    s = get_secondary()

    if(p and (datetime.datetime.today() + datetime.timedelta(60)) < p.date):
        season = get_season()
        disp_season = True

    if disp_season:
        return render_to_response('home.html', {'member': m, 'season': season }, 
                              context_instance=RequestContext(request))
    else:
        return render_to_response('home.html', {'member': m, 'primary_event': p, "secondary_event": s}, 
                              context_instance=RequestContext(request))
 

def get_season():
    season = cache.get('season')

    if season:
        return season

    season = get_current_season()

    cache.set('season', season, CACHE_TIME )
    return season


def get_member():
    member = cache.get('member')

    if member:
        return member

    m = OrchestraMember.objects.exclude(photo__exact="").exclude(noncurrent_member=True).exclude(bio__exact="")
    if len(m) > 0:
        rand_index = random.randint(0, (len(m) -1 ))
        member = m[rand_index] if (len(m) > 0) else None
    
    cache.set('member', member, CACHE_TIME )

    return member

def get_primary():
    primary_event = cache.get('primary_event')
    
    if primary_event:
        return primary_event

    e = Event.objects.filter(date__gte=datetime.datetime.today()).filter(status=1).order_by('date')
    primary_event = e[0] if (len(e) > 0) else None

    cache.set('primary_event', primary_event, CACHE_TIME )
    return primary_event

def get_secondary():
    secondary_event = cache.get('secondary_event')
    
    if secondary_event:
        return secondary_event

    e = Event.objects.filter(date__gte=datetime.datetime.today()).filter(status=2).order_by('date')
    secondary_event = e[0] if (len(e) > 0 ) else None

    cache.set('secondary_event', secondary_event, CACHE_TIME )
    return secondary_event

