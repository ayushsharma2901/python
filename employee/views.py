from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required, permission_required
from .forms import EmployeeForm,RegisterForm,RegisterGroup,EditGroup
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model



def employees_list(request):
    # employees = Employee.objects.all()

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    employees = Employee.objects.filter(
        Q(emp_name__icontains=search_query) | 
        Q(emp_role__icontains=search_query) |
        Q(emp_salary__icontains=search_query)
    )


    context = {
        'employees': employees,
        'search_query': search_query,
    }
    return render(request, 'employee/list.html', context)


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)

def user_list(request):
    # employees = Employee.objects.all()
    

    User = get_user_model()
    users = User.objects.all()
    context = {
        'users': users,
        
    }
    return render(request, 'employee/userlist.html', context)

def create_user(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user-list')
        
    context = {
        'form': form,
    }
    return render(request, 'employee/usercreate.html', context)


def edit_user(request, pk):
    User = get_user_model()
    users = User.objects.get(id=pk)

    form = RegisterForm(instance=users)

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
            return redirect('user-list')

    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'employee/useredit.html', context)

def delete_user(request, pk):
    User = get_user_model()
    users = User.objects.get(id=pk)
    if request.method == 'POST':
        users.delete()
        return redirect('user-list')

    context = {
        'users': users,
    }
    return render(request, 'employee/userdelete.html', context)

def group_list(request):
    # employees = Employee.objects.all()
    #Groups = get_user_model()
    #users = User.objects.all()
    groups=Group.objects.all()
    context = {
        'groups': groups,
        
    }
    return render(request, 'employee/grouplist.html', context)

def create_group(request):
    form = RegisterGroup()

    if request.method == 'POST':
        form = RegisterGroup(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('group-list')
        
    context = {
        'form': form,
    }
    return render(request, 'employee/groupcreate.html', context)


def edit_group(request, pk):
    #User = get_user_model()
    #allusers = User.objects.all()
    groups=Group.objects.get(id=pk)
    users = groups.user_set.all()
    form = EditGroup(instance=groups)

    if request.method == 'POST':
        form = EditGroup(request.POST, request.FILES, instance=groups)
        if form.is_valid():
            user=request.POST.get('Users')
            groups.user_set.add(user)
            form.save()
            return redirect('group-list')

    context = {
        
        'users':users,
        'groups': groups,
        'form': form,
    }
    return render(request, 'employee/groupedit.html', context)

def delete_group(request, pk):
   #User = get_user_model()
    #users = User.objects.get(id=pk)
    groups=Group.objects.get(id=pk)
    if request.method == 'POST':
        groups.delete()
        return redirect('group-list')

    context = {
        'groups': groups,
    }
    return render(request, 'employee/groupdelete.html', context)


def user_edit_group(request, pk):
    User = get_user_model()
    users = User.objects.get(id=pk)
    #groups=Group.objects.get(id=pk2)
    #groups.user_set.remove(users)

    users.groups.clear()
    
    return redirect('group-list')

