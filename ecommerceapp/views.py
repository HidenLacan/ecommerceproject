from django.shortcuts import render
from .models import products,order
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    products_to_post = products.objects.all()

    #search section
    search_product = request.GET.get('search_product')
    if search_product != '' and search_product is not None:
        products_to_post = products_to_post.filter(title__icontains=search_product)
        # ////////////////////////////////////////in this part of code the _ is double to filter , and also
        #///////////////////////////////////////// the parameter icontains filter the content about variable destiny for instance title

    #pagination section
    paginator = Paginator(products_to_post,4)
    page = request.GET.get('page')
    products_to_post = paginator.get_page(page)

    return render(request,'home.html',{'products_to_post':products_to_post})

def detail_view(request,id):
    products_to_post = products.objects.get(id=id)
    return render(request,'view_detail.html',{'products_to_post':products_to_post})

def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        dire = request.POST.get('dire','')
        state = request.POST.get('state','')
        city = request.POST.get('city','')
        zip_code = request.POST.get('zip_code','')
        total = request.POST.get('total','')
        aorder = order(name=name,email=email,dire=dire,state=state,city=city,zip_code=zip_code,items=items,total=total)
        aorder.save()



    return render(request,'checkout.html')