from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    products = Product.objects.all()[:12]
    return render(request, 'catalog/home.html', {'products': products})

@login_required(login_url='login')
def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})

@login_required(login_url='login')
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'catalog/category_form.html', {'form': form})

@login_required(login_url='login')
def category_update_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'catalog/category_form.html', {'form': form, 'category': category})

@login_required(login_url='login')
def category_delete_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('category_list')
    return render(request, 'catalog/category_confirm_delete.html', {'category': category})

# ============================
# Product CRUD
# ============================

@login_required(login_url='login')
def product_list_view(request):
    products = Product.objects.select_related('category').all()
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, 'catalog/product_list.html', {'products': products})

@login_required(login_url='login')
def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'catalog/product_detail.html', {'product': product})

@login_required(login_url='login')
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/product_form.html', {'form': form})

@login_required(login_url='login')
def product_update_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_form.html', {'form': form, 'product': product})

@login_required(login_url='login')
def product_delete_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'catalog/product_confirm_delete.html', {'product': product})
