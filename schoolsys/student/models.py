from django.db import models

# Create your models here.
class studentModel(models.Model):
    first_name=models.CharField(max_length=100,verbose_name='name')
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(verbose_name='age')
    gaurdian_name=models.CharField(max_length=100)
    total_marks=models.IntegerField(verbose_name='mark',null=True
                                    )
    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        db_table='student table'
           