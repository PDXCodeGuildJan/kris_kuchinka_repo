from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.http import JsonResponse
import json

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


def submit_vote(request):
	"""Handles vote submissions via AJAX"""
	# Basic security checking
	if request.method == 'POST':
		
		# Decode request body from bytecode to normal
		data_json = request.body.decode('utf-8')

		# Convert data from string to object
		data = json.loads(data_json)
		
		# Get the choice at that id
		choice = Choice.objects.get(pk=int(data['choice_id']))

		# Increment the votes of the choice by 1
		choice.votes += 1

		# Save the updated object choice to the database
		choice.save()

		# Get all the choices for the question just voted on
		question = Question.objects.get(pk=int(data['question_id']))

		# Get all the choices for the question just voted on
		question_choices = question.choice_set.all()
		
		# Loop through the choices and add them to a dictionary
		response = []
		for choice in question_choices:
			c_dict = {
				'id': choice.id,
				'text': choice.choice_text,
				'votes': choice.votes
			}
			response.append(c_dict)

	
	# takes python dictionary and turns into a list of JSON data
	return JsonResponse({'data': response})





