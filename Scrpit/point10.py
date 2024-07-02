import arcpy


arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True
geography_regions_points = arcpy.GetParameterAsText(0)
field_list= arcpy.ListFields(geography_regions_points)


list_field =[]

for x in field_list:
    arcpy.AddMessage( x.name)
    arcpy.AddMessage (x.type)
    if x.type == 'String':
        list_field.append(x.name)
    else:
        arcpy.AddMessage("this is not a String,it's a {}".format(x.type))



for field in list_field:

    with arcpy.da.UpdateCursor(geography_regions_points, [field]) as cursor:
        for x in cursor:
            print  x[0]

            if x[0] == ' ':
                x[0] = 'Unknown'
                cursor.updateRow(x)
                arcpy.AddMessage("Value updated to {}".format(x[0]))





