from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpRequest
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomRegForm, CodeForm
from .models import Profile, EmailCode

class RegView(FormView):
    template_name = 'my_auth/registration.html'
    form_class = CustomRegForm
    success_url = reverse_lazy('my_auth:code')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(
            user=user,
            phone=form.cleaned_data['phone'],
            birthday=form.cleaned_data['birthday'],
            reason=form.cleaned_data['reason'],
        )

        # генерируем код
        code = get_random_string(length=6, allowed_chars='0123456789')
        EmailCode.objects.create(user=user, code=code)

        # отправляем письмо
        send_mail(
            'Код подтверждения регистрации',
            f'Ваш код: {code}',
            'sshlyuz@yandex.ru',
            [user.email],
            fail_silently=False,
        )

        # сохраняем user.id в сессии для проверки
        self.request.session['verify_user_id'] = user.id

        return super().form_valid(form)

@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/auth')


class CodeView(FormView):
    template_name = 'my_auth/code.html'
    form_class = CodeForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user_id = self.request.session.get('verify_user_id')
        if not user_id:
            form.add_error(None, 'Сессия подтверждения устарела.')
            return self.form_invalid(form)

        user = get_object_or_404(User, id=user_id)
        code = EmailCode.objects.filter(user=user).last()

        # Проверяем код
        if not code or code.is_expired() or code.code != form.cleaned_data['code']:
            form.add_error('code', 'Неверный или просроченный код.')
            return self.form_invalid(form)

        # Активируем пользователя
        user.is_active = True
        user.save()

        # Удаляем код и очищаем сессию
        code.delete()
        del self.request.session['verify_user_id']

        return redirect(self.get_success_url())


