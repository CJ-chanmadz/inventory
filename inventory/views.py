from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def display_laptops(request):
    items = Laptop.objects.all()

    context = {
        'items': items,
        'header': 'Laptops'
    }

    return render(request, 'home/index.html', context)

def display_desktops(request):
    items = Desktop.objects.all()

    context = {
        'items': items,
        'header': 'Desktops'
    }

    return render(request, 'home/index.html', context)

def display_mobiles(request):
    items = Mobile.objects.all()

    context = {
        'items': items,
        'header': 'Mobiles'
    }

    return render(request, 'home/index.html', context)

def add_device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LaptopForm()
        return render(request, 'home/add_new.html', {'form':form})

def add_laptop(request):
    return add_device(request, LaptopForm)

def add_desktop(request):
    return add_device(request, DesktopForm)

def add_mobile(request):
    return add_device(request, MobileForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'home/edit_item.html', {'form': form})

def edit_laptop(request, pk):
    return edit_item(request, pk, Laptop, LaptopForm)

def edit_desktop(request, pk):
    return edit_item(request, pk, Desktop, DesktopForm)

def edit_mobile(request, pk):
    return edit_item(request, pk, Mobile, MobileForm)

def delete_laptop(request, pk):

    template = 'home/index.html'
    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_desktop(request, pk):

    template = 'home/index.html'
    Desktop.objects.filter(id=pk).delete()

    items = Desktop.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mobile(request, pk):

    template = 'home/index.html'
    Mobile.objects.filter(id=pk).delete()

    items = Mobile.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)