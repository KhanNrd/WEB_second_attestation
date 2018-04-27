from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from api.models import Category, Product

@csrf_exempt
def index(request):
    return JsonResponse({"endterm": "web"}, safe=False)

@csrf_exempt
def all_categories(request):
    if request.method == "GET":
        categories = Category.objects.all().order_by('name')
        categories_json = [c.to_json() for c in categories]
        return JsonResponse({"categories": categories_json}, safe=False)
    else:
        return JsonResponse({"error": str(e)}, status=404)


@csrf_exempt
def all_products(request):
    if request.method == "GET":
        products = Product.objects.all().order_by('name')
        products_json = [p.to_json() for p in products]
        return JsonResponse({"products": products_json}, safe=False)
    else:
        return JsonResponse({"error": str(e)}, status=404)


@csrf_exempt
def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        if name is None or len(name) is 0:
            return JsonResponse({"error": str(e)}, status=404)
        
        new_category, _ = Category.objects.get_or_create(name=name)
        return JsonResponse({"category": new_category.to_json()}, safe=False)
    else:
        return JsonResponse({"error": str(e)}, status=404)


@csrf_exempt
def add_product(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name', '')
        product_name = request.POST.get('product_name', '')
        price = request.POST.get('price', 0)
        print(category_name, product_name, price)
        new_category, _ = Category.objects.get_or_create(name=category_name)
        new_product, _ = Product.objects.get_or_create(name=product_name, price=price, category=new_category)
        return JsonResponse({"product": new_product.to_json()}, safe=False)
    else:
        return JsonResponse({"error": str(e)}, status=404)

@csrf_exempt
def delete_product(request):
    if request.method == "POST":
        product_id = request.POST.get('id', '')
        if product_id is None or len(product_id) is 0:
            return JsonResponse({"error": str(e)}, status=404)
        try:
            product = Product.objects.get(id=product_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        product.delete()
        return JsonResponse({"deleted": True}, safe=False)
    else:
        return JsonResponse({"error": str(e)}, status=404)


@csrf_exempt
def edit_product(request):
    if request.method == "POST":
        product_id = request.POST.get('id', '')
        category_name = request.POST.get('category_name', '')
        product_name = request.POST.get('product_name', '')
        price = request.POST.get('price', 0)

        if product_id is None or len(product_id) is 0:
            return JsonResponse({"error": str(e)}, status=404)
        try:
            product = Product.objects.get(id=product_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        if category_name is not None and len(category_name) is not 0:
            category, _ = Category.objects.get_or_create(name=category_name)
            product.category = category
        if product_name is not None and len(product_name) is not 0:
            product.name = product_name
        if price is not None and price is not 0:
            product.price = price
        product.save()
        return JsonResponse({"product": product.to_json()}, safe=False)
    else:
        return JsonResponse({"error": str(e)}, status=404)