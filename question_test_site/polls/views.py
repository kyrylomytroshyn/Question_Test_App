
from django.shortcuts import render, redirect, get_object_or_404

from .models import Test
from .forms import PostForm


def index(request):
    context = {"posts": Test.objects.select_related('category')}
    return render(request, "posts/index.html", context)

