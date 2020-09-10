from django.util.timezone import time
from django.utils import timezone
from django.contrib.auth import models

class User(models.User):
    """Using inbuilt User Database for logins and registrations"""
    def __str__(self):
        return self.username

class Proposals(models.model):
    """Stores all the Talk proposals, can be used for reviewing proposal"""
    title = models.CharField(max_length=200,unique=True)
    abstract = models.CharField(blank=False,null=False)
    category = models.CharField(max_length=100,blank=False,null=False)
    duration = models.IntegerField(max_length=3,blank=False,null=False)
    level_of_audience = models.CharField(max_length=50,default='ALL Level')
    Speaker_bio = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Events(models.Model):
    """Event is create for all approved Proposals"""
    proposal_id =models.ForeignKey(Proposals,on_delete = models.CASCADE)
    created_on = models.DatetimeField(default=timezone.now)
    modified_on = models.DatetimeField()
    created_by = models.ForeignKey(User,on_delete = models.CASCADE)
    modified_by = models.ForeignKey(User,on_delete = models.CASCADE)

    def save(self,*args,**kwargs):
        """Update date and time on modification after creation default=created time"""
        modified_on = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.proposal_id.talk_title

class Metadata(models.Model):
    """Stores metadata information of all social platforms"""
    name = models.charField()
    unique_id = models.BooleanField(default=False)
    parent_id = models.BooleanField(default=False)
    url = models.BooleanField(default=False)
    subject_id = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Posts(models.Model):
    """Stores Post details of all published posts and content of posts"""
    event_id = models.ForeignKey(Events,on_delete=models.CASCADE)
    created_on = models.DatetimeField(default=timezone.now)
    modified_on = models.DatetimeField()
    created_by = models.ForeignKey(User,on_delete = models.CASCADE)
    modified_by = models.ForeignKey(User,on_delete = models.CASCADE)
    platform = models.ForeignKey(Metadata,on_delete = models.CASCADE)
    Platform_data = models.JsonField()
    content = models.TextField()

    def save(self,*args,**kwargs):
        """Update date and time on modification after creation default=created time"""
        modified_on = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.platform.name