
from django.contrib import admin
from .models import player,filedatacheck,userprofile,sha1hash,sha256hash,md5hash,filedata

# Register your models here.



admin.site.register(userprofile)
admin.site.register(filedata)
admin.site.register(sha256hash)
admin.site.register(sha1hash)
admin.site.register(md5hash)
