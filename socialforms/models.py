from django.db import models

# Create your models here.


class Family(models.Model):
    FAMILY_TYPE = [
        ('أيتام', 'أيتام'),
        ('دخل محدود', 'دخل محدود'),
        ('أسرة ضمانية', 'أسرة ضمانية'),
        ('عجز', 'عجز')
    ]

    HASBAND_STATUS = [
        ('عاطل', 'عاطل'),
        ('مسجون', 'مسجون'),
        ('عاجز', 'عاجز'),
        ('متوفي', 'متوفي')
    ]

    WIFE_STATUS = [
        ('ربة منزل', 'ربة منزل'),
        ('أرملة', 'أرملة'),
        ('هجر', 'هجر'),
        ('عجز', 'عجز'),
        ('مريضة', 'مريضة'),
        ('متوفاة', 'متوفاة'),
        ('مطلقة', 'مطلقة')
    ]

    regdt = models.DateTimeField(auto_now_add=True)
    gov = models.CharField(verbose_name="المحافظة",
                           max_length=50, null=True, blank=True)
    wly = models.CharField(verbose_name="الولاية",
                           max_length=50, null=True, blank=True)
    vill = models.CharField(verbose_name="القرية",
                            max_length=50, null=True, blank=True)
    stre = models.CharField(verbose_name="الشارع",
                            max_length=50, null=True, blank=True)
    ftype = models.CharField(verbose_name="فئة الأسرة", max_length=50,
                             choices=FAMILY_TYPE, default=FAMILY_TYPE[1][1],  null=True, blank=True)
    hasname = models.CharField(
        verbose_name="إسم الزوج", max_length=300, null=True, blank=True)
    hasnat = models.CharField(
        verbose_name="جنسية الزوج", max_length=50, null=True, blank=True)
    hasid = models.CharField(verbose_name="الرقم المدني",
                             max_length=50, null=True, blank=True)
    hasmobile = models.CharField(
        verbose_name="هاتف الزوج", max_length=50, null=True, blank=True)
    hasstatus = models.CharField(
        verbose_name="حالة الزوج", max_length=50, null=True)
    hasstatus_others = models.TextField(
        verbose_name="أخري", default=HASBAND_STATUS[1][1], null=True, blank=True)
    wfname = models.CharField(
        verbose_name="إسم الزوجة", max_length=300, null=True, blank=True)
    wfnat = models.CharField(verbose_name="جنسية الزوجة",
                             max_length=50, null=True, blank=True)
    wfid = models.CharField(verbose_name="الرقم المدني",
                            max_length=50, null=True, blank=True)
    wfmobile = models.CharField(
        verbose_name="رقم الهاتف", max_length=50, null=True, blank=True)
    wfstatus = models.CharField(verbose_name="حالة الزوجة", max_length=300,
                                choices=WIFE_STATUS, default=WIFE_STATUS[1][1], null=True, blank=True)
    wfstatus_others = models.TextField(verbose_name="أخرى", null=True)
    orph = models.CharField(
        verbose_name="إسم ولي أمر الأيتام أو الوكيل", max_length=300, null=True)
    orph_id = models.CharField(
        verbose_name="الرقم المدني", max_length=50, null=True)
    orph_rel = models.CharField(
        verbose_name="صلة القرابة", max_length=50, null=True)
    orphmobile = models.CharField(
        verbose_name="رقم الهاتف", max_length=50, null=True)

    def __str__(self):
        return self.hasname


class FamilyMember(models.Model):
    inhouse_no = models.IntegerField(
        verbose_name="عدد أفراد الأسرة المقيمين بالمنزل بصفة دائمة",  null=True, blank=True)
    above18 = models.IntegerField(
        verbose_name="عدد الأبناء فوق سن ١٨ سنة", null=True, blank=True)
    study_elm = models.IntegerField(
        verbose_name="عدد الطلبة في الإبتدائي", null=True, blank=True)
    study_elm = models.IntegerField(
        verbose_name="عدد الطلبة في الإعدادي",  null=True, blank=True)
    study_elm = models.IntegerField(
        verbose_name="عدد الطلبة في الثانوي", null=True, blank=True)
    study_elm = models.IntegerField(
        verbose_name="عدد الطلبة في الجامعي",  null=True, blank=True)
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return "Family Id" + self.fid + " - No of Members"


class FamilyMemberDetail(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    fullname = models.CharField(
        verbose_name="الأسم الثلاثي و القبيلة",  max_length=300, null=True, blank=True)
    rel = models.CharField(verbose_name="صلة القرابة",
                           max_length=50, null=True, blank=True)
    familystatus = models.CharField(
        verbose_name="الحالة الإجتماعية", max_length=300, null=True, blank=True)
    dateofbirth = models.CharField(
        verbose_name="سنة الميلاد", max_length=50, null=True, blank=True)
    education = models.CharField(
        verbose_name="المرحلة الدراسية",  max_length=50, null=True, blank=True)
    job = models.CharField(verbose_name="الوظيفة",
                           max_length=50, null=True, blank=True)
    jobplace = models.CharField(
        verbose_name="جهة العمل", max_length=50, null=True, blank=True)
    montlyincom = models.DecimalField(
        verbose_name="مبلغ الدخل الشهري", max_digits=6, decimal_places=2)
    loan = models.DecimalField(
        verbose_name="مبلغ القرض", max_digits=6, decimal_places=2)
    installment = models.DecimalField(
        verbose_name="مبلغ القسط الشهري", max_digits=6, decimal_places=2)
    loandesc = models.TextField(
        verbose_name="سبب القرض", null=True, blank=True)
    healthstatus = models.TextField(
        verbose_name="إسم الحالة الصحية", null=True, blank=True)

    def __str__(self):
        return "Family Id" + self.fid + " - Member Details"


class FamilyIncome(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    mainIncom = models.DecimalField(
        verbose_name="مبلغ الراتب", max_digits=6, decimal_places=2)
    retirIncom = models.DecimalField(
        verbose_name="مبلغ التقاعد", max_digits=6, decimal_places=2)
    insuIncom = models.DecimalField(
        verbose_name="الضمان", max_digits=6, decimal_places=2)
    sctIncom = models.DecimalField(
        verbose_name="مبلغ فريق صلالة الخيري", max_digits=6, decimal_places=2)
    othersIncom = models.DecimalField(
        verbose_name="مبالغ أخرى", max_digits=6, decimal_places=2)


def __str__(self):
    return "Family Id" + self.fid + " - Incomes"


class FamilyHouse(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    housetype = models.CharField(
        verbose_name="نوع السكن", max_length=50, null=True, blank=True)
    houseothers = models.CharField(
        verbose_name="أخرى", max_length=50, null=True, blank=True)
    houseontype = models.CharField(
        verbose_name="نوع حيازة السكن", max_length=50, null=True, blank=True)
    houseroom_n = models.IntegerField(
        verbose_name="عددالغرف", null=True, blank=True)
    housersetting_n = models.IntegerField(
        verbose_name="عددالمجالس", null=True, blank=True)
    housekitten_n = models.IntegerField(
        verbose_name="عددالمطابخ", null=True, blank=True)
    housebath_n = models.IntegerField(
        verbose_name="عددالحمامات", null=True, blank=True)
    houserent_t = models.DecimalField(
        verbose_name="مبالغ الإيجار الشهري", max_digits=6, decimal_places=2)
    houserent_r = models.DecimalField(
        verbose_name="المتبقي من الإيجار الشهري", max_digits=6, decimal_places=2)
    houseelec_r = models.DecimalField(
        verbose_name="مبالغ فاتورة الكهرباء", max_digits=6, decimal_places=2)
    housewater_r = models.DecimalField(
        verbose_name="مبالغ فاتورةالمياة", max_digits=6, decimal_places=2)

    def __str__(self):
        return "Family Id" + self.fid + " - House Details"


class FamilyAssit(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    assit_private_cars = models.IntegerField(
        verbose_name="السيارات الخاصة", null=True, blank=True)
    assit_taxi = models.IntegerField(
        verbose_name="تاكسي",  null=True, blank=True)
    assit_school_bus = models.IntegerField(
        verbose_name="حافلات المدرسة", null=True, blank=True)
    assit_gaz_car = models.IntegerField(
        verbose_name="سيارات الغاز",  null=True, blank=True)
    assit_others = models.TextField(verbose_name="أخرى", null=True)

    def __str__(self):
        return "Family Id" + self.fid + " - Assit"


class FamilyLoan(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    loantype = models.IntegerField(
        verbose_name="نوع القرض",  null=True, blank=True)
    nameloner = models.DecimalField(
        verbose_name="إسم الجهة المناعة للقرض أو التمويل", max_digits=6, decimal_places=2)
    totalloan = models.DecimalField(
        verbose_name="مبلغ القرض", max_digits=6, decimal_places=2)
    instllament = models.DecimalField(
        verbose_name="القسط الشهري", max_digits=6, decimal_places=2)
    balanc = models.DecimalField(
        verbose_name="المبلغ المتبقي", max_digits=6, decimal_places=2)

    def __str__(self):
        return "Family Id" + self.fid + " - Loan Details"


class FamilyNeeds(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    food_supply = models.BooleanField(
        verbose_name="كفالة مواد غذائية", default=False)
    orp_care = models.BooleanField(
        verbose_name="كفالة أسر أيتام", default=False)
    elec_needs = models.TextField(
        verbose_name="المواد الكهربائية", null=True, blank=True)
    furn_needs = models.TextField(
        verbose_name="الأثاث المنزلي",  null=True, blank=True)
    other_needs = models.TextField(
        verbose_name="متطلبات أخري",  null=True, blank=True)


class FamilyReport(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    family_report = models.TextField(
        verbose_name="تقرير الباحث الإجتماعي عن حالة الأسرة", null=True, blank=True)
    recome = models.TextField(
        verbose_name="إقتراحات الباحث", null=True, blank=True)
    res_name = models.CharField(
        verbose_name="إسم الباحث", max_length=200, null=True, blank=True)
    res_date = models.DateTimeField(
        verbose_name="تاريخ البحث", null=True, blank=True)
    res_tel = models.CharField(
        verbose_name="رقم الهاتف", max_length=30, null=True, blank=True)
    comm_rec = models.TextField(
        verbose_name="توصية اللجنة", null=True, blank=True)

    def __str__(self):
        return "Family Id" + self.fid + " - Report Details"


class FamilyAttch(models.Model):
    fid = models.ForeignKey(Family, on_delete=models.CASCADE)
    letter_app = models.FileField(verbose_name="رسالة طلب لفريق صلالة الخيري",
                                  upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    id_copy1 = models.FileField(verbose_name="البطاقة الشخصية لصحاب الطلب",
                                upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    id_copy2 = models.FileField(verbose_name="البطاقة الشخصية أو الجواز لكل سكان المنزل",
                                upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    incom_prove = models.FileField(verbose_name="كشف حساب بنكي لمدة ستة شهور",
                                   upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    dept_prove = models.FileField(verbose_name="إثبات المديونية",
                                  upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    workforce_prove = models.FileField(verbose_name="إثبات القوة العاملة",
                                       upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    incom_prove = models.FileField(verbose_name="كشف حساب بنكي لمدة ستة شهور",
                                   upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    coll_copy = models.FileField(verbose_name="نسخ من عقد الزواج/وثيقة الطلاق/شهادة وفاه/ملكية منزل/حكم بالسجن",
                                 upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    rent_prove = models.FileField(verbose_name="نسخة عقد إيجار مثبت",
                                  upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')
    medical_report = models.FileField(
        verbose_name="تقرير طبي مفصل", upload_to='documents/%Y/%m/%d/%H/%M/%S/', default='documents/None/no-img.jpg')

    def __str__(self):
        return "Family Id" + self.fid + " - Attachment Details"
