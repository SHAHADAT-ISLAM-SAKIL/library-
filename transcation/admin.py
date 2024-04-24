from django.contrib import admin
from .models import Transcation,BorrowedBookModel,review
# Register your models here.

admin.site.register(Transcation)
admin.site.register(BorrowedBookModel)
admin.site.register(review)
