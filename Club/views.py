from django.shortcuts import render, get_object_or_404
from . models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list' : meeting_list})

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list' : resource_list})

def meetdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    agenda=meet.magenda
    title=meet.mtitle
    date=meet.mdate
    location=meet.mlocation
    time=meet.mtime
    context={
        'meet' : meet,
        'agenda' : agenda,
        'title' : title,
        'date' : date,
        'location' : location,
        'time' : time,
    } 
    return render(request, 'Club/meetdetails.html', context=context)
