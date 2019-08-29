from xml.dom import minidom

def getFilesData(file):
    parsedFile = minidom.parse(file)
    item1 = parsedFile.getElementsByTagName('activityName')[0].firstChild.data
    item2 = parsedFile.getElementsByTagName('shortname')[0].firstChild.data
    item3 = parsedFile.getElementsByTagName('unitName')[0].firstChild.data

    meta={}
    meta['activityName'] = item1
    meta['shortname'] = item2
    meta['unitName'] = item3
    return meta

