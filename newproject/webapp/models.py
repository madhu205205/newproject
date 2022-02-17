from django.db import models


# Create your models here.
class College(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField(blank=True, null=True)
   code = models.IntegerField(blank=True, null=True)
   phone = models.IntegerField(blank=True, null=True)
   address = models.TextField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
       verbose_name_plural = "Colleges"

   def __str__(self):
       return "College Name " + str(self.name)

class Branch(models.Model):
   clg_name = models.ForeignKey(College, on_delete=models.CASCADE)
   name = models.CharField(max_length=50, null=True, blank=True)
   email = models.EmailField(blank=True, null=True)
   head = models.CharField(max_length=50, null=True, blank=True)
   phone = models.IntegerField(null=True, blank=True)
   total_staff = models.IntegerField(null=True, blank=True)
   address = models.TextField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
       verbose_name_plural = "Branches"

   def __str__(self):
       return "Branch Name:" + str(self.name) + " College name:" + str(self.clg_name.name)