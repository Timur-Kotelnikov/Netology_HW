from django.shortcuts import render

from .models import Phone


def show_catalog(request):
    phone = Phone.objects.all()
    if request.GET.get("sort") == "name":
        phone = Phone.objects.order_by('name')
    elif request.GET.get("sort") == "min_price":
        phone = Phone.objects.order_by('price')
    elif request.GET.get("sort") == "max_price":
        phone = Phone.objects.order_by('-price')
    context = {
        'phones': phone
    }
    return render(request=request, template_name='orm_phones/catalog.html', context=context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request=request, template_name='orm_phones/product.html', context=context)
