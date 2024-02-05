
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from pprint import pprint
from .middleware import auth, guest, autha
from .models import UploadedImage
from .forms import UploadImageForm




@guest
@autha
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Authenticate user before logging in
            authenticated_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, 'You have successfully registered!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Failed to authenticate the user. Please try again.')
    else:
        messages.error(request, 'There was an error with your registration. Please check your inputs.')
        initial_data = {'username': '', 'password1': '', 'password2': ''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form})



@auth
def profile_view(request):
    context = {'username': request.user.username}
    return render(request, 'profile.html', context)

def trending_view(request):
    context = {'username': request.user.username}
    return render(request, 'trending.html', context)
    

def login_view(request):
    
    if request.method=='POST':

        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect ('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form': form})

    
@auth
def dashboard_view(request):
    images = UploadedImage.objects.all()
    
    # Pass the images to the template context
    context = {'images': images}
    
    return render(request, 'dashboard.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('login')





def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_list.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        print(request.POST)
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'image_list', {'form': form})

    else:
        form = UploadImageForm()

    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_list.html', {'images': images})