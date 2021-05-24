from django.shortcuts import render
from django.http import HttpResponse
from pipeline.models import RegisteredUsersForms, RegisteredUsers


def index(request):
    '''Index page to register user'''
    if request.method == 'POST':
        form = RegisteredUsersForms(request.POST)
        if form.is_valid():
            form.save()
    register_form = RegisteredUsersForms()
    context = {'form' : register_form}
    return render(request, 'pipeline/index.html', context)

def list(request):
    '''fetch all the query from the database and show it on the page.'''
    query = RegisteredUsers.objects.all()
    context = {'query' : query}
    return render(request, 'pipeline/show.html', context)

def person(request):
	query = RegisteredUsers.objects.filter(username = request.GET['person'])
	context = {'query' : query}
	return render(request, 'pipeline/show.html', context)