from django.shortcuts import render, get_object_or_404 #render templates and retrieve objects from the database(404 = not found)
from .models import Snippet #allows views to interact with the Snippet database table
#POST = method used for sending data from client to server

def home(request):
    if request.method == 'POST':
        new_code = request.POST.get('typedText') #.get method returns 'None' if the specified key doesn't exist, avoiding a KeyError
        new_snippet = Snippet(code=new_code) #instance created with the submitted code (This line effectively prepares a new database record with the submitted code snippet but doesn't save it to the database yet.)
        new_snippet.save() # and saved to the database (When .save() is called, Django executes an INSERT SQL statement behind the scenes)
    return render(request, 'home.html')

def history(request):
    snippets = Snippet.objects.all() # retrieves all Snippet instances from the database
    return render(request, 'history.html', {'snippets': snippets})

def texts(request, pk): # displays details of a single Snippet instance, identified by its primary key
    snippet = get_object_or_404(Snippet, pk=pk) # fetch the snippet with the given pk from the database
    return render(request, 'texts.html', {'snippet': snippet}) 
