from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from .models import Profile, EmailVerification, ResetPasswordVerification, ChangePersonalDataRequest
from .forms import SignupFormStep1, SignupFormStep3, AccountChangeEmailForm, AccountChangePersonalDataForm


def signup(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = SignupFormStep1(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            agreed = form.cleaned_data['agreed']

            # Проверка на согласие с политикой
            if not agreed:
                messages.error(request, "Вы должны согласиться с обработкой персональных данных.")
                return render(request, 'signup.html', {'form': form})

            # Создание пользователя и профиля
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=email, email=email, password=password)
                Profile.objects.create(user=user, created=timezone.now())

                # Отправка ключа подтверждения
                EmailVerification.objects.create(user=user, new_email=email)

                # Вход пользователя и перенаправление
                login(request, user)
                messages.success(request, "Вы успешно зарегистрировались!")
                return redirect('home')
            else:
                messages.error(request, "Этот email уже зарегистрирован.")
    else:
        form = SignupFormStep1()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Неверное имя пользователя или пароль."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def account_change_email(request):
    form = AccountChangeEmailForm(request.POST or None)
    if form.is_valid():
        new_email = form.cleaned_data['new_email']

        # Проверяем, не используется ли уже email
        if not User.objects.filter(email=new_email).exists():
            EmailVerification.objects.create(user=request.user, new_email=new_email)
            message = "На новый email отправлено письмо для подтверждения."
            return render(request, 'change_email.html', {'message': message, 'form': form})
        else:
            error_message = "Этот email уже используется."
            return render(request, 'change_email.html', {'error_message': error_message, 'form': form})
    return render(request, 'change_email.html', {'form': form})


@login_required
def account_change_personal_data(request):
    form = AccountChangePersonalDataForm(request.POST or None)
    if form.is_valid():
        new_data = form.cleaned_data['new']
        field_to_update = form.cleaned_data['field_to_update']  # Например, 'name' или 'phone'

        # Создаем запрос на изменение данных
        ChangePersonalDataRequest.objects.create(profile=request.user.profile, new=new_data, type=field_to_update)
        message = "Запрос на изменение данных отправлен на модерацию."
        return render(request, 'change_personal_data.html', {'message': message, 'form': form})
    return render(request, 'change_personal_data.html', {'form': form})


def reset_password_request(request):
    """Запрос сброса пароля"""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Генерация ключа и сохранение
            key = get_random_string(length=6, allowed_chars='0123456789')
            ResetPasswordVerification.objects.create(user=user, key=key)
            # Отправка ключа пользователю (здесь можно подключить email-систему)
            messages.success(request, f'Код для сброса пароля: {key}')
            return redirect('reset_password_verify')
        else:
            messages.error(request, 'Пользователь с таким email не найден.')
    return render(request, 'password_reset_request.html')


def reset_password_verify(request):
    """Подтверждение ключа и установка нового пароля"""
    if request.method == 'POST':
        email = request.POST.get('email')
        key = request.POST.get('key')
        new_password = request.POST.get('new_password')

        reset_entry = ResetPasswordVerification.objects.filter(
            user__email=email, key=key
        ).first()

        if reset_entry:
            user = reset_entry.user
            user.set_password(new_password)
            user.save()
            reset_entry.delete()  # Удаляем ключ после успешного сброса
            messages.success(request, 'Пароль успешно изменён.')
            return redirect('login')
        else:
            messages.error(request, 'Неверный код или email.')

    return render(request, 'password_reset_verify.html')