from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,
                  'clone/pages/home.html',
                  context={
                      'Model': 'LENOVO V330-15IKB',
                  })


def item(request, id):
    return render(request,
                  'clone/pages/item.html',
                  context={
                      'Product': '81AX012WJP',
                      'Model': 'LENOVO V330-15IKB',
                      'SerialNumber': 'R90T1QLE',
                      'MachineTypeNumber': '81AX012WJP',
                      'BIOSVersion': '6SCN41WW',
                      'BIOSReleaseDate': '2023-09-28T13:43:59.077Z',
                      'is_detail_page': True,
                  })
