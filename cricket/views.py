


from django.shortcuts import render
from .models import player,filedatacheck,userprofile,dataset,validfiles,sha256hash,sha1hash,md5hash

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

#
# def viewfiles(request):
#     data=validfiles.objects.get(id=5)
#     paths=[]
#
#     print(data.myfile.path)
#     return render(request,'viewfiles.html')

def viewfiles(request):
    data=validfiles.objects.all()
    paths=[]
    names=[]
    name_clean=[]
    for idx,item in enumerate(data):
        paths.append(item.myfile.url)
        names.append((item.myfile.name))
    for idx,item in enumerate(names):
        name_clean.append(item.split('/')[-1])
    print(len(paths))
    print(len(name_clean))
    context={}
    data1=list(tuple(zip(paths,name_clean)))
    context['data']=data1

    return render(request,'viewfiles.html',context=context)

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
            context={}
            context['user']=username
            from datetime import datetime
            context['date']=datetime.today().strftime('%Y-%m-%d')
            return render(request, 'uploadfile.html',context)
        else:
            return render(request, 'index.html')


def sha256(request):
    print("sha256")
    if request.method=="POST":
        store=request.FILES['file']
        records=sha256hash.objects.all()

        myfile = request.FILES['file'].read()

        obj = dataset(myfile=store)
        obj.save()

        import hashlib
        h = hashlib.sha256()  # Construct a hash object using our selected hashing algorithm
        h.update(myfile)
        digest=h.hexdigest()
        sharecord = sha256hash(value=digest)
        sharecord.save()
        hashes=[]
        records = sha256hash.objects.values()
        for item in records:
            hashes.append(item['value'])

        ctr=0

        for item in hashes:
            if item==digest:
                ctr=ctr+1

        if ctr==1:
            v = validfiles(myfile=store)
            v.save()
            return render(request, 'file_success.html')
        else:
            return render(request, 'file_failure.html')







def sha1(request):
    if request.method == "POST":
        store = request.FILES['file']

        records = sha1hash.objects.all()

        myfile = request.FILES['file'].read()

        obj = dataset(myfile=store)
        obj.save()

        import hashlib
        h = hashlib.sha1()  # Construct a hash object using our selected hashing algorithm
        h.update(myfile)
        digest = h.hexdigest()
        sharecord = sha1hash(value=digest)
        sharecord.save()
        hashes = []
        records = sha1hash.objects.values()
        for item in records:
            hashes.append(item['value'])

        ctr = 0

        for item in hashes:
            if item == digest:
                ctr = ctr + 1

        if ctr == 1:
            v = validfiles(myfile=store)
            v.save()
            return render(request, 'file_success.html')
        else:
            return render(request, 'file_failure.html')


def md5(request):
    print("sha256")
    if request.method == "POST":
        store = request.FILES['file']
        records = md5hash.objects.all()
        myfile = request.FILES['file'].read()
        obj = dataset(myfile=store)
        obj.save()
        import hashlib
        h = hashlib.md5()  # Construct a hash object using our selected hashing algorithm
        h.update(myfile)
        digest = h.hexdigest()
        sharecord = md5hash(value=digest)
        sharecord.save()
        hashes = []
        records = md5hash.objects.values()
        for item in records:
            hashes.append(item['value'])

        ctr = 0

        for item in hashes:
            if item == digest:
                ctr = ctr + 1

        if ctr == 1:
            v = validfiles(myfile=store)
            v.save()
            return render(request, 'file_success.html')
        else:
            return render(request, 'file_failure.html')










