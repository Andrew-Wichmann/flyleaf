from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Book

# Create your views here.
class IndexView(generic.TemplateView):
    model = Book
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class BookOfTheMonthView(generic.ListView):
    model = Book
    template_name = 'catalog/botm.html'

    def get_context_data(self, **kwargs):
        context = super(BookOfTheMonthView, self).get_context_data(**kwargs)
        botm = Book.objects.first()
        context['botm'] = botm
        context['other_books'] = Book.objects.exclude(id=botm.id)
        return context

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('catalog:index')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/signup.html', {'form': form})