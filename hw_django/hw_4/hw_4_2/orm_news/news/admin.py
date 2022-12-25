from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError
from .models import Article, Tag, Scope


class ScopeFormset(BaseInlineFormSet):
    def clean(self):
        main_num = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_num += 1
        if main_num < 1:
            raise ValidationError('Задайте основной тэг')
        elif main_num > 1:
            raise ValidationError('Только один тэг может быть основным')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
