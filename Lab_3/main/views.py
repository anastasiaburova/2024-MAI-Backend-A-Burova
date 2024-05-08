import json

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Category, Product, Customer, Order, OrderItem

@csrf_exempt
@require_http_methods(['GET'])
def categories(request):
    #category_objects = Category.objects.all()
    #return JsonResponse({'categories': [model_to_dict(category) for category in category_objects]})
    return JsonResponse({'category': "model_to_dict(current_category)"})

@csrf_exempt
@require_http_methods(['GET'])
def products(request):
    product_objects = Product.objects.all()
    return JsonResponse({'product': "model_to_dict(current_product)"})
    # return JsonResponse({'products': [model_to_dict(product) for product in product_objects]})

@csrf_exempt
@require_http_methods(['GET'])
def category(request, category_id):
    # current_category = Category.objects.get(pk=category_id)
    # return JsonResponse({'category': model_to_dict(current_category)})
    return JsonResponse({'category': "model_to_dict(current_category)"})

@csrf_exempt
@require_http_methods(['GET'])
def product(request, product_id):
    current_product = Product.objects.get(pk=product_id)
    return JsonResponse({'product': "model_to_dict(current_product)"})
    # return JsonResponse({'product': model_to_dict(current_product)})

@csrf_exempt
@require_http_methods(['POST'])
def create_product(request):
    # data = json.loads(request.body)
    # category_id = data.get('category_id')
    # category = Category.objects.get(pk=category_id)
    # product = Product.objects.create(
    #     name=data.get('name'),
    #     description=data.get('description'),
    #     price=data.get('price'),
    #     category=category,
    #     available=data.get('available')
    # )

    #return JsonResponse({'product': model_to_dict(product)})
    return JsonResponse({'product': "none"})

@csrf_exempt
@require_http_methods(['PUT'])
def update_product(request, product_id):
    # data = json.loads(request.body)
    # product = Product.objects.get(pk=product_id)
    # category_id = data.get('category_id')
    # category = Category.objects.get(pk=category_id)
    # product.name = data.get('name')
    # product.description = data.get('description')
    # product.price = data.get('price')
    # product.category = category
    # product.available = data.get('available')
    # product.save()
    # return JsonResponse({'product': model_to_dict(product)})
    return JsonResponse({'product': "model_to_dict(product)"})

# @csrf_exempt
# @require_http_methods(['DELETE'])
# def delete_product(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     product.delete()
#     return JsonResponse({'status': 'ok'})

