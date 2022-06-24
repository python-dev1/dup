from django.shortcuts import render
from .models import player,filedatacheck

# Create your views here.

import hashlib

def hash_file_sha1(filename):

   h = hashlib.sha1()

   with open(filename,'rb') as file:

       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()


def hash_file_sha256(filename):
    h = hashlib.sha256()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()

def hash_file_sha_md5(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()

def index(request):
    return render(request,'index.html')

def getdata(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']

        player1=player(name=name,age=age)
        player1.save()
    return render(request,'getdata.html')

def uploaddata(request):
    p=player.objects.all()
    context={}
    context['data']=p
    return render(request,'uploaddata.html',context=context)

def getfile(request):
    if request.method=='POST':
        file=request.FILES['records']
        mdata=''
        mdata = file.read().replace('\n', '')
        result = hashlib.md5(bytes(mdata)).hexdigest()
        print(result)


        file1=filedatacheck(myfile=file,md5="ali",sha1="shaa",sha256="bilal")
        file1.save()
    return render(request,'getfile.html')

def uploadfile(request):
    return render(request,'uploadfile.html')

