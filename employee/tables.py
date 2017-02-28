import django_tables2 as tables
from django_tables2.utils import A

from employee.filters import EmployeeFilter
from .models import Employee


class EmployeeTable(tables.Table):
    id = tables.Column()
    get_full_name = tables.LinkColumn('employee:detail', kwargs={"employee_id": A('id')},\
                                      order_by=('last_name'), verbose_name='Name')
    email = tables.Column()
    get_role = tables.Column(verbose_name='Role')
    date_joined = tables.DateColumn(attrs={'td': {'align': 'center', 'width': '10%'}})
    is_active = tables.BooleanColumn(attrs={'th': {'style': 'text-align: center'},
                                            'td': {'align': 'center', 'width': '10%'}},
                                     verbose_name='In action')
    online_status = tables.Column(verbose_name='Activity')

    class Meta:
        model = Employee
        attrs = {"class": "table table-bordered table-striped table-hover"}
        exclude = ('id')
        fields = ['get_full_name', 'email', 'get_role', 'online_status', 'is_active', 'date_joined']

