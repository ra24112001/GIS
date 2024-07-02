import arcpy
arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True

geography_regions_elevation_points = arcpy.GetParameterAsText(0)


fields = ['name', 'lat_y', 'long_x', 'comment']
comment = ""

cursor = arcpy.UpdateCursor(geography_regions_elevation_points, fields)
for row in cursor:
    name_value = row.getValue('name')
    if not name_value or name_value.strip() == '':
        latitude = row.getValue('lat_y')
        longitude = row.getValue('long_x')
        arcpy.AddMessage("Mountain with no name found at latitude {0} and longitude {1}".format(latitude, longitude))

        comment_value = row.getValue('comment')
        if comment_value:
            comment_value = comment_value.encode('utf-8')  # Encode to utf-8
            row.setValue('name', str(comment_value).replace("(", "").replace(")", ""))
            cursor.updateRow(row)
            arcpy.AddMessage("Comment: {}".format(comment_value))
