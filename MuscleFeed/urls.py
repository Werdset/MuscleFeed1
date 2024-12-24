from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

# Основные маршруты (без префикса языка)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Поддержка смены языка
    path('', include('home.urls')),  # Главная страница доступна без префикса
    path('admin/', admin.site.urls),
]

# Многоязычные маршруты
urlpatterns += i18n_patterns(

    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
    path('notifications/', include('notifications.urls')),
    path('reviews/', include('reviews.urls')),
    path('reports/', include('reports.urls')),
    path('dishes/', include('dishes.urls')),
)