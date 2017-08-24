# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class dojoManager(models.Manager):
    def Creator(self, Name, City, State):
        info = { errors:[], newDojo: None }

        NAME_MIN_LENGTH = 2
        NAME_MAX_LENGTH = 255
        CITY_MIN_LENGTH = 2
        CITY_MAX_LENGTH = 255
        STATE_MIN_LENGTH = 2
        STATE_MAX_LENGTH = 2
        if len(Name) < NAME_MIN_LENGTH:
            info.errors.append("Dojo name is too short, must be atleast {0}} characters.").format(NAME_MIN_LENGTH)
        elif len(Name) > NAME_MAX_LENGTH:
            info.errors.append("Dojo name is too long, limted to {0}} characters.").format(NAME_MAX_LENGTH)
        else:
            pass

        if len(City) < CITY_MIN_LENGTH:
            info.errors.append("Dojo city is too short, must be atleast {0}} characters.").format(CITY_MIN_LENGTH)
        elif len(City) > CITY_MAX_LENGTH:
            info.errors.append("Dojo city is too long, limted to {0}} characters.").format(CITY_MAX_LENGTH)
        else:
            pass

        if len(State) < STATE_MIN_LENGTH:
            info.errors.append("Dojo state is too short, must be atleast {0}} characters.").format(STATE_MIN_LENGTH)
        elif len(State) > STATE_MAX_LENGTH:
            info.errors.append("Dojo state is too long, limted to {0}} characters.").format(STATE_MAX_LENGTH)
        else:
            pass

        if len(info.errors) == 0:
            info.newDojo = dojos.objects.create(name=Name, city=City, state=State )
        return info
    def __str__(self):
        print "< name:"+ self.name + " city:"+ self.city + " state:"+ self.state  + " >"
        for each in ninjas.objects.filter(name=self.name):
            each.__str__()
    def __repr__(self):
        print "< name:"+ self.name + " city:"+ self.city + " state:"+ self.state  + " >"
        for each in ninjas.objects.filter(name=self.name):
            each.__repr__()

class dojos(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    objects=dojoManager()

class ninjaManager(models.Manager):
    def Creator(self, DojoId, FirstName, LastName):
        info = { errors:[], newDojo: None }

        FIRSTNAME_MIN_LENGTH = 2
        FIRSTNAME_MAX_LENGTH = 255
        LASTNAME_MIN_LENGTH = 2
        LASTNAME_MAX_LENGTH = 255
        thisDojo = dojos.objects.find(id=DojoId).first()
        if None == thisDojo:
            info.errors.append("Not able to locate dojo by id '{0}'.").format(DojoId)

        if len(FirstName) < FIRSTNAME_MIN_LENGTH:
            info.errors.append("First name is too short, must be atleast {0}} characters.").format(FIRSTNAME_MIN_LENGTH)
        elif len(FirstName) > FIRSTNAME_MAX_LENGTH:
            info.errors.append("First name is too long, limted to {0}} characters.").format(FIRSTNAME_MAX_LENGTH)
        else:
            pass

        if len(LastName) < LASTNAME_MIN_LENGTH:
            info.errors.append("First name is too short, must be atleast {0}} characters.").format(LASTNAME_MIN_LENGTH)
        elif len(LastName) > LASTNAME_MAX_LENGTH:
            info.errors.append("First name is too long, limted to {0}} characters.").format(LASTNAME_MAX_LENGTH)
        else:
            pass

        if len(info.errors) == 0:
            info.newDojo = dojos.objects.create(dojo_id = thisDojo, first_name = FirstName, clast_name = LastName)
        return info
    def __str__(self):
        print "  < first_name:" + self.first_name + " last_name:"+ self.last_name + " dojo_id:"+ self.dojo_id.id  + " >"
    def __repr__(self):
        print "  < first_name:" + self.first_name + " last_name:"+ self.last_name + " dojo_id:"+ self.dojo_id.id  + " >"

class ninjas(models.Model):
    dojo_id = models.ForeignKey(dojos)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    objects=ninjaManager()
