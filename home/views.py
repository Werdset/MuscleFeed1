from django.shortcuts import render
from reviews.models import Review  # Предполагается, что модель отзывов находится в этом же приложении

def home(request):
    # Подгружаем последние 5 опубликованных отзывов
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:5]
    return render(request, 'home.html', {'reviews': reviews})