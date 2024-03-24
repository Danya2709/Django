from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>Главная</body>")


def cof(request):
    return HttpResponse("Я чайник", status=418)
