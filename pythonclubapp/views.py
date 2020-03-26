from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getresources(request):
    type_list=Resource.objects.all()
    return render(request, 'pythonclubapp/types.html', {'type_list':type_list})

"Add a view that returns all the meetings:"
def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonclubapp/meeting.html', {'meeting_list': meeting_list})

"Make a view that takes an int id as an parameter and retrieves "
"the meeting that has that id"

def meetingdetail(request, id):
    md=get_object_or_404(MeetingMinutes, pk=id)
    context={
        'md' : md,
    }
    return render(request, 'pythonclubapp/meetingid.html', context=context)

@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='GET':
        form=MeetingForm(request.GET)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
        else:
            form=MeetingForm()
        return render(request, 'pythonclubapp/newmeeting.html', {'form' : form})

def loginmessage(request):
    return render(request, 'pythonclubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'pythonclubapp/logoutmessage.html')