from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Student
import datetime

# Create your views here.

def newstudent(request):
   if request.method == 'POST':
      student_name = request.POST['student_name']
      father_name = request.POST['father_name']
      dob = request.POST['dob']
      address = request.POST['address']
      city = request.POST['city']
      state = request.POST['state']
      pin = request.POST['pin']
      mobile = request.POST['mobile']
      email = request.POST['email']
      class_opted = request.POST.get('class_opted',True)
      marks = request.POST['marks']

      student = Student.objects.create(student_name=student_name, father_name=father_name, dob=dob, address=address, city=city, state=state, pin=pin, mobile=mobile, email=email, class_opted=class_opted, marks=marks)
      student.save()
      messages.info(request, 'Student created sucessfully')
      return render(request, 'newstudent.html')
   else:
      return render(request, 'newstudent.html')

'''   
def register(request):
   if request.method == 'POST':
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      password1 = request.POST['password1']
      password2 = request.POST['password2']

      if password1 == password2:
         if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken')
            return redirect('register')
         elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('register')
         else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                            password=password1)
            user.save()
            messages.info(request, 'user created sucessfully')
            return redirect('login')
      else:
         messages.info(request, 'password is not matching....!')
         return redirect('register')

   else:
      return render(request, 'newstudent.html')


def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
         auth.login(request, user)
         return redirect('/')
      else:
         messages.info('Invalid Credentails')
         return redirect('login')

   else:
      return render(request, 'login.html')


def logout(request):
   auth.logout(request)
   return redirect('/')


'''

def enrolmrnt(request):
   data = Student.objects.all()
   student = {
      "student_number": data
   }
   return render(request, "dashboard.html", student)

