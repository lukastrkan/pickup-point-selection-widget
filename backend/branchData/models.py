from django.db import models


class BranchType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/', null=True, blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    branchId = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    branch_type = models.ForeignKey(BranchType, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    openning_hours = models.JSONField()
    box = models.BooleanField(default=False)
    card = models.BooleanField(default=False)
    wheelchair = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Branches"
        ordering = ['name']
