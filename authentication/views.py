from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, EmailVerification, ResetPasswordVerification, ChangePersonalDataRequest
from .forms import SignupFormStep1, SignupFormStep3, AccountChangeEmailForm, AccountChangePersonalDataForm


def signup(request, step):
    if step == 1:
        form = SignupFormStep1(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            agreed = form.cleaned_data['agreed']

            # Создаем профиль, если согласие получено
            if agreed:
                user = User.objects.create_user(username=email, email=email, password=None)
                Profile.objects.create(user=user)
                # Отправка email для подтверждения
                EmailVerification.objects.create(user=user)
                return redirect('signup', step=3)
    elif step == 3:
        form = SignupFormStep3(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.name = form.cleaned_data['user_name']
            profile.surname = form.cleaned_data['user_surname']
            profile.sex = form.cleaned_data['user_sex']
            profile.phone = form.cleaned_data['user_phone']
            profile.address = form.cleaned_data['user_address']
            profile.save()
            return redirect('home')
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

