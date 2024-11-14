from django.utils import timezone

def project_context(request):
    """Добавляет общие данные в контекст шаблонов"""
    return {
        'project_name': 'My Project',
        'current_year': timezone.now().year,
    }
