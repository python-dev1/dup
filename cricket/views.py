





from django.shortcuts import render
from .models import player,filedatacheck,userprofile,sha1hash,sha256hash,md5hash,filedata
import hashlib
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

def registration(request):
    return render(request,'registration.html')

def adduser(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        userdata=userprofile(name=name,username=username,email=email,password=password)
        userdata.save()
        context={}
        return render(request, 'index.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        flag=False
        u=[]
        p=[]
        records=list(userprofile.objects.values())
        for item in records:
            u.append(item['username'])
            p.append(item['password'])
        idx1=0
        for idx,item in enumerate(u):
            if username==item:
                idx1=idx

        if p[idx1]==password:
            flag=True
        else:
            flag=False

        if flag==True:
            return render(request, 'uploadfile.html')
        else:
            return render(request, 'index.html')


def sha256(request):
    print("sha256")
    if request.method=="POST":
        hashes=[]
        records = list(sha256hash.objects.values())
        for item in records:
            hashes.append(item['value'])
        print(hashes)


        myfile = request.FILES['file'].read()
        h = hashlib.sha256()  # Construct a hash object using our selected hashing algorithm
        h.update(myfile)
        hash_value=h.hexdigest()
        if hash_value in hashes:
            print("File can not be inserted since it already exist in the database")
            return render(request, 'file_failure.html')
        else:
            datas=sha256hash(value=hash_value)
            datas.save()
            print("File is uploaded in the database successfully")
            x=filedata(myfile=myfile)
            x.save()
            return render(request, 'file_success.html')




# def sha256(request):
#     print("sha256")
#     if request.method=="POST":
#         myfile=request.FILES['file'].read()
#         print(type(myfile))
#         print(myfile)
#         data1=myfile.decode(encoding="utf-8")
#         print(type(data1))
#         h = hashlib.sha256()
#         h.update(data1.encode('utf-8'))
#         hashvalue=h.hexdigest()
#         print(hashvalue)
#
#         return render(request, 'index.html')

def sha1(request):
    if request.method == "POST":
        hashes = []
        records = list(sha1hash.objects.values())
        for item in records:
            hashes.append(item['value'])
        print(hashes)

        myfile = request.FILES['file'].read()
        h = hashlib.sha1()  # Construct a hash object using our selected hashing algorithm
        h.update(myfile)
        hash_value = h.hexdigest()
        if hash_value in hashes:
            print("File can not be inserted since it already exist in the database")
            return render(request, 'file_failure.html')
        else:
            datas = sha1hash(value=hash_value)
            datas.save()
            print("File is uploaded in the database successfully")
            x = filedata(myfile=myfile)
            x.save()
            return render(request, 'file_success.html')

def md5(request):
    if request.method == "POST":
        hashes = []
        records = list(md5hash.objects.values())
        for item in records:
            hashes.append(item['value'])
        print(hashes)

        myfile = request.FILES['file'].read()
        h = hashlib.md5()  # Construct a hash object using our selected hashing algorithm
        h.update(myfile)
        hash_value = h.hexdigest()
        if hash_value in hashes:
            print("File can not be inserted since it already exist in the database")
            return render(request, 'file_failure.html')
        else:
            datas = md5hash(value=hash_value)
            datas.save()
            print("File is uploaded in the database successfully")
            x = filedata(myfile=myfile)
            x.save()
            return render(request, 'file_success.html')








