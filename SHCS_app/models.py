from django.db import models


class Requests(models.Model):
    r_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)

class Users(models.Model):
    r_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)

class Selling(models.Model):
    idd_s=models.IntegerField(primary_key=True)
    r_id1=models.CharField(max_length=255)
    Name=models.CharField(max_length=255)
    Ptype=models.CharField(max_length=255)
    Prop_id=models.CharField(max_length=255)
    details=models.CharField(max_length=255)
    image=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    amount=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    hash1=models.CharField(max_length=255)

class Transaction(models.Model):
    r_id1=models.IntegerField(primary_key=True)
    SName=models.CharField(max_length=255)
    Saddr=models.CharField(max_length=255)
    RName=models.CharField(max_length=255)
    Raddr=models.CharField(max_length=255)
    P_id=models.CharField(max_length=255)
    Amount=models.CharField(max_length=255)
    T_hash=models.CharField(max_length=255)

class Buyed(models.Model):
    r_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    p_id=models.CharField(max_length=255)
    hash1=models.CharField(max_length=255)    
    p_type=models.CharField(max_length=255) 
    im=models.CharField(max_length=255) 
    details=models.CharField(max_length=255) 
    phone=models.CharField(max_length=255) 

class Buyed_tk(models.Model):
    r_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    p_id=models.CharField(max_length=255)
    tk_name=models.CharField(max_length=255)
    hash1=models.CharField(max_length=255)    
    p_type=models.CharField(max_length=255) 
    im=models.CharField(max_length=255) 
    details=models.CharField(max_length=255) 
    amnt=models.CharField(max_length=255) 
    phone=models.CharField(max_length=255)
    tok_co=models.CharField(max_length=255)

class Token(models.Model):
    idd_t=models.IntegerField(primary_key=True)
    r_id1=models.CharField(max_length=255)
    Name=models.CharField(max_length=255)
    Ptype=models.CharField(max_length=255)
    Prop_id=models.CharField(max_length=255)
    details=models.CharField(max_length=255)
    tkname=models.CharField(max_length=255)
    image=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    amount=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    token_count=models.CharField(max_length=255)
    Cuholder=models.CharField(max_length=255)
    hashh=models.CharField(max_length=255)
    Button=models.CharField(max_length=255)