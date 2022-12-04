from django.shortcuts import render
# Create your views here.

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def get_food(request, dish=''):
    context = dict()
    sub_data = DATA.copy()
    if request.GET.get("servings"):
        servings = int(request.GET.get("servings"))
    else:
        servings = 1
    context['servings'] = servings
    for k, v in sub_data.items():
        for k1, v1 in v.items():
            v[k1] = v1 * servings
    if dish:
        context['recipe'] = sub_data[dish]
    return render(request=request, template_name='app_2/result.html', context=context)