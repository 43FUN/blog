from  django.forms import ModelForm
from article.models import Comments
from article.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_text']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']





