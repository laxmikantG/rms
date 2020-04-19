from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse

from core.models import Table, Menu, MenuDetail, Orders, OrderedMenu
# Create your views here.


def to_reqdict(request):
    reqdict = {}
    if request.method == 'POST':
      reqdict = dict(zip(request.POST.keys(), request.POST.values()))
    else:
      reqdict = dict(zip(request.GET.keys(), request.GET.values()))
    reqdict.pop('csrfmiddlewaretoken', None)
    print({"message": reqdict})
    return reqdict

def home(request):
    tables = Table.objects.all()
    menu = Menu.objects.all()
    orders = Orders.objects.all()
    return render(request, "home1.html", {"tables": tables, "menu":menu, "orders": orders})


def add_table(request):
    if request.method == 'GET':
      return render(request, "add_table.html", {})
    if request.method == 'POST':
      reqdict = to_reqdict(request)
      name = reqdict.get('name')
      capacity = reqdict.get('capacity')
      print({"name": name, "capacity":capacity, 'c':all([name, capacity])})
      if all([name, capacity]):
        try:
          table = Table.objects.create(**reqdict)
          table.save()
          messages.success(request, f'Table created: {table.name}.')
        except Exception as e:
          messages.error(request, 'Could not create the table.')
        print({"Table created"})
      return render(request, "add_table.html", {})


def modify_table(request, table_id):
    reqdict = to_reqdict(request)
    if request.method == 'GET':
      try:
        table = Table.objects.get(id=table_id)
      except Exception as e:
        messages.error(request, f'Table can not be edited.')        
        print(e)
    if request.method== 'POST':
      try:
        table = Table.objects.get(id=table_id)
        table.name = reqdict.get('name', table.name)
        table.capacity = reqdict.get('capacity', table.name)
        table.save()
        messages.error(request, f'Table {table.name} edited.')        
      except Exception as e:
        messages.error(request, f'Table can not be edited.')        
        print(e)
    return render(request, "modify_table.html", {"table":table})
    

def remove_table(request, table_id):
    if request.method == 'GET':
      try:
        table = Table.objects.get(id=table_id)
        table.delete()
        messages.success(request, f'Table: {table.name} Removed.')        
      except Exception as e:
        messages.error(request, f'Table can not be Removed.')        
        print(e)
      return redirect(reverse('home'))




def add_menu(request):
  reqdict = to_reqdict(request)
  menu_types = MenuDetail.objects.all()
  if request.method=='GET':
    return render(request, 'add_menu.html', {"menu_types": menu_types})
  if request.method=='POST':
    try:
      menu = Menu()
      mtype = menu_types.get(id=reqdict.get('menu_type'))
      menu.name = reqdict.get('menu_name')
      menu.quantity = reqdict.get('quantity')
      menu.price = reqdict.get('price')
      menu.taste = reqdict.get('taste')
      menu.description = reqdict.get('description')
      menu.type = mtype
      menu.save()
      messages.success(request, f'Menu {menu.name} has been added')
    except Exception as e:
      messages.error(request, 'Failed to add Menu')
      print(e)
  return render(request, 'add_menu.html', {"menu_types": menu_types})

  
def edit_menu(request, menu_id):
  reqdict = to_reqdict(request)
  menu_types = MenuDetail.objects.all()
  menu = Menu.objects.get(id=menu_id)
  # if request.method=='GET':
  #   return render(request, 'edit_menu.html', {'menu_types':menu_types, 'menu': menu})
  if request.method=='POST':
    try:
      menu.name = reqdict.get('menu_name', menu.name)
      menu.type = menu_types.get(id=reqdict.get('menu_type'))
      menu.price = reqdict.get('price')
      menu.taste = reqdict.get('taste')
      menu.quantity = reqdict.get('quantity')
      menu.description = reqdict.get('description')
      menu.save()
      messages.success(request, f"Menu - {menu.name} has been modified ")
    except Exception as e:
      print(e)
      messages.error(request, f"Menu - {menu.name} could not update")
  return render(request, 'edit_menu.html', {'menu_types':menu_types, 'menu': menu})

def remove_menu(request, menu_id):
  try:
    m = Menu.objects.filter(id=menu_id)
    m.delete()
    messages.success(request, "Item has been removed")
  except Exception as e:
    messages.error(request, "Could not remove the item")
  return redirect(reverse('home'))




def get_order(request):
  if request.method=='POST':
    try:
      reqdict = to_reqdict(request)
      table_id = reqdict.get('table_id')
      menu_ids = reqdict.get('menu_ids'), 
      staff_id=None
      table = Table.objects.get(id=table_id)
      items = OrderedMenu.objects.filter(id__in=menu_ids)
      order = Orders()
      order.table = table 
      order.menu.add(items)
      order.save()
      messages.success(request, f'Order has been placed for {table.name}')
    except Exception as e:
      messages.error(request, 'Failed to add Menu')
      print(e)
  return redirect(reverse('home'))

def remove_orders(request, table_id, menu_id):
    if request.method=='POST':
      try:
        reqdict = to_reqdict(request)
        table_id = reqdict.get('table_id')
        menu_ids = reqdict.get('menu_ids'), 
        staff_id=None
        table = Table.objects.get(id=table_id)
        items = OrderedMenu.objects.filter(id__in=menu_ids)
        order = Orders()
        order.table = table 
        order.menu.add(items)
        order.save()
        messages.success(request, f'Order has been placed for {table.name}')
      except Exception as e:
        messages.error(request, 'Failed to add Menu')
        print(e)
    return redirect(reverse('home'))
