from django.shortcuts import render, redirect, get_object_or_404

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# Create your views here.


def index(request):
    user = request.user
    question_list = Question.objects.order_by('-asked_date')
    return render(request, 'home/index.html', {'user': user, 'question_list': question_list})


def create_question(request):
    if not request.user.is_authenticated:
        return render(request, 'account/loginform.html')
    else:
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            a_question = form.save(commit=False)
            a_question.asked_by = request.user
            a_question.save()
            return redirect('home:index')
        context = {
            "form": form,
        }
        return render(request, 'home/create_question.html', context)


def create_answer(request, question_id):
    form = AnswerForm(request.POST or None)
    question = get_object_or_404(Question, pk=question_id)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.question = question
        answer.answered_by = request.user

        answer.save()
        return redirect('home:all_answer', question_id)
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'home/create_answer.html', context)


def all_answers(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_list = question.answer_set.all()
    return render(request, 'home/question_detail.html', {'question': question, 'answer_list': answer_list})


def delete_answer(request, question_id, answer_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = question.answer_set.get(pk=answer_id)
    answer.delete()
    return redirect('home:all_answer', question_id)


def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()
    return redirect('home:index')


def update_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        a_question = form.save(commit=False)
        question.question_title = a_question.question_title
        question.save()
        return redirect('home:index')
    context = {
        "form": form,
        'previous_question': question,
    }
    return render(request, 'home/update_question.html', context)
