from django.contrib import admin
from app.models import EmployeeListing, Employee, WorkSkill,PointOfInterest, PeopleWeKnow, Book

# Register your models here.
admin.site.register(EmployeeListing)
admin.site.register(Employee)
admin.site.register(WorkSkill)
admin.site.register(PointOfInterest)
admin.site.register(PeopleWeKnow)
admin.site.register(Book)
