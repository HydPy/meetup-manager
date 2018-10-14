from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import (
    UserForm,
    SpeakerForm
)

from .models import (
    User,
    Speaker
)


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'User added successfully')
            return HttpResponseRedirect('/')

    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def get_user(request, username):
    return render(request, 'get_user.html', {'user': User.objects.get(username=username)})


def add_speaker(request):
    if request.method == "POST":
        form = SpeakerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Speaker added successfully')
            return HttpResponseRedirect('')

    else:
        form = SpeakerForm()

    return render(request, 'add_speaker.html', {'form': form})


def get_speaker(request, username):
    return render(request, 'get_speaker.html', {'speaker': Speaker.objects.get(username=username)})
