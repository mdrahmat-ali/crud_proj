from django.shortcuts import render
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.shortcuts import redirect

def retrieve_view(request):
    employees=Employee.objects.all()
    return render(request, 'index.html',{'employees':employees})

def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'create.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html',{'employee':employee})

    
