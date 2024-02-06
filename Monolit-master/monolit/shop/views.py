from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import *
from .models import *

class IndexView (ListView):
    model = Product
    paginate_by = 5
    template_name = 'index.html'
    def index(self):
        return render(self, 'index.html')
    def get_queryset(self):
        object_list = Product.objects.order_by('-date')
        return object_list

class ProductDetail(DetailView):
    model = Product
    def details(self):
        return render(self, 'details.html')

class AllProduct(ListView):
    model = Product
    paginate_by = 10
    template_name = 'service.html'
    success_url = reverse_lazy('service')
    def service(self):
        return render(self, 'service.html')
    def get_queryset(self):
        object_list = Product.objects.order_by('-date')
        return object_list

class AllFirma(ListView):
    model = Product
    paginate_by = 10
    template_name = 'firma.html'
    success_url = reverse_lazy('firma')
    def service(self):
        return render(self, 'firma.html')

class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')
    def registration(self):
        return render(self, 'user/register.html')

class LoginViewMy(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('index')
    def login(self):
        return render(self, 'user/login.html')
class LogoutView(LogoutView):
    form_class = CustomUser
    template_name = 'user/logout.html'
    success_url = reverse_lazy('index')
    def logout(self):
        return render(self, 'user/logout.html')

class ProfileView(UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'avatar']
    success_url = reverse_lazy('profile')
    template_name = 'user/profile.html'

class SearchResult(ListView):
    model = Product
    paginate_by = 10
    template_name = 'result.html'

    def result(self):
        return render(self, 'result.html')
    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(title=query)
        return object_list
class ProductDetail(DetailView):
    model = Product
    template_name = 'details.html'
    success_url = reverse_lazy('details')
    def details(self):
        return render(self, 'details.html')
