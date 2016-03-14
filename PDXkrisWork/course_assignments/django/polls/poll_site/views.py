from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse

from .models import Question, Choice

# Create your views here.
def index(request):
	questions = Question.objects.all()
	context = {
		'questions': questions,
		'name': 'Kris',
		'fav_color': 'green',
		'toys': [
			'MacBook',
			'iPad',
			'remote control',
		]

	}

	return render(request, 'poll_site/index.html', context)

def another_page(request):
	return render(request, 'poll_site/another.html', context)


def question_details(request, question_id):

	print("Passed Question:", question_id)

	question = get_object_or_404(Question, pk=question_id)

	context = {
		'question': question,
	}

	return render(request, 'poll_site/question_details.html', context)