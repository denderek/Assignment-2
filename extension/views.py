from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
	template_name = 'extension/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by('-question_text')[:5]
		
class DetailView(generic.DetailView):
	model = Question
	template_name = 'extension/detail.html'
	

def answer(request, question_id):
	#selected_choice = question.choice_set.get(pk=request.POST['choice'])'
	question = get_object_or_404(Question, pk=question_id)
	chosenChoice= str(question.choice_set.get(pk=request.POST['choice']))
	return render(request, 'extension/answer.html',{'question':question, 'answer':chosenChoice})
	
