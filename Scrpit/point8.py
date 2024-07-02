import arcpy

arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True
rivers_lake_centerlines = arcpy.GetParameterAsText(0)
output_workspace = arcpy.GetParameterAsText(1)


arcpy.env.workspace = output_workspace
arcpy.env.overwriteOutput = True


arcpy.MakeFeatureLayer_management(rivers_lake_centerlines, "river_lake_centerline_lyr", """ "featurecla"='Lake Centerline' """)


arcpy.FeatureClassToFeatureClass_conversion('river_lake_centerline_lyr', output_workspace, "ALL_LAKE_Centerline")
