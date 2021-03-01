from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    mtitle=models.CharField(max_length=255)
    mdate=models.DateField()
    mtime=models.CharField(max_length=255)
    mlocation=models.TextField(null=True, blank=True)
    magenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.mtitle

    class Meta:
        db_table='meeting' 

class MeetingMinutes(models.Model):
    meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.CharField(max_length=255)

    def __str__(self):
        return self.meeting
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resourcedate=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'

class Event(models.Model):
    etitle=models.CharField(max_length=255)
    elocation=models.TextField(null=True, blank=True)
    edate=models.DateField()
    etime=models.CharField(max_length=255)
    edescription=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.etitle
    
    class Meta:
        db_table='event'