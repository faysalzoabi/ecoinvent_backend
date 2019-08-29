from django.contrib import admin
from .models import DatasetData, DatasetFile, System, Version
from datasets.api.getdata import getFilesData

admin.site.register(DatasetData)
admin.site.register(System)
admin.site.register(Version)

class DatasetFileAdmin(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        obj.save()
        #get the data
        data = getFilesData(obj.document.path)

        #create instance of DatasetFile
        datasetData = DatasetData()
        
        DatasetData.datafile = obj

        datasetData.activity_name = data['activityName']
        datasetData.geography = data['shortname']
        datasetData.referenceProductName = data['unitName']
        datasetData.save()

admin.site.register(DatasetFile, DatasetFileAdmin) 
