from django.shortcuts import render
from django.utils import timezone
from .models import Clothingplain

# Create your views here.
def completeclothinglist(request):
    posts = Clothingplain.objects.order_by('name')
    return render(request, 'tracker/completeclothinglist.html', {'posts': posts})