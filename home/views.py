from django.core.checks import messages
from django.http import HttpResponse

from .models import Event
from . import urls
from django.shortcuts import redirect, render

def index(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'index.html',context)


def addEvent(request):
    if request.method == "POST":
        event = Event()
        event.email = request.POST.get('email')
        event.password = request.POST.get('password')
        event.event_name = request.POST.get('event_name')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time')
        event.location = request.POST.get('location')
        event.image = request.POST.get('image')

        event.save()
        # messages.success(request, "Event Added Successfully!")
        return redirect('/')
    return render(request, 'add_event.html')