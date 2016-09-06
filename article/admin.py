from django.contrib import admin
from article.models import Article, Comments

# Register your models here.


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text',
              'article_date', 'article_author']
    inlines = [ArticleInline]
    list_filter = ['article_date', 'article_author']


admin.site.register(Article, ArticleAdmin)
