from django import template

register = template.Library()

@register.filter(name='split')
def split_filter(value, separator=' '):
    """Разделяет строку по указанному разделителю"""
    return value.split(separator)

@register.filter(name='replace')
def replace_filter(value, args):
    """Заменяет подстроку в строке"""
    old, new = args.split(',')
    return value.replace(old, new)

@register.filter(name='weekday')
def weekday_filter(date):
    """Возвращает день недели для даты"""
    return date.strftime('%A')

@register.filter(name='remove_minus')
def remove_minus(value):
    """Удаляет символ минуса из строки"""
    return str(value).replace('-', '')

@register.filter(name='get_ordered_questions')
def get_ordered_questions(questions):
    """Сортирует вопросы по порядку"""
    return sorted(questions, key=lambda q: q.order)
