from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class ArticlesView(ListView):
    model = Articles
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Articles
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articles
    fields = ('title','body','photo')
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title','body','photo','author')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
