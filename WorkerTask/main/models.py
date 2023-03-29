import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404

from django.db import models


class Bosses(models.Model):
    Boss_id = models.AutoField(primary_key=True)
    Boss_name = models.TextField("ПІБ")
    Department = models.TextField("Підрозділ")
    Boss_level = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(7)
    ])


# Create your models here.
class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.TextField("ПІБ")
    position = models.TextField("Посада")
    Employment_date = models.DateField(default=datetime.date.today())
    email = models.EmailField(null=False, blank=False, unique=True)
    Boss = models.ForeignKey(Bosses, on_delete=models.PROTECT)


def random_mail():
    import random
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    email = ""
    for i in range(15):
        email += random.choice(alphabet)
    email += "@gmail.com"
    return email


def db_seeder():
    import random
    first_name = ["Олена", "Нікіта", "Віталій", "Сергій", "Андрій", "Ярослав"]
    last_name = ["Кравцов", "Савчук", "Іванченко", "Фіщук", "Краснобок", "Корнатовчський", "Горошко", "Харченко",
                 "Юхимчук"]
    father_name = ["Андрійович(ївна)", "Олегович(івна)", "Сергійович(ївна)", "Олегович(івна)"]
    position = ["Office manager", "Seller", "SMM", "Software Dev", "HR", "Recruiter"]
    boss_positions = ["CEO", "CTO", "CFO", "COO", "CIO", "CSO", "CISO"]
    bosses = []
    for i in range(7):
        boss = Bosses()
        boss.Boss_level = i
        boss.Boss_name = f"{random.choice(first_name)} {random.choice(last_name)} {random.choice(father_name)}"
        boss.Department = boss_positions[i]
        boss.save()
        if i != 0:
            bosses.append(boss)

    for i in range(50000):
        emp = Employees()
        emp.Boss = random.choice(bosses)
        emp.position = random.choice(position)
        while True:
            email = random_mail()
            if (len(list(Employees.objects.all().filter(email=email))) == 0):
                emp.email = random_mail()
                break
        emp.Employment_date = datetime.date.today() - datetime.timedelta(days=random.randint(-100, -10))
        emp.full_name = f"{random.choice(first_name)} {random.choice(last_name)} {random.choice(father_name)}"
        emp.save()


def get_worker_by_boss(boss):
    return list(Employees.objects.all().filter(Boss=boss))


def get_all_bosses():
    bosses = list(Bosses.objects.all())
    bosses.pop(0)
    return bosses


def get_worker_by_boss_id(id):
    boss = get_object_or_404(Bosses, Boss_id=id)
    return convert_to_dictionary(list(Employees.objects.all().filter(Boss=boss)))


def convert_to_dictionary(list_object):
    list_dict = []
    for i in list_object:
        temp = {
            "employee_id": i.employee_id,
            "full_name": i.full_name,
            "position": i.position,
            "Employment_date": i.Employment_date,
            "email": i.email,
        }
        list_dict.append(temp)
    return list_dict


def get_all_workers():
    return list(Employees.objects.all())
