from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, QuestionBlock
from .forms import ReviewForm

def reviews_show_all(request):
    """Отображение всех опубликованных отзывов"""
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

@login_required
def write_review(request):
    """Добавление нового отзыва пользователем"""
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('reviews:reviews_show_all')
    return render(request, 'reviews/write_review.html', {'form': form})

def faq(request):
    """Отображение списка часто задаваемых вопросов (FAQ)"""
    question_blocks = QuestionBlock.objects.prefetch_related('questions').all()
    return render(request, 'reviews/faq.html', {'question_blocks': question_blocks})

