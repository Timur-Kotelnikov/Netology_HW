from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    students = Student.objects.all().prefetch_related('teachers').order_by(ordering)
    context = {'students': students}
    return render(request=request, template_name='school/students_list.html', context=context)
