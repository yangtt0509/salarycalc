from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from employees.models import Employee


def index(request):
    context = {
        'employees': Employee.objects.filter(available=True).order_by('-id'),
        'msg': request.GET['msg'] if 'msg' in request.GET else ''
    }
    return render(request, 'employee_index.html', context=context)


def delete(request, id):
    employee = Employee.objects.filter(id=id).first()
    if employee:
        employee.available = False
        employee.save()
        msg = '{} 删除成功'.format(employee.name)
    else:
        msg = '员工不存在'
    return HttpResponseRedirect('/employees?msg={}'.format(msg))


def create(request):
    print(request.method)
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        employee = Employee.objects.filter(name=employee_name).first()
        if employee:
            employee.available = True
            employee.save()
            msg = '已经存在该员工'
        else:
            Employee.objects.create(name=employee_name)
            msg = '创建成功'
        return HttpResponseRedirect('/employees?msg={}'.format(msg))
    elif request.method == 'GET':
        return render(request, 'employee_create.html')
