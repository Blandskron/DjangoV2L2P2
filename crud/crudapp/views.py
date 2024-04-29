from django.shortcuts import render, redirect
from .models import Item, Vendedor
from .forms import ItemForm, VendedorForm

# CRUD ITEMS
def item_list(request):
    items = Item.objects.all()
    return render(request, 'crudapp/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'crudapp/item_form.html', {'form': form})

def item_update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'crudapp/item_form.html', {'form': form})

def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'crudapp/item_confirm_delete.html', {'item': item})


# CRUD VENDEDOR
def vendedor_list(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor/vendedor_list.html', {'vendedores': vendedores})

def vendedor_create(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedorForm()
    return render(request, 'vendedor/vendedor_form.html', {'form': form})

def vendedor_update(request, pk):
    item = Vendedor.objects.get(pk=pk)
    if request.method == 'POST':
        form = VendedorForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedorForm(instance=item)
    return render(request, 'vendedor/vendedor_form.html', {'form': form})

def vendedor_delete(request, pk):
    item = Vendedor.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('vendedor_list')
    return render(request, 'vendedor/vendedor_confirm_delete.html', {'item': item})
