from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)

    if form.is_valid():
      form.save() # saving the user in DB
      
      username = form.cleaned_data.get('username')
      messages.success(request, f"Account created for {username}!")

      return redirect('blog-home')

  else:
    form = UserRegisterForm()

  # Returns empty form for GET request
  # Returns form with erros if 'is_valid' check fails
  return render(request, 'users/register.html', { 'form': form })
