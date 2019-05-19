from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import ArticleColumn
from .forms import ArticleColumnForm

# Create your views here.


@login_required(login_url='/account/login')
@csrf_exempt
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, "article/column/article_column.html", {"columns": columns, "column_form": column_form})

    if request.method == 'POST':
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)

        if columns:
            # 栏目已经存在
            return HttpResponse("invalid")
        else:
            # 创建栏目成功
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("success")


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def rename_article_column(request):
    # print(request.POST)
    column_name = request.POST["column_name"]
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse("success")
    except:
        return HttpResponse("failed")


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("success")
    except:
        return HttpResponse("failed")
