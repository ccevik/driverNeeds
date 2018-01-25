from django.shortcuts import render

def wait_point_view(request):
	return render(request, 'wait_point/index.html')