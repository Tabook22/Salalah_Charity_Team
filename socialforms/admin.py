from django.contrib import admin
from .models import Family, FamilyAssit, FamilyAttch, FamilyHouse, FamilyIncome, FamilyLoan, FamilyMember, FamilyMemberDetail, FamilyNeeds, FamilyReport

# Register your models here.
admin.site.register(Family)
admin.site.register(FamilyAssit)
admin.site.register(FamilyAttch)
admin.site.register(FamilyHouse)
admin.site.register(FamilyIncome)
admin.site.register(FamilyLoan)
admin.site.register(FamilyMember)
admin.site.register(FamilyMemberDetail)
admin.site.register(FamilyNeeds)
admin.site.register(FamilyReport)
