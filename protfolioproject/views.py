from django.shortcuts import render
from database.models import Testimonial, About, Aboutextra, Hero,HeroCV
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect



def Home (request):
    perosn = Testimonial.objects.all()
    about = About.objects.all()
    aboutextra=Aboutextra.objects.all()
    img = Hero.objects.all()
    herolist =Hero.objects.all()
    favicon=Hero.objects.all()
    file = HeroCV.objects.all()
   
  
    try:
        with open ('input.txt') as files:
            file_read=files.read()
        print('File is there')  
    except FileNotFoundError:
        print('File not found')  
    finally:
        print('Finally Block exicuted')    
    
    
    

    return render (request,'index.html',{'testimonials':perosn,'about':about,'about1':aboutextra,'imagefild':img,'nam':herolist,'favicon':favicon,'file':file})

def Login (request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')

    return render (request,'login.html')


def Registration (request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
    
        if password1 != password2:
            return render(request, 'registration.html', {'error': 'Passwords do not match.'})

        
        if User.objects.filter(username=user_name).exists():
            return render(request, 'login.html', {'error': 'Username already exists.'})

        
        user = User.objects.create_user(
            username=user_name,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        return render (request,'login')
    return render (request,'registration.html')


def Logout(request):
    if request.method=='POST':
        auth.logout(request)
        return render (request,'login.html')
    
    
def Dashboard (request):
    if request.user.is_authenticated:
        return render (request,'dashboard.html')
    return render ( request,'login.html')