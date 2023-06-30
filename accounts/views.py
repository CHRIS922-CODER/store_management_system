from django.shortcuts import render,redirect
from django.contrib.auth import forms
from django.contrib import messages
from .forms import CreationUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def start_app(request):
    return redirect('login')

@staff_member_required
def register(request):
    if request.method == 'POST':
        form = CreationUserForm(request.POST,request=request)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'{username} Registered successfully!',extra_tags='success')
            return redirect('login')
        else:
            form = CreationUserForm(request=request)
              # Concatenate form errors into a single string
            form_errors = ', '.join(str(error) for field_errors in form.errors.values() for error in field_errors)
            messages.error(request, form_errors)
            messages.warning(request, 'Please correct the errors below.')
    else:

        form = CreationUserForm(request=request)
        context = {
            'form':form,
            'messages': messages.get_messages(request)
        }
        return render(request,'accounts/register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            username = user.username
            request.session['username'] = username
            if user.is_superuser:
                messages.success(request, 'Welcome ' + username, extra_tags='success')
                request.session['username'] = username
                return redirect('/commodity_app/')
            else:
                messages.success(request, 'Welcome ' + username, extra_tags='success')
                request.session['username'] = username
                return redirect('/staff_app/')
        else:
            messages.warning(request, 'Wrong login credentials', extra_tags='warning')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')