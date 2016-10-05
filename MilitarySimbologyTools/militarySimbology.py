# -*- coding: utf-8 -*-

# Qt imports
from PyQt4.QtSql import QSqlDatabase
# QGIS imports
from qgis.core import QgsDataSourceURI, QgsMapLayerRegistry, QgsVectorLayer, QgsProject, QgsLayerTreeLayer
# lib python imports
import re
import os

class MilitarySymbology:        
    def __init__(self, iface, sqlitePathDB, stylePath, nameLayer):
        self.iface = iface
        self.stylePath = stylePath
        uri = QgsDataSourceURI()
        uri.setDatabase(sqlitePathDB)
        listOfTables = self.readTablesSqlite(uri)
        listOfConf = self.loadTables(uri, listOfTables)
        self.loadLayer(listOfConf, uri, nameLayer)

    def readTablesSqlite(self, uri):
        db = QSqlDatabase.addDatabase("QSQLITE");
        db.setDatabaseName(uri.database())
        db.open()
        query = db.exec_("""SELECT name FROM sqlite_master WHERE type='table';""")
        listOfTables = []
        while query.next():
            m = re.search('^d', query.value(0))
            if m != None:
                listOfTables.append(m.string)
        return listOfTables
    
    def setConfStyleForm(self, tableId):
        conf = dict()
        #conf[u'FilterExpression'] = u'code in (0,1,2,3)'
        conf[u'Layer'] = tableId
        conf[u'UseCompleter'] = False
        conf[u'AllowMulti'] =  True
        conf[u'AllowNull'] = True
        conf[u'OrderByValue'] =  False
        conf[u'Value'] = u'code_name'
        conf[u'Key'] = u'code'
        return conf        
    
    def loadTables(self, uri, listOfTables):
        listOfConfToFields = []
        root = QgsProject.instance().layerTreeRoot()
        if not root.findGroup(u"Mapa_de_valores"):
            legend = self.iface.legendInterface()
            groupMapvalue = legend.addGroup (u"Mapa_de_valores", True)
            
            for table in listOfTables:
                uri.setDataSource('', table,'','','id')
                table = QgsVectorLayer(uri.uri(), table[9:], 'spatialite')
                QgsMapLayerRegistry.instance().addMapLayer(table)
                tableId = self.iface.activeLayer().id()
                legend.moveLayer(legend.layers()[0], groupMapvalue)
                conf = self.setConfStyleForm(tableId)
                listOfConfToFields.append(conf)
            return listOfConfToFields
        else:
            group = root.findGroup(u"Mapa_de_valores")
            for table in group.children():
                conf = self.setConfStyleForm(table.layerId())
                listOfConfToFields.append(conf)
            return list(reversed(listOfConfToFields))
        
        
    def loadLayer(self, listOfConf, uri, nameLayer):
        root = QgsProject.instance().layerTreeRoot()
        mygroup = root.findGroup(u"Mapa_de_valores")
        parentGroup = mygroup.parent()
        groupIndex=-1
        for child in parentGroup.children():
            groupIndex+=1
            if mygroup == child:
                break
        uri.setDataSource('', nameLayer.lower(), 'geometria', '', 'id')
        layer = QgsVectorLayer(uri.uri(), nameLayer, 'spatialite')
        QgsMapLayerRegistry.instance().addMapLayer(layer, False)
        parentGroup.insertChildNode(groupIndex, QgsLayerTreeLayer(layer))
        self.loadStyle(layer, listOfConf)
            
    def loadStyle(self, layer, listOfConf):
        with open( self.stylePath, 'r') as template_style:
            style = template_style.read().replace('\n', '')
        styleReady = unicode(self.setPathStyle(style), 'utf-8')    
        layer.applyNamedStyle(styleReady)
        i = 2
        for index in range(len(listOfConf)) : 
            layer.setEditorWidgetV2Config(i, listOfConf[index] )
            i+=1

    def setPathStyle(self, style):
        currentPath = os.path.join(os.path.dirname(__file__), 'symbols')+os.sep
        styleReady = style.replace('{path}', currentPath)
        return styleReady

