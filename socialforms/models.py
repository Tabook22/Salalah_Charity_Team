from django.db import models

# Create your models here.

class FamilyDesc(models.Model):
    regdt=models.DateTimeField(auto_now_add=True)
    gov=models.CharField(verbose_name="المحافظة", max_length=50,null=True, blank=True)
    wly=models.CharField(verbose_name="الولاية", max_length=50, null=True, blank=True)
    vill=models.CharField(verbose_name="القرية",max_length=50, null=True, blank=True)
    stre=models.CharField(verbose_name="الشارع", max_length=50, null=True, blank=True)
    ftype=models.CharField(verbose_name="فئة الأسرة", max_length=50,null=True, blank=True)
    hasname=models.CharField(verbose_name="إسم الزوج", max_length=300,null=True, blank=True)
    hasnat=models.CharField(verbose_name="جنسية الزوج", max_length=50,null=True, blank=True)
    hasid=models.CharField(verbose_name="الرقم المدني", max_length=50,null=True, blank=True)
    hasmobile=models.CharField(verbose_name="هاتف الزوج", max_length=50,null=True, blank=True)
    hasstatus=models.CharField(verbose_name="حالة الزوج", max_length=50, null=True)
    hasstatus_others=models.CharField(verbose_name="أخري", max_length=500, null=True)
    wfname=models.CharField(verbose_name="إسم الزوجة", max_length=300,null=True, blank=True)
    wfnat=models.CharField(verbose_name="جنسية الزوجة", max_length=50,null=True, blank=True)
    wfid=models.CharField(verbose_name="الرقم المدني", max_length=300,null=True, blank=True)
    wfmobile=models.CharField(verbose_name="رقم الهاتف", max_length=300,null=True, blank=True)
    wfstatus=models.CharField(verbose_name="حالة الزوجة", max_length=300,null=True, blank=True)
    wfstatus_others=models.CharField(verbose_name="أخرى", max_length=500, null=True)
    orph=models.CharField(verbose_name="إسم ولي أمر الأيتام أو الوكيل", max_length=300, null=True)
    orph_id=models.CharField(verbose_name="الرقم المدني", max_length=50, null=True)
    orph_rel=models.CharField(verbose_name="صلة القرابة", max_length=50, null=True)
    orphmobile=models.CharField(verbose_name="رقم الهاتف", max_length=50, null=True)
    
    def __str__(self):
        return self.hasname

class FamilyMember(models.Model):
    inhouse_no=models.IntegerField(verbose_name="أخريعدد أفراد الأسرة المقيمين بالمنزل بصفة دائمة",  null=True, blank=True)
    above18=models.IntegerField(verbose_name="عدد الأبناء فوق سن ١٨ سنة",null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الإبتدائي", null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الإعدادي",  null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الثانوي", null=True,blank=True)
    study_elm=models.IntegerField(verbose_name="عدد الطلبة في الجامعي",  null=True,blank=True)

class FamilyMemberDetail(models.Model):
    fullname=models.CharField(verbose_name="الأسم الثلاثي و القبيلة", max_length=300,null=True, blank=True)
    rel=models.CharField(verbose_name="صلة القرابة", max_length=300,null=True, blank=True)
    familystatus=models.CharField(verbose_name="الحالة الإجتماعية", max_length=300,null=True, blank=True)
    dateofbirth=models.CharField(verbose_name="سنة الميلاد", max_length=300,null=True, blank=True)
    education=models.CharField(verbose_name="المرحلة الدراسية", max_length=300,null=True, blank=True)
    job=models.CharField(verbose_name="الوظيفة", max_length=300,null=True, blank=True)
    jobplace=models.CharField(verbose_name="جهة العمل", max_length=300,null=True, blank=True)
    montlyicom=models.CharField(verbose_name="مبلغ الدخل الشهري", max_length=300,null=True, blank=True)
    loan=models.CharField(verbose_name="مبلغ القرض", max_length=300,null=True, blank=True)
    installment=models.CharField(verbose_name="مبلغ القسط الشهري", max_length=300,null=True, blank=True)
    loandesc=models.CharField(verbose_name="سبب القرض", max_length=500,null=True, blank=True)
    healthstatus=models.CharField(verbose_name="إسم الحالة الصحية", max_length=500,null=True, blank=True)

class FamilyIncome(models.Model):
    mainIncom=models.DecimalField(verbose_name="مبلغ الراتب",max_digits=6, decimal_places=2)
    retirIncom=models.DecimalField(verbose_name="مبلغ التقاعد",max_digits=6, decimal_places=2)
    insuIncom=models.DecimalField(verbose_name="الضمان",max_digits=6, decimal_places=2)
    sctIncom=models.DecimalField(verbose_name="مبلغ فريق صلالة الخيري",max_digits=6, decimal_places=2)
    othersIncom=models.DecimalField(verbose_name="مبالغ أخرى",max_digits=6, decimal_places=2)

class FamilyHouse(models.Model):
    housetype=models.CharField(verbose_name="نوع السكن", max_length=50,null=True, blank=True)
    houseothers=models.CharField(verbose_name="أخرى", max_length=50,null=True, blank=True)
    houseontype=models.CharField(verbose_name="نوع حيازة السكن", max_length=50,null=True, blank=True)
    houseroom_n=models.IntegerField(verbose_name="عددالغرف",null=True,blank=True)
    housersetting_n=models.IntegerField(verbose_name="عددالمجالس",null=True,blank=True)
    housekitten_n=models.IntegerField(verbose_name="عددالمطابخ", null=True,blank=True)
    housebath_n=models.IntegerField(verbose_name="عددالحمامات", null=True,blank=True)
    houserent_t=models.DecimalField(verbose_name="مبالغ الإيجار الشهري",max_digits=6, decimal_places=2)
    houserent_r=models.DecimalField(verbose_name="المتبقي من الإيجار الشهري",max_digits=6, decimal_places=2)
    houseelec_r=models.DecimalField(verbose_name="مبالغ فاتورة الكهرباء",max_digits=6, decimal_places=2)
    housewater_r=models.DecimalField(verbose_name="مبالغ فاتورةالمياة",max_digits=6, decimal_places=2)

class FamilyAssit(models.Model):
    assit_private_cars=models.IntegerField(verbose_name="السيارات الخاصة", null=True,blank=True)
    assit_taxi=models.IntegerField(verbose_name="تاكسي",  null=True,blank=True)
    assit_school_bus=models.IntegerField(verbose_name="حافلات المدرسة", null=True,blank=True)
    assit_gaz_car=models.IntegerField(verbose_name="سيارات الغاز",  null=True,blank=True)
    assit_others=models.CharField(verbose_name="أخرى", max_length=500, null=True)


class Familyloan(models.Model):
    loantype=models.IntegerField(verbose_name="نوع القرض",  null=True,blank=True)
    nameloner=models.DecimalField(verbose_name="إسم الجهة المناعة للقرض أو التمويل",max_digits=6, decimal_places=2)
    totalloan=models.DecimalField(verbose_name="مبلغ القرض",max_digits=6, decimal_places=2)
    instllament=models.DecimalField(verbose_name="القسط الشهري",max_digits=6, decimal_places=2)
    balanc=models.DecimalField(verbose_name="المبلغ المتبقي",max_digits=6, decimal_places=2)
