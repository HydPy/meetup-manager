from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages
from django.db.utils import IntegrityError

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
            try:
                form.save()
            except IntegrityError as error:
                messages.debug(request, f'Failed to add user due to error: {error}')

            messages.info(request, 'User added successfully')
            return HttpResponseRedirect(f'/user/{form.cleaned_data.get("username")}')

    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseBadRequest('No user exists with the given username')

    return render(request, 'get_user.html', {'user': user})


def add_speaker(request):
    if request.method == "POST":
        form = SpeakerForm(request.POST)

        if form.is_valid():
            try:
                form.save()
            except IntegrityError as error:
                messages.debug(request, f'Failed to add speaker due to error: {error}')

            messages.info(request, 'Speaker added successfully')
            return HttpResponseRedirect(f'/speaker/{form.cleaned_data.get("username")}')

    else:
        form = SpeakerForm()

    return render(request, 'add_speaker.html', {'form': form})


def get_speaker(request, username):
    try:
        speaker = Speaker.objects.get(username=username)
    except Speaker.DoesNotExist:
        return HttpResponseBadRequest('No speaker exists with the given username')

    return render(request, 'get_speaker.html', {'speaker': speaker})
