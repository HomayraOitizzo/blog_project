from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    form = UserCreationForm(request.POST)
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form': form, 'registered': registered}
    return render(request, 'App_Login/signup.html',context=dict)
