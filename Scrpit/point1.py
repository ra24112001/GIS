import arcpy
arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True
geography_regions_elevation_points = arcpy.GetParameterAsText(0)
geography_regions_points= arcpy.GetParameterAsText(1)
rivers_lake_centerlines = arcpy.GetParameterAsText(2)
glaciated_areas = arcpy.GetParameterAsText(3)
geography_regions_polys= arcpy.GetParameterAsText(4)
land = arcpy.GetParameterAsText(5)

feature_list = arcpy.ListFeatureClasses()


arcpy.AddMessage("List of feature classes:")
for feature_class in feature_list:
    arcpy.AddMessage(feature_class)