import arcpy
arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True

rivers_lake_centerlines = arcpy.GetParameterAsText(0)
output = arcpy.GetParameterAsText(1)


curso= arcpy.SearchCursor(rivers_lake_centerlines ,['scalerank'])
for i in curso:
    where_clause = '"scalerank" = {}'.format(i.getValue('scalerank'))
    arcpy.MakeFeatureLayer_management(rivers_lake_centerlines ,'river',where_clause)

    scalerank_value = i.getValue('scalerank')
    output_name = 'rivers_lake_{}'.format(scalerank_value)
    arcpy.FeatureClassToFeatureClass_conversion('river',output,output_name)