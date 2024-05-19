from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NoteForm
from django.forms import Form
from .models import Note
import time

# Create your views here.

def index(request):
    notes = Note.objects.all().order_by('-date_created') # Retrive the available Notes    
    if request.method == 'POST':
        # Create a new form object
        form = NoteForm(request.POST) # bounding the request date
        note = Note() # the new Note
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            note.title = title
            note.description = description
            note.save()
        else:
            return HttpResponseRedirect('error')
        return HttpResponseRedirect('/')
    else:
        form = NoteForm()
    return render(request, 'notes/index.html', {'form':form, 'notes':notes})

def error(request):
    error = "For you to see this page, it means Logic Error!"
    return render(request, 'notes/error.html', {'error': error})

def update(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(request.POST or None, instance=note) # Create a form with the submitted data
    if request.method == 'POST':
        if form.is_valid():
            note.title = request.POST['title']
            note.description = request.POST['description']
            note.save()
            
        return HttpResponseRedirect('/')
    return render(request, 'notes/update.html', {'form':form, 'note':note})

# Delete mechanism
def delete(request, id):
    note = Note.objects.get(id=id)
    note_uper = note.title.upper()
    # Script to delete the note with this id
    if request.method == 'POST':
        note.delete()
        return HttpResponseRedirect('/')
    return render(request, 'notes/delete.html', {'note':note, 'note_uper':note_uper})

def about(request):
    return render(request, 'notes/about.html')