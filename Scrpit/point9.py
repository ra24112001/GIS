import arcpy
arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True



geography_regions_elevation_points = arcpy.GetParameterAsText(0)

output_workspace = arcpy.GetParameterAsText(1)


arcpy.env.workspace = output_workspace
arcpy.env.overwriteOutput = True


arcpy.MakeFeatureLayer_management(geography_regions_elevation_points, "elevation_points_lyr",
                                  """ "region" = 'Africa' """)

# Create a set to store unique feature classes
unique_featureclas = set()


with arcpy.da.SearchCursor("elevation_points_lyr", ["featurecla"]) as cursor:
    for row in cursor:
        unique_featureclas.add(row[0])

# Iterate through unique feature classes
for featurecla in unique_featureclas:
    # Construct query for feature class and elevation condition
    query = """ "featurecla" = '{}' AND "elevation" > 1500 """.format(featurecla)

    # Make a selection based on the query
    arcpy.SelectLayerByAttribute_management("elevation_points_lyr", "NEW_SELECTION", query)

    # Check if there are selected features
    if int(arcpy.GetCount_management("elevation_points_lyr")[0]) > 0:
        # Define output filename based on feature class
        output_filename = "{}_Africa.shp".format(featurecla.replace(" ", "_"))

        # Copy selected features to a new shapefile
        arcpy.FeatureClassToFeatureClass_conversion("elevation_points_lyr", output_workspace, output_filename)

        # Print a message indicating the creation of the shapefile
        arcpy.AddMessage("Created shapefile for {}: {}".format(featurecla, output_filename))
