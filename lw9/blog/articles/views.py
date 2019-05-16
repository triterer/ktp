from django.shortcuts import render, redirect, reverse
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def archive(request):
    return render(request, 'index.html', {"posts": Article.objects.all(), "user":User.objects.all()})


def scriptik(request):
    return render(request, 'kek.html', {})


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

def registr(request):
    if request.method == "POST":
        try:
            form = {
                'username': request.POST.get("username"),
                'email': request.POST.get("email"),
                'password':request.POST.get("password")
            }

            try:
                User.objects.get(username=form['username'])
                # если пользователь существует, то ошибки не произойдет ипрограмма # удачно доберется до следующей строчки
                form['errors'] = "Пользователь с таким именем уже есть"
                return render(request, 'registr.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(username=form['username'], email = form['email'], password=form['password'])
                return render(request, 'index.html', {"posts": Article.objects.all()})
        except ValueError:
            form['errors'] = "не указано имя пользователя"
            return render(request, 'registr.html', {'form': form})
    else:
        return render(request, 'registr.html', {})


def loginuser(request):
    if request.method == "POST":
        try:
            form = {
                'username': request.POST.get("username"),
                'password': request.POST.get("password")
            }
            user = authenticate(username=form['username'], password=form['password'])
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return render(request, 'index.html', {"posts": Article.objects.all()})
            else:
                # Return an 'invalid login' error message.
                form['errors'] = "invalid login"
                return render(request, 'login.html', {'form': form})
        except:
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html',{})