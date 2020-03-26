from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"Meeting which will have fields for meeting title," 
"meeting date, meeting time, location, Agenda"
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.CharField(max_length=255)
    location=models.TextField()
    agenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
    "define what you are going to show"

    class Meta():
        db_table='Meeting Name'
        verbose_name_plural='Meeting Names'


"Meeting Minutes which will have fields for meeting id (a foreign key),"
"attendance (a many to many field with User), Minutes text"

class MeetingMinutes(models.Model):
    minutename=models.CharField(max_length=255)
    meetingtitle=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.CharField(max_length=255)

    def __str__(self):
        return self.minutename

    class Meta():
        db_table='Minute Name'
        verbose_name_plural='Minute Names'

"Resource which will have fields for resource name, resource type, URL,"
"date entered, user id (foreign key with User), and description"

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.resourcename
    
    class Meta():
        db_table='Resource'
        verbose_name_plural='Resources'
    
"Event which will have fields for event title, location, date, time, "
"description and the user id of the member that posted it"

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.CharField(max_length=255)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.eventtitle
    
    class Meta():
        db_table='Event'
        verbose_name_plural='Events'