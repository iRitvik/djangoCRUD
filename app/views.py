from django.shortcuts import render, redirect
from .models import Users
# Create your views here.
def index(request):
    data = Users.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)
    
def insertData(request):
    if request.method == "POST":
        name = request.POST['name']
        photo = request.POST['photo']
        email = request.POST['email']
        password = request.POST['password']
        mobilenumber = request.POST['mobilenumber']
        age = request.POST['age']
        dateOfBirth = request.POST['dateOfBirth']
        gender = request.POST['gender']

        print(name,email,password)
        query = Users(name = name, photo = photo, email = email, password = password, mobilenumber = mobilenumber, age= age, dateOfBirth = dateOfBirth, gender = gender)
        query.save()
        return redirect("/")

    return render(request, "index.html")
    
def updateData(request,id):
    if request.method == "POST":
        name = request.POST['name']
        photo = request.POST['photo']
        email = request.POST['email']
        password = request.POST['password']
        mobilenumber = request.POST['mobilenumber']
        age = request.POST['age']
        dateOfBirth = request.POST['dateOfBirth']
        gender = request.POST['gender']

        edit = Users.objects.get(id = id)
        edit.name = name
        edit.photo = photo
        edit.email = email
        edit.password = password
        edit.mobilenumber = mobilenumber
        edit.age = age
        edit.dateOfBirth = dateOfBirth
        edit.gender = gender
        edit.save()
        return redirect("/")
    
    d = Users.objects.get(id = id)
    context = {"d": d}
    return render(request, "edit.html", context)
    
def deleteData(request,id):
    d = Users.objects.get(id = id)
    d.delete()
    return redirect("/")    
    
def about(request):
    return render(request, "about.html")
