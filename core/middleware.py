from django.utils import translation

class LanguageMiddleware:
    """Промежуточное ПО для установки языка по сессии пользователя"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.session.get(translation.LANGUAGE_SESSION_KEY)
        if language:
            translation.activate(language)
        response = self.get_response(request)
        translation.deactivate()
        return response
