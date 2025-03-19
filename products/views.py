from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# List all products for the logged-in shop_owner
@login_required
def product_list(request):
    if request.user.role == 'shop_owner':  # Only shop_owner can view their products
        products = Product.objects.filter(shop_owner=request.user)
        return render(request, 'product/product_list.html', {'products': products})
    return redirect('home')  # Customers are redirected to home

# Create a new product for the logged-in shop_owner
@login_required
def product_create(request):
    if request.user.role == 'shop_owner':  # Ensure only shop_owner can create
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.shop_owner = request.user  # Associate product with the logged-in shop_owner
                product.save()
                return redirect('product_list')
        else:
            form = ProductForm()
        return render(request, 'product/product_form.html', {'form': form})
    return redirect('home')

# Update a product for the logged-in shop_owner
@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, shop_owner=request.user)  # Ensure product belongs to the logged-in shop_owner
    if request.user.role == 'shop_owner':  # Ensure only shop_owner can edit
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_list')
        else:
            form = ProductForm(instance=product)
        return render(request, 'product/product_form.html', {'form': form})
    return redirect('home')

# Delete a product for the logged-in shop_owner
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, shop_owner=request.user)  # Ensure product belongs to the logged-in shop_owner
    if request.user.role == 'shop_owner':  # Ensure only shop_owner can delete
        if request.method == 'POST':
            product.delete()
            return redirect('product_list')
        return render(request, 'product/product_confirm_delete.html', {'product': product})
    return redirect('home')