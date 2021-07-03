from django.shortcuts import render
from .models import Product
from .models import Orders
from django.core.paginator import Paginator

# Create your views here.
def Index(request):
    product_objects=Product.objects.all()

    #search_code
    item_name = request.GET.get('item_name')
    if item_name!='' and item_name!=None:
        product_objects=Product.objects.filter(title__icontains=item_name)

    #paginator_code
    paginator=Paginator(product_objects,2)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)
    
    return render(request,'shop/index.html',{'product_objects':product_objects})

def Detail(request,id):

    product_object=Product.objects.get(id=id)

    return render(request,'shop/detail.html',{'product_object':product_object})
 
def Checkout(request):
    
    if request.method == "POST":
        items=request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip',"")
        total=request.POST.get('total')

        orders=Orders(total=total,item=items,name=name,email=email,address=address,city=city,state=state,zip=zip)
        orders.save() 
    
    

    return render(request,'shop/checkout.html')
