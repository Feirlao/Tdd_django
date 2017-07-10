from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item
# Create your views here.
def home_page(request):
<<<<<<< HEAD

    item=Item()
    item.text=request.POST.get('item_text',)
    item.save()
    return render(request,'home.html',{
     'new_item_text':request.POST.get('item_text',''),
     })
=======
    if request.method == 'POST':
        new_item_text=request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    return render(request,'home.html')
>>>>>>> 826a76537cd9d84f25e92ce18a36a4ac1e6d8ff4
