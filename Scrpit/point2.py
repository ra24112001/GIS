import arcpy

arcpy.env.workspace = r'E:\FinalProjectGis\Data'

arcpy.env.overwriteOutput = True


geography_regions_elevation_points = arcpy.GetParameterAsText(0)
geography_regions_points = arcpy.GetParameterAsText(1)
land = arcpy.GetParameterAsText(2)
output_workspace = arcpy.GetParameterAsText(3)


arcpy.MakeFeatureLayer_management(geography_regions_elevation_points, 'evpoints')
arcpy.MakeFeatureLayer_management(geography_regions_points, 'points')
arcpy.MakeFeatureLayer_management(land,'land')
arcpy.SelectLayerByLocation_management('evpoints','WITHIN','land')
arcpy.SelectLayerByLocation_management('points','WITHIN','land')
# Perform feature class to feature class conversion

arcpy.FeatureClassToFeatureClass_conversion('evpoints', output_workspace, 'evpointsshap')
arcpy.FeatureClassToFeatureClass_conversion('points', output_workspace, 'pointsshap')


elevation_count = int(arcpy.GetCount_management('evpoints').getOutput(0))
region_count = int(arcpy.GetCount_management('points').getOutput(0))


arcpy.AddMessage("Number of points in elevation shapefile: {}".format(elevation_count))
arcpy.AddMessage("Number of points in region shapefile: {}".format(region_count))
