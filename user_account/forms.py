from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Useraccount, UserAddress
from django import forms
from .constant import GENDER_TYPE


# --------------------- Register Form Creation Now ----------------------->


class UserSingUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    post_code = forms.IntegerField()
    city = forms.CharField(max_length=200)
    current_address = forms.CharField(max_length=200)
    ccuntry = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "gender",
            "post_code",
            "city",
            "ccuntry",
            "current_address",
        ]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            gender = self.cleaned_data.get("gender")
            post_code = self.cleaned_data.get("post_code")
            city = self.cleaned_data.get("city")
            ccuntry = self.cleaned_data.get("ccuntry")
            current_address = self.cleaned_data.get("current_address")

            Useraccount.objects.create(
                user=our_user,
                gender=gender,
            )
            UserAddress.objects.create(
                user=our_user,
                post_code=post_code,
                city=city,
                ccuntry=ccuntry,
                current_address=current_address,
            )
        return our_user

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "w-100 shadow-sm form-control"}
            )


class UpdateUser(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    post_code = forms.IntegerField()
    city = forms.CharField(max_length=200)
    current_address = forms.CharField(max_length=200)
    ccuntry = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "w-100 shadow-sm form-control"}
            )

        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except:
                if Useraccount.DoesNotExist:
                    user_account = None
                    user_address = None

            if user_account:
                self.fields["gender"].initial = user_account.gender

                self.fields["current_address"].initial = user_address.current_address
                self.fields["city"].initial = user_address.city
                self.fields["post_code"].initial = user_address.post_code
                self.fields["ccuntry"].initial = user_address.ccuntry

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            user_account, created = Useraccount.objects.get_or_create(user=user)

            user_address, created = UserAddress.objects.get_or_create(user=user)

            user_account.gender = self.cleaned_data["gender"]
            user_account.save()
            user_address.post_code = self.cleaned_data["post_code"]
            user_address.city = self.cleaned_data["city"]
            user_address.ccuntry = self.cleaned_data["ccuntry"]
            user_address.current_address = self.cleaned_data["current_address"]
            user_address.save()
        return user
