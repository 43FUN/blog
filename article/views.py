from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm, ArticleForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from users.models import User
import datetime
# Create your views here.


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    authors = User.objects.filter(article__isnull=False).distinct()
    get_params = request.GET
    requested_author = get_params.get('author', None)
    if requested_author:
        all_articles = all_articles.filter(
            article_author_id=int(requested_author))

    requested_date = get_params.get('date', None)
    if requested_date:
        if requested_date == '7':
            start_date = datetime.datetime.now()\
                         - datetime.timedelta(days=7)
            end_date = datetime.datetime.now()
            all_articles = all_articles.filter(
                article_date__range=(start_date, end_date))

    if requested_date:
        if requested_date == '31':
            start_date = datetime.datetime.now()\
                         - datetime.timedelta(days=31)
            end_date = datetime.datetime.now()
            all_articles = all_articles.filter(
                article_date__range=(start_date, end_date))

    if requested_date:
        if requested_date == '365':
            start_date = datetime.datetime.now()\
                         - datetime.timedelta(days=365)
            end_date = datetime.datetime.now()
            all_articles = all_articles.filter(
                article_date__range=(start_date, end_date))

    current_page = Paginator(all_articles, 5)
    return render(request, 'articles.html', {
        'articles': current_page.page(page_number),
        'username': auth.get_user(request).username,
        'authors': authors
    })


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(
        comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article.html', args)


def addlike(request, article_id):
    back_url = request.META['HTTP_REFERER']
    try:
        if article_id in request.COOKIES:
            redirect(back_url)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(back_url)
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)


def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(
                id=article_id)
            comment.comments_author = request.user
            comment.avatar = request.user.avatar
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id, request.user)


def article_edit(request, article_id):
    article = Article.objects.get(id=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    args = {}
    args['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/articles/get/%s/' % article_id)
    return render(request, 'article_edit.html', args)


def article_add(request):
    form = ArticleForm(request.POST)
    args = {}
    args['form'] = form
    args['article_author'] = request.user
    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            article.article_author = request.user
            article.save()
            return redirect('users:profile')
    return render(request, 'article_add.html', args)


def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('users:profile')

