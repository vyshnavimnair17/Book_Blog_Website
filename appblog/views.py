from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout as auth_logout
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def homepage(request):
    home = Category.objects.all()
    return render(request, 'homepage.html', {"data": home})


@login_required(login_url='/login')
def about(request):
    bio = Category.objects.all()
    return render(request, 'About.html', {"data": bio})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print("user entered")
            auth_login(request, user)
            return redirect('/homepage/')
        else:
            return redirect('/login/')

    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/login')


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists() or User.objects.filter(password=password).exists():
            return redirect('/')

        user = User.objects.create_user(
            username=username,
            email=email
        )

        user.name = name
        user.set_password(password)
        user.save()

        return redirect('/login')
    return render(request, 'register.html')


def search(request):
    if request.method == "POST":
        search_obj = request.POST.get("search")
        items = Category.objects.filter(Q(title__icontains=search_obj) | Q(author__icontains=search_obj))
        return render(request, 'search.html', {"data": items})
    else:
        return render(request, 'results.html')


@login_required(login_url='/login')
def profile(request):
    if request.user:
        user = Category.objects.filter(user_id=request.user)
        print(user)
        return render(request, 'profile.html', {"data": user})


@login_required(login_url='/login')
def add_blog(request):
    if request.method == 'POST':
        print(request.POST)
        item = Category()
        item.title = request.POST.get("title")
        item.author = request.POST.get("author")
        item.synopsis = request.POST.get("synopsis")
        item.description = request.POST.get("description")
        item.image = request.POST.get("image")
        item.genre = request.POST.get("genre")
        item.user_id = request.user
        item.save()
        return redirect('/profile')
    return render(request, 'create_blog.html')


@login_required(login_url='/login')
def add_bio(request):
    if request.method == 'POST':
        print(request.POST)
        bio = Category()
        bio.img = request.POST.get("image")
        bio.about = request.POST.get("bio")
        bio.save()
        return redirect('/about')
    return render(request, 'Bio_form.html')


# 1 Currently Reading table
def current(request, cat_id):
    read = Category.objects.get(cat_id=cat_id)
    print(read)
    read_obj = Current(curr_read=read)
    read_obj.save()
    return redirect('/currentbook')


@login_required(login_url='/login')
def current_display(request):
    current_obj = Current.objects.all()
    print(current_obj.values())
    return render(request, 'current.html', {'data': current_obj})


# Book Review table
def review(request, cat_id):
    bookrev = Category.objects.get(cat_id=cat_id)
    print(bookrev)
    book_obj = Review(review=bookrev)
    book_obj.save()
    return redirect('/bookreview')


def review_display(request):
    rev_obj = Review.objects.all()
    print(rev_obj.values())
    return render(request, 'book_review.html', {'data': rev_obj})


def book_detail(request, rev_id):
    book = Review.objects.get(rev_id=rev_id)
    return render(request, 'description.html', {"data": book})


# TBR list table
def tbr(request, cat_id):
    list = Category.objects.get(cat_id=cat_id)
    print(list)
    list_obj = Tbr(toread=list)
    list_obj.save()
    return redirect('/tbrdisplay')


@login_required(login_url='/login')
def tbr_display(request):
    tbr_obj = Tbr.objects.all()
    print(tbr_obj.values())
    return render(request, 'tbr_list.html', {"data": tbr_obj})


# 2023 Favourites Table
def favourite(request, cat_id):
    fav = Category.objects.get(cat_id=cat_id)
    print(fav)
    fav_obj = Favourites(fav_read=fav)
    fav_obj.save()
    return redirect('/fav_display')


@login_required(login_url='/login')
def fav_display(request):
    year_obj = Favourites.objects.all()
    print(year_obj.values())
    return render(request, 'favourite.html', {"data": year_obj})


# Monthly Wrapup Table
def month(request, cat_id):
    wrap = Category.objects.get(cat_id=cat_id)
    print(wrap)
    wrap_obj = Wrapup(month=wrap)
    wrap_obj.save()
    return redirect('/monthdisplay')


@login_required(login_url='/login')
def month_display(request):
    month_obj = Wrapup.objects.all()
    print(month_obj.values())
    return render(request, 'wrapup.html', {"data": month_obj})


# Recommendations Table
def recom(request, cat_id):
    table = Category.objects.get(cat_id=cat_id)
    print(table)
    table_obj = Recommendation(recommend=table)
    table_obj.save()
    return redirect('/recom_display')


@login_required(login_url='/login')
def recom_display(request):
    recom_obj = Recommendation.objects.all()
    print(recom_obj.values())
    return render(request, 'recommend.html', {"data": recom_obj})


# Edit blog
@login_required(login_url='/login')
def edit_blog(request, cat_id):
    user = Category.objects.get(cat_id=cat_id)
    if request.method == "POST":
        user.title = request.POST.get("title")
        user.author = request.POST.get("author")
        user.synopsis = request.POST.get("synopsis")
        user.description = request.POST.get("description")
        user.image = request.POST.get("image")
        user.genre = request.POST.get("genre")
        user.save()
        return redirect('/profile')
    return render(request, 'edit_blog.html', {"data": user})


# Delete blog
@login_required(login_url='/login')
def delete_blog(request, cat_id):
    dlt_item = Category.objects.get(cat_id=cat_id)
    dlt_item.delete()
    return redirect('/profile')
