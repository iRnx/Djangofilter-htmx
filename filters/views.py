from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .forms import BookNameFilterForm
from .models import Book
from .filters import BookFilter
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    books_filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        'form': books_filter.form,
        'books': books_filter.qs,
        }
    return render(request, 'index.html', context)


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self) -> QuerySet[Any]:

        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
    

# API #
class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
