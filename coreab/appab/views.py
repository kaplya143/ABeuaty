# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


def home(request):
    if request.method == 'POST':
        form = BackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BackForm()
    data = {
        'form': form,
    }
    return render(request, "appab/home.html", data)


def about(request):
    return render(request, "appab/about.html")


def services(request):
    tovar = Tovar.objects.all()
    data = {
        'tovar': tovar,
    }
    return render(request, "appab/services.html", data)


def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../services")
    else:
        form = TestForm()
    data = {
        "form": form,
    }
    return render(request, "appab/test.html", data)


def reg(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('../vhod')
    else:
        form = Register()
    return render(request, 'appab/register.html', {'form': form})


class LoginUser(auth_views.LoginView):
    form_class = auth_views.AuthenticationForm
    template_name = 'appab/vhod.html'
    extra_context = {'title': 'Вход'}
    success_url = reverse_lazy('your-success-url')


def logout_view(request):
    logout(request)
    return redirect('../home')


@login_required
def profil(request):
    return render(request, 'appab/profil.html', {'user': request.user})


def service_appointment(request):
    if request.method == 'POST':
        form = ServiceAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../success')
    else:
        form = ServiceAppointmentForm()

    return render(request, 'appab/service_form.html', {'form': form})