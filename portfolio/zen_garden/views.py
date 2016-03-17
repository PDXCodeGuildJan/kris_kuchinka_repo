from django.shortcuts import render

# Create your views here.

def zenGarden(request):
	return render(request, 'zen_garden/zen_mockup.html', {})