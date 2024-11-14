from django.utils import timezone, translation
from django.template.defaultfilters import register as reg

def activate_translations(request, language):
    """Активирует перевод для указанного языка"""
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language

def wrap_data(context):
    """Оборачивает данные в единый контекст"""
    common_context = {
        'project_name': 'My Project',
        'year': timezone.now().year,
    }
    common_context.update(context)
    return common_context
