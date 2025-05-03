# # DjangoWebApps/goods/views.py
# from django.shortcuts import render, get_object_or_404
# from .models import Product, Category
# from django.core.paginator import Paginator
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#
#     return render(request, 'goods/product_list.html', {
#         'category': category,
#         'categories': categories,
#         'products': products
#     })
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'goods/product_detail.html', {'product': product})
#
# def category_list(request, category_slug=None):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category, available=True)
#
#     # 分页功能
#     paginator = Paginator(products, 12)  # 每页显示12个产品
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'goods/category_list.html', {
#         'category': category,
#         'page_obj': page_obj
#     })