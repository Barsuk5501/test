from django.contrib import admin
from .models import MyUser
from .models import Admin
from .models import Post

admin.site.register(Admin)
admin.site.register(MyUser)
admin.site.register(Post)


