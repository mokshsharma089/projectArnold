from django.shortcuts import render
from home import models

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def home(request):
    games=models.Games.objects.all()
    context={
        "games":games
    }
    return render(request,'home/home.html',context)

def game_page(request,id):
    game=models.Games.objects.get(id=id)
    offers=models.Offers.objects.filter(game=game)
    context={
        "game":game,
        "offers":offers
    }
    return render(request,'home/game_page.html',context)
