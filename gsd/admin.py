from django.contrib import admin
from .models import User, Task



#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'email')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'creation', 'deadline', 'importance' )


