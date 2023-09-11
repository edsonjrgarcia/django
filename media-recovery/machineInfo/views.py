from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request,
                  'clone/pages/home.html',
                  context={
                      'serialNumber': '128B12',
                  })


def item(request, id):
    return render(request,
                  'clone/pages/home.html',
                  context={
                      'serialNumber': '128B12',
                  })
