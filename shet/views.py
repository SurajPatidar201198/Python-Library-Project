import csv,io
from django.shortcuts import render,redirect
from .forms import ProductForm,ProductFormCol
from .models import ProductLink
from plotmygsheet import *
list1=[]
linklist=[]

def columns(request):
    if(request.method=="GET"):
        form1 = ProductFormCol()
        return render(request,"shet/Axis.html",{'form':form1,'list1':list1})
    else:
        form1 = ProductFormCol(request.POST)
        link=str(linklist[0])
        column1=request.POST['col1']
        column2=request.POST['col2']
        plot_graph(link,column1,column2)
        return render(request,"shet/plot.html")


def product_form(request,id=0):
    if request.method == "GET":
        form = ProductForm()
        return render(request,"shet/link.html",{'form':form})
    else:
        form = ProductForm(request.POST)
        link=request.POST['link']
        list1[:]=get_all_columns(str(link))
        linklist.append(link)
        # print(list1)
        return  redirect('/columns')
        