from random import randint
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User


"""This is the blueprint for a tribe table in the database"""




class Tribe(models.Model):
    objects = models.Manager()
    tribeID = models.IntegerField(primary_key=True)
    tribeName = models.CharField(max_length=50)
    # How long its been a tribe
    dateOfCreation = models.DateField(default=timezone.now)
    # Location
    location = models.CharField(max_length=30)
    # Privacy
    choices = [('Public', 'Private'), ('Private', 'Public')]
    privacyMode = models.CharField(max_length=7, choices=choices, default='Private')
    # Number of members
    numOfMembers = models.IntegerField(default=1)
    # Description
    description = models.TextField(blank=True)
    # owner, tribe founder(s)
    tribeOwner = models.CharField(max_length=50)
    # list of tribe members
    tribeMembers = models.ManyToManyField(User, related_name="tribeMembers")

    def tribe_present(tribeName):
        if Tribe.objects.filter(tribeName=tribeName).exists():
            return True
        else:
            return False

    def tribe_search(tribeName):
        q = Q()
        for t in Tribe:
            q |= Q(name_icontains=t)
            return Tribe.objects.filter(q)

    def __str__(self):
        """String for representing the Model object 'tribeName'."""
        return self.tribeName



class House(models.Model):
    objects = models.Manager()
    houseName = models.CharField(default='', max_length=200)
    houseID = models.IntegerField(primary_key=True, default=randint(0,1000))
    houseInTribe = models.ManyToManyField(Tribe)
    # How long its been a tribe
    dateOfCreation = models.DateField(default=timezone.now)
    # Description
    description = models.TextField(blank=True)
    # owner, tribe founder(s)
    houseCreator = models.OneToOneField(User, on_delete=models.CASCADE, default=User.is_active)

    def __str__(self):
        """String for representing the Model object 'houseName'."""
        return self.houseName


class Posts(models.Model):
    """NEEDS IMPROVEMENT"""
    objects = models.Manager()
    title = models.CharField(default='', max_length=200)
    postID = models.IntegerField(primary_key=True, default=randint(0,1000))
    #User who posted
    tribePosterID = models.ManyToManyField(User, related_name="tribePosterID")
    #What tribe does this post belong to
    postTribeID = models.ManyToManyField(Tribe, related_name="postTribeID")
    image = models.ImageField(default='blankProfile.jpg', upload_to='profile_pics')
    description = models.TextField(blank=True)
    dateOfCreation = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class JoinRequest(models.Model):
    objects = models.Manager()
    requestingUser = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    tribeIDToJoin = models.ManyToManyField(Tribe, related_name="tribeIDToJoin")
    requestMessage = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.requestingUser.username

class Events(models.Model):
    objects = models.Manager()
    postingUser = models.ForeignKey(User, on_delete=models.CASCADE)
    tribeEvent = models.OneToOneField(Tribe, primary_key=True,on_delete=models.CASCADE, default=None)
    requestMessage = models.TextField(max_length=300, default='')
    image = models.ImageField(default='blankProfile.jpg', upload_to='profile_pics')
    description = models.TextField(blank=True)
    dateOfCreation = models.DateField(default=timezone.now)
