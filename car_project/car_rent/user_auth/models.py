from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=30,validators=
                            [MinLengthValidator(limit_value=3, message='Name must be more than 3 char'),
                             RegexValidator(regex=r'^[a-zA-Z]+(\s[a-zA-Z]+)?$',message='Name accepts alphabets only')
                            ])
    
    email= models.EmailField(unique=True)
    password = models.TextField(validators=[MinLengthValidator(limit_value=6,message="Password must be between 6 to 15 char")])
   
    # username =None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):

        return self.name
   
        
 


