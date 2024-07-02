import arcpy
arcpy.env.workspace = r'E:\FinalProjectGis\Data'
arcpy.env.overwriteOutput = True
geography_regions_polys = arcpy.GetParameterAsText(0)



with arcpy.da.SearchCursor(geography_regions_polys, ['NAME', 'REGION', 'WIKIDATAID']) as cursor:
    for row in cursor:
        # Convert values to string and handle Unicode characters
        name = row[0].encode('utf-8').decode('utf-8').replace('(', '').replace(')', '').replace('-', '').replace('_', '').replace(' ', '').replace('.', '')
        region = row[1].encode('utf-8').decode('utf-8').replace('(', '').replace(')', '').replace('-', '').replace('_', '').replace(' ', '')
        wikidataid = row[2].encode('utf-8').decode('utf-8')

        arcpy.AddMessage(name)
        arcpy.AddMessage(region)
        arcpy.AddMessage(wikidataid+"\n")