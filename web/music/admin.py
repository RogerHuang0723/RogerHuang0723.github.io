from django.contrib import admin

# Register your models here.
from .models import Member,board

admin.site.register(Member)
admin.site.register(board)