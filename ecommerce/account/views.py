from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store')

    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)
