from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_demo.models import User_data, Products



def home_page(request):
    return render(request, "home.html", {"home_last": "Testing"})



def contact_page(request):
    return render(request, "contact.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home_page_path")   
        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")



def user_logout(request):
    logout(request)
    return redirect("login")   



def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken"})

        User.objects.create_user(username=username, password=password)
        return redirect("login")   

    return render(request, "register.html")



@login_required
def form_page(request):
    if request.method == "POST":
        usr_name = request.POST["u_name"]
        usr_age = request.POST["u_age"]
        usr_city = request.POST["u_city"]
        usr_hobby = request.POST["u_hobby"]
        usr_food = request.POST["u_food"]

        User_data.objects.create(
            user_name=usr_name,
            user_age=usr_age,
            user_city=usr_city,
            user_hobby=usr_hobby,
            user_food=usr_food,
        )
        return redirect("user_list_path")

    return render(request, "form.html")



@login_required
def user_list(request):
    users_list = User_data.objects.all()
    return render(request, "user_list.html", {"Users_list": users_list})



@login_required
def user_update(request, user_id):
    if request.method == "POST":
        user_data_update = User_data.objects.get(id=user_id)
        user_data_update.user_name = request.POST["u_name"]
        user_data_update.user_age = request.POST["u_age"]
        user_data_update.user_city = request.POST["u_city"]
        user_data_update.user_hobby = request.POST["u_hobby"]
        user_data_update.user_food = request.POST["u_food"]
        user_data_update.save()
        return redirect("user_list_path")

    user_data_return = User_data.objects.filter(id=user_id).values().first()
    return render(request, "update_user.html", user_data_return)



@login_required
def user_delete(request, user_id):
    User_data.objects.filter(id=user_id).delete()
    return redirect("user_list_path")



@login_required
def product_list(request):
    pro_list = Products.objects.filter(is_available=True)
    return render(request, "product.html", {"product_list": pro_list})
