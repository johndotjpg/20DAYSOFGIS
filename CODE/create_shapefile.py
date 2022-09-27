import qgis
fn="C:/Users/Ayo/Documents/PROJECTS/20DAYSOFGIS/SHAPEFILES/fdfdfd"

layer_fields=QgsFields()
layer_fields.append(QgsField("id",QVariant.Int))
layer_fields.append(QgsField("value",QVariant.Double))
layer_fields.append(QgsField("name",QVariant.String))

writer=QgsVectorFileWriter(fn,"UTF-8",layer_fields,QgsWkbTypes.Point,
QgsCoordinateReferenceSystem("EPSG:26912"),"ESRI.Shapefile")

feat=QgsFeature()
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(6.5820529739151, 3.3212420846234534)))
feat.setAttributes([1,1.1,"name"])

writer.addFeature(feat)
iface.addVectorLayer(fn,"","ogr")
del(writer)