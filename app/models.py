from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=10)

class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=1000)
    age = models.CharField(max_length=3)
    phone = models.BigIntegerField()
    photo = models.FileField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)





class complaint_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=1000)
    date=models.DateField()
    reply=models.CharField(max_length=1000,default='pending')

class feedback_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=1000)
    rating=models.IntegerField()
    date=models.DateField()

class code_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    language = models.CharField(max_length=10)
    topic = models.CharField(max_length=500)
    code = models.TextField()
    date = models.DateField()


class sample_programs(models.Model):
    Language=models.CharField(max_length=10)
    topic=models.CharField(max_length=500)
    code=models.CharField(max_length=5000)
    date=models.DateField()

class group_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    grpName=models.CharField(max_length=100)
    date=models.DateField()
    Detail=models.CharField(max_length=1000)
    photo=models.FileField()
#       
class group_members_table(models.Model):
    GROUP=models.ForeignKey(group_table, on_delete=models.CASCADE)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    date=models.DateField()
    type=models.CharField(max_length=100)

class share_table(models.Model):
    FROMUSER = models.ForeignKey(user_table, on_delete=models.CASCADE,related_name='fromuser')
    TOUSER = models.ForeignKey(user_table, on_delete=models.CASCADE,related_name='touser')
    Language=models.CharField(max_length=10)
    topic=models.CharField(max_length=1000)
    code=models.CharField(max_length=5000)
    date=models.DateField()
    status=models.CharField(max_length=10)

class share_group_table(models.Model):
    GROUP = models.ForeignKey(group_table, on_delete=models.CASCADE)
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    Language=models.CharField(max_length=10)
    topic=models.CharField(max_length=1000)
    code=models.CharField(max_length=5000)
    type=models.CharField(max_length=10)
    date=models.DateField()
