from urllib import request
from homepage.models import Faculty, Restaurant
from django.shortcuts import render

# Create your views here.


def home(request):
    search = request.GET.get('inputSearch', '')
    faculty = Faculty.objects.all()
    classes = Restaurant.objects.filter(
        name__icontains=search
    )
    return render(request, template_name='home.html',
                  context={
                      'search': search,
                      'classes': classes,
                      'faculty': faculty}
                  )


def management(request):
    return render(request, template_name='management.html')


def detail(request):
    return render(request, template_name='detail.html')
