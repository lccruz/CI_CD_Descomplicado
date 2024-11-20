from django.http import JsonResponse
from product.models import Product
from product.services import get_service_data


def product_list(request):
    """Product List."""
    products = Product.objects.all().values()

    data = {
        'products': list(products),
        'external': get_service_data()
    }

    return JsonResponse(data, safe=False)
