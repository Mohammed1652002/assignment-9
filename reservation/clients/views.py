# views.py
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Assuming you have a URL named 'product_list'
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})
