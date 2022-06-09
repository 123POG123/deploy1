from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import *
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import Product
from .forms import FormProduct, AuthorsForm


class SearchHomePageView(ListView):
    template_name = 'app/search_view.html'
    model = Product
    context_object_name = 'search'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_name'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        return (Product.objects.filter(
            Q(title__icontains=query)
        ))


def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")


def home(request):
    authorForm = AuthorsForm()
    post = Product.objects.all()
    form = FormProduct(request.POST)
    new_visit = request.session.get('new_session', 0)
    request.session['new_session'] = new_visit + 1

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormProduct()
    context = {
        'post': post,
        'form': form,
        'new_visit': new_visit,
        'authorForm': authorForm,
    }
    return render(request, 'app/home.html', context)


def about(request, p_key):
    product = get_object_or_404(Product, pk=p_key)
    context = {
        'product': product
    }
    return render(request, 'app/about.html', context)


def contact(request):
    context = {

    }
    return render(request, 'app/contact.html', context)
