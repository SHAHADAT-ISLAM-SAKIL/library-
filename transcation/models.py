from django.db import models
from .constant import TRANSACTION_TYPE
from user_account.models import Useraccount
from django.contrib.auth.models import User
from post.models import PostModel


# ---------------------- Transaction here ---------------------->
class Transcation(models.Model):
    account = models.ForeignKey(
        Useraccount, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)


class BorrowedBookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)


class review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()