from django.shortcuts import render, redirect, reverse
from .models import Article
from django.http import Http404
# Create your views here.


def archive(request):
    return render(request, 'index.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def check(name):
    try:
        article = Article.objects.get(title = name)
        if name == article.title:
            return True
        else:
            return False

    except Article.DoesNotExist:
        return False


def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if(check(form['title'])):
                form['errors']='Статья  уже есть'
                return render(request, 'create_post.html', {'form': form})
            else:
                if form["text"] and form["title"]:
                    # еслиполязаполненыбезошибок
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    article_id = Article.objects.latest('id').pk
                    return redirect('get_article', article_id)
                    # перейти на страницу поста
                else:
                    # если введенные данные некорректны
                    form['errors'] = u"Не все поля заполнены"
                    return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

