from django import forms
from .models import Transcation,review


class TranscationForm(forms.ModelForm):
    class Meta:
        model = Transcation
        fields = ["amount", "transaction_type"]

    def __init__(self, *args, **kwargs):
        self.user_account = kwargs.pop("account")  
        super().__init__(*args, **kwargs)
        self.fields["transaction_type"].disabled = True  #
        self.fields[
            "transaction_type"
        ].widget = forms.HiddenInput()  

    def save(self, commit=True):
        self.instance.account = self.user_account
        self.instance.balance_after_transaction = self.user_account.balance
        return super().save()

class DepositForm(TranscationForm):
    def clean_amount(self): 
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') 
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount



#----------------------- review --------------------->

class reviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ['comment']

