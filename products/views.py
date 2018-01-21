from django.shortcuts import render, HttpResponseRedirect
from products.models import Product


# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'product_index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST['product_name']
        unit_price = request.POST['unit_price']
        unit = request.POST['unit']
        work_type = request.POST['work_type']
        product = Product.objects.filter(name=name).first()
        if product:
            Product.objects.create(name=name, unit_price=unit_price,
                                   unit=unit, work_type=work_type)
        msg = "创建成功"
        return HttpResponseRedirect('/products?msg={}'.format(msg))
    elif request.method == 'GET':
        return render(request, 'product_create.html')


def update(request):
    product_id = request.POST['product_id']
    unit_price = request.POST['unit_price']
    unit = request.POST['unit']
    work_type = request.POST['work_type']
    product = Product.objects.filter(id=product_id).first()
    if product:
        product.update(unit=unit, unit_price=unit_price,
                       work_type=work_type)
        product.save()
        msg = "更新成功"
    else:
        msg = "该产品不存在"
    return HttpResponseRedirect('/products?msg={}'.format(msg))

