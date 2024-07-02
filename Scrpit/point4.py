import arcpy
arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True
geography_regions_elevation_points = arcpy.GetParameterAsText(0)
glaciated_areas = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)
arcpy.MakeFeatureLayer_management(glaciated_areas,'glaciated')
curso= arcpy.SearchCursor(geography_regions_elevation_points ,['region'])
for i in curso:
    name= str(i.getValue('region')).replace('(','').replace(')','').replace('-','').replace('_','').replace(' ','')
    arcpy.MakeFeatureLayer_management(geography_regions_elevation_points ,'gego',""" "region"='{}' """.format(i.getValue('region')))
    arcpy.SelectLayerByLocation_management('gego', 'WITHIN', 'glaciated')
    arcpy.FeatureClassToFeatureClass_conversion('gego',output,'eachregoin_{}'.format(name))