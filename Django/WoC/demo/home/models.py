from django.db import models
from django.db.models.deletion import CASCADE
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# Create your models here.
class Event(models.Model):
    host_email = models.EmailField(max_length=254, default="")
    password = models.CharField(max_length=122)
    eventname = models.CharField(max_length=122)
    location = models.CharField(max_length=15)
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    endDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    deadDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    nop = models.IntegerField()
    dec = models.TextField()

    def __str__(self):
        return self.host_email 

class Part(models.Model):
    name = models.CharField(max_length=122, default="")
    contactnumber = models.CharField(max_length=122, default="")
    part_email = models.EmailField(max_length=254, default="")
    password = models.CharField(max_length=122)
    eventName = models.CharField(max_length=122)
    reg_type = models.CharField(max_length=20, default = "")
    number = models.CharField(max_length=122)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        account_sid = 'AC3e69d9334e9e2f47bbc48bd877af0ff7'
        auth_token = '47688951daf85278de8b7aac9ed14c04'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Hello There, You have successfully registered in the event.",
                            from_='+17655713757',
                            to='+919913715425'
                        )
        # print(args)
        return super().save(*args, **kwargs)
