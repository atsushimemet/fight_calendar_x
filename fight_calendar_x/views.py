from django.shortcuts import render


def index(request):
    return render(request, "fight_calendar_x/index.html")
