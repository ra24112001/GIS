import arcpy

arcpy.env.workspace = r'E:\FinalProjectGis\Data'
geography_regions_points = arcpy.GetParameterAsText(0)
output = arcpy.GetParameterAsText(1)


arcpy.env.workspace = output
arcpy.env.overwriteOutput = True


countries_layer = ['Indian Ocean', 'North Pacific Ocean', 'South Pacific Ocean']


for subregion_name in countries_layer:

    arcpy.MakeFeatureLayer_management(geography_regions_points, 'threepoints',
                                      """ "subregion" = '{}' """.format(subregion_name))

    arcpy.FeatureClassToFeatureClass_conversion('threepoints', output, 'subregions_{}'.format(subregion_name))


    arcpy.AddMessage("Subregion Name: {}".format(subregion_name))
