from django.shortcuts import render
from django.http import HttpResponse

from .forms import (
    UserForm,
    SpeakerForm
)


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            return HttpResponse(
                f'{form.cleaned_data}'
                'User Added successfully'
            )

    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def add_speaker(request):
    if request.method == "POST":
        form = SpeakerForm(request.POST)

        if form.is_valid():
            return HttpResponse(
                f'{form.cleaned_data}'
                'Speaker Added successfully'
            )

    else:
        form = SpeakerForm()

    return render(request, 'add_speaker.html', {'form': form})
