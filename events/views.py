from django.shortcuts import render

def events_view(request):
	return render(request, 'events/index.html')