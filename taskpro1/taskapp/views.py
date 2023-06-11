from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


def school(request):
    return render(request, "school.html")
def newpage(request):
    return render(request, "newpage.html")
def form(request):
    return render(request, "Form.html")
def login(request):
    return render(request, "login.html")
def register(request):
    return render(request, "Register.html")



# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request, "invalid credentials")
#             return redirect('/')
#     return render(request, "login.html")
# def Register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST.get('password')
#         cpassword = request.POST['cpassword']
#         if password==cpassword:
#                 user = User.objects.create_user(username=username,password=password)
#                 user.save()
#                 print("user created")
#                 return redirect('login')
#         else:
#             messages.info(request,"password not matching")
#             return redirect('/')
#     return render(request,"Register.html")

