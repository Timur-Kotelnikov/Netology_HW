import csv

from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
def paginator(request):
    bus_stations = list()
    with open(file='/home/timur/Documents/Python/HW/Netology_hw_nogit/hw_django/hw_2/netology_2/file_1.csv') as f:
        file_csv = csv.DictReader(f)
        for row in file_csv:
            stations = dict()
            stations['Name'] = row['Name']
            stations['Street'] = row['Street']
            stations["District"] = row["District"]
            bus_stations.append(stations)
    paginator = Paginator(bus_stations, 10)
    page_num = request.GET.get("page")
    page = paginator.get_page(page_num)
    context = {
        'page': page
    }
    return render(request=request, template_name='pagi_2/paginator.html', context=context)
