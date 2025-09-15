#Function-based View
from django.http import HttpResponse
from django.views import View



def home(request):
    return HttpResponse("Welcome to the Home Page!")


def not_found(request):
    return HttpResponse("404")


#Class-based View
class About(View):
    def get(self, request):
        return HttpResponse("About Us")