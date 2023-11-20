from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView #追加
from django.db import connection #追加

#list
def index(request):
    sqltext="""SELECT
        a.id
      , a.empid
      , a.empname
      , a.deptid
      , a.mailaddress 
      , b.deptname
    FROM
      joinquery_employee AS a 
    INNER JOIN
      joinquery_department AS b
      on a.deptid=b.deptid
    ORDER BY
      a.id
        ;  """
    emplist=exec_query(sqltext);
    return render(request, 'joinquery/index.html', {'emplist':emplist})

def exec_query(sql_txt):
#   cursor.descriptionでフィールド名を配列にセットして、resultsにフィールド名を付加
    with connection.cursor() as c:
        c.execute(sql_txt)
        results = c.fetchall()
        columns=[]
        for field in c.description:
            columns.append(field[0])
        values=[]
        for result in results:
            value_dic={}
            for index,field in enumerate(columns):
                value_dic[field]=result[index]
            values.append(value_dic)
        return values
