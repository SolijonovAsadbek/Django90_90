import xlwt
from django.http import HttpResponse

# Create your views here.
from test_model_layer.models import Runner


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['name', 'medal']

    for colnum in range(len(columns)):
        ws.write(row_num, colnum, columns[colnum], font_style)

    font_style = xlwt.XFStyle()

    rows = Runner.objects.all().values_list('name', 'medal')

    for row in rows:
        row_num += 1
        for colnum in range(len(row)):
            ws.write(row_num, colnum, str(row[colnum]), font_style)
    wb.save(response)
    return response

    # return render(request, template_name='test_excel/excel.html')
