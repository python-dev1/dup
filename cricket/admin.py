from django.contrib import admin
from .models import player,filedatacheck,userprofile,sha1hash,sha256hash,md5hash,filedata,dataset,validfiles

# Register your models here.



admin.site.register(userprofile)
admin.site.register(sha256hash)
admin.site.register(sha1hash)
admin.site.register(md5hash)
admin.site.register(dataset)
admin.site.register(validfiles)


