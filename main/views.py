from django.shortcuts import render, get_object_or_404, redirect
from .models import Mahsulot
from .forms import MahsulotForm

def mahsulot_list(request):
    mahsulotlar = Mahsulot.objects.all()
    return render(request, 'mahsulot_list.html', {'mahsulotlar': mahsulotlar})

def mahsulot_create(request):
    if request.method == 'POST':
        form = MahsulotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mahsulot_list')
    else:
        form = MahsulotForm()
    return render(request, 'forma.html', {'form': form, 'title': "Yangi mahsulot qo'shish"})

def mahsulot_update(request, pk):
    mahsulot = get_object_or_404(Mahsulot, pk=pk)
    if request.method == 'POST':
        form = MahsulotForm(request.POST, instance=mahsulot)
        if form.is_valid():
            form.save()
            return redirect('mahsulot_list')
    else:
        form = MahsulotForm(instance=mahsulot)
    return render(request, 'forma.html', {'form': form, 'title': "Mahsulotni tahrirlash"})

def mahsulot_delete(request, pk):
    mahsulot = get_object_or_404(Mahsulot, pk=pk)
    if request.method == 'POST':
        mahsulot.delete()
        return redirect('mahsulot_list')
    return render(request, 'ochirish.html', {'mahsulot': mahsulot})
