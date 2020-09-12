from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Event(models.Model):
    event_id = models.PositiveBigIntegerField(unique=True)
    name = models.CharField(max_length=500, null=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='event_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='event_modified_by')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def save(self):
        if self.created_at is None or self.modified_at is None:
            raise ValidationError('Created by / modified by is not set')


class Talk(models.Model):
    talk_id = models.PositiveBigIntegerField(unique=True)
    content = models.JSONField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.content__title


class PlatformMetadata(models.Model):
    name = models.CharField(max_length=50)
    unique_id = models.BooleanField(default=False)
    parent_id = models.BooleanField(default=False)
    url = models.BooleanField(default=False)
    subject = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(PlatformMetadata, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='post_modified_by')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    data = models.JSONField()

    def __str__(self):
        return f"Post created for Event: [{event_id}] on platform: [{platform_id}]"
