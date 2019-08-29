from django.db import models
from datasets.api.getdata import getFilesData
# Create your models here.

class Version(models.Model):
    data_version = models.IntegerField()

class System(models.Model):
    data_system = models.IntegerField()

class DatasetFile(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    version = models.ForeignKey(
        Version,
        related_name='datasetfiles',
        on_delete=models.CASCADE
    )
    system = models.ForeignKey(
        System,
        related_name='datasetfiles',
        on_delete=models.CASCADE
    )
    def save(self, *args, **kwargs):
        if self.document:
            data = getFilesData(self.document)
            datasetData = DatasetData()
            DatasetData.datafile = self
            datasetData.activity_name = data['activityName']
            datasetData.geography = data['shortname']
            datasetData.referenceProductName = data['unitName']
            datasetData.save()
        super(DatasetFile, self).save(*args, **kwargs)

class DatasetData(models.Model):
    activity_name = models.CharField(max_length=250 , null=True, blank=True)
    geography = models.CharField(max_length=250, null=True, blank=True)
    referenceProductName = models.CharField(max_length=200, null=True, blank=True)
    datafile = models.OneToOneField(
        DatasetFile,
        on_delete=models.CASCADE,
        primary_key=True,
        db_constraint=False
    )
    


