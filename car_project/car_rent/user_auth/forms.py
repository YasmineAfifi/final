from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        # user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['name','email','password']
        widgets ={
            'name':forms.TextInput(attrs={"class":"registerInputs",'placeholder': 'Your Full Name'}),
            'email':forms.EmailInput(attrs={'class':'registerInputs','placeholder': 'Email'}),
            'password':forms.PasswordInput(attrs={'class':'registerInputs','placeholder': 'Password'})
        }
        error_messages = {
            'name': {
                'required':"Name Is Required",
                'max_length':"Name must be less than 30 char"
            },
            'email':
            {   'required':'Email Is Required',
                'unique':'Email is already Exist'
            },'password':
            {
                'required':'Password Is Required',
                'max_length':'Password is more than 15 char'
            }
            
        }
            
   