from django.db import models
import datetime


class lesson (models.Model):
    lesson = models.CharField('Предмет', max_length=250)
    lesson_type = models.CharField('Категория', max_length=250)
    def __str__(self):
        return self.lesson
    
class group (models.Model):
    group = models.CharField('Класс', max_length=250)
    group_type = models.CharField('Тип', max_length=250)
    group_number = models.IntegerField('Номер')
    def __str__(self):
        return self.group   

class weeklesson (models.Model):
    lessonday= models.CharField ('Учебный день',  max_length=250)
    lesson_1 = models.ForeignKey('lesson',related_name='Урок_1', on_delete=models.CASCADE)
    group_1 = models.ForeignKey ('group', related_name='Класс_1',on_delete=models.CASCADE, null=True)
    lesson_2 = models.ForeignKey('lesson',related_name='Урок_2', on_delete=models.CASCADE)
    group_2 = models.ForeignKey ('group', related_name='Класс_2',on_delete=models.CASCADE, null=True)
    lesson_3 = models.ForeignKey('lesson',related_name='Урок_3', on_delete=models.CASCADE)
    group_3 = models.ForeignKey ('group', related_name='Класс_3',on_delete=models.CASCADE, null=True)
    lesson_4 = models.ForeignKey('lesson',related_name='Урок_4', on_delete=models.CASCADE)
    group_4 = models.ForeignKey ('group', related_name='Класс_4',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.lessonday
    
class student (models.Model):
    student_id = models.IntegerField('ID', primary_key=True, unique=True)
    second_name = models.CharField('Фамилия', max_length=250)
    first_name = models.CharField('Имя', max_length=250)
    father_name = models.CharField('Отчество', max_length=250)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    birthday = models.DateField('Дата рождения')
    def __str__(self):
        return self.second_name   
    
class check (models.Model):
    date = models.DateField('Дата урока')
    student = models.ForeignKey(student, on_delete=models.CASCADE, default='')
    lesson = models.ForeignKey(lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    def __str__(self):
        return self.date  

class mark (models.Model):
    date = models.DateField('Дата урока')
    student = models.ManyToManyField(student)
    lesson = models.ForeignKey(lesson, on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    def __date__(self):
        return self.date  

class Attendence(models.Model):
    EmpId = models.IntegerField(verbose_name='EmpId')
    Name = models.ForeignKey(student, verbose_name='Name', on_delete=models.CASCADE, default='')
    lesson = models.ForeignKey(lesson, on_delete=models.CASCADE, default='')
    group = models.ForeignKey(group, on_delete=models.CASCADE, default='')
    choices = [('P','Present'),('A','Absent'),('O','Off')]
    
    Status = models.CharField(choices=choices,blank = False,max_length=10,verbose_name='Status')
    AttendenceOn = models.DateField(default = datetime.datetime.now())

    def __date__(self):
       return self.AttendenceOn

class homework (models.Model):
    student = models.CharField('Фамилия', max_length=250)
    homework = models.FileField(upload_to='uploads_model')
    lesson = models.ForeignKey(lesson, on_delete=models.CASCADE)
    def __str__(self):
        return self.student  
    
class marking (models.Model):
    student = models.ManyToManyField(homework)
    class Marks(models.IntegerChoices):
        AMAZING = 5
        GOOD = 4
        NORMAL = 3
        BAD = 2
    mark = models.IntegerField(choices=Marks)
    def __int__(self):
        return self.mark  