"""Views for play page."""
from django.shortcuts import render
from healers.models import Event, AddEvent, DeleteEvent
from django.http import HttpResponseRedirect


def play_view(request):
    """Populate evnets on play page."""
    # TODO: Order by event date ending soonest to ending latest.
    events = Event.objects.all()
    return render(request, 'play.html', {'events': events})


def add_event(request):
    """View to add an event to database through UI."""
    form = AddEvent(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/healers/play/')
    return render(request, 'add_event.html', context={'form': form})


def edit_event(request, pk):
    """Edit an event."""
    if request.method == 'POST':
        event = Event.objects.get(id=pk)
        form = AddEvent(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/healers/play/')
        return render(request, 'edit_event.html', context={'form': form})
    else:
        event = Event.objects.get(id=pk)
        form = AddEvent(instance=event)
        return render(request, 'edit_event.html', context={'form': form})


def delete_event(request, pk):
    """Delete an event."""
    if request.method == 'POST':
        event = Event.objects.get(id=pk)
        form = DeleteEvent(request.POST, instance=event)
        if form.is_valid():
            event.delete()
            return HttpResponseRedirect('/healers/play/')
        return render(request, 'delete_event.html', context={'form': form})
    else:
        event = Event.objects.get(id=pk)
        form = DeleteEvent(request.POST, instance=event)
        return render(request, 'delete_event.html', context={'form': form})
