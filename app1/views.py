from django.shortcuts import render
import logging
from random import choice
from django.http import HttpResponse
from .models import Games

# from django.db import models as m

# Create your views here.

logger = logging.getLogger(__name__)

def flip(request):
    side = choice(["орёл", "решка"])
    result = Games(side=side)
    result.save()
    return HttpResponse(result)


def stats(request):
    n = 5
    result = Games.get_stats(n)
    return HttpResponse(f"{result = }")

