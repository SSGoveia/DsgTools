# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2016-02-18
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Philipe Borba - Cartographic Engineer @ Brazilian Army
        email                : borba@dsg.eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.core import QgsMessageLog
from PyQt4.QtGui import QMessageBox
from PyQt4.Qt import QObject

class ValidationProcess(QObject):
    def __init__(self, postgisDb, codelist):
        super(ValidationProcess, self).__init__()
        self.abstractDb = postgisDb
        if self.getStatus() == None:
            self.setStatus('Instantianting process', 0)
        self.classesToBeDisplayedAfterProcess = []
        self.parameters = None
        self.parametersDict = None
        self.codelist = codelist
        
    def setParameters(self, params):
        self.parameters = params

    def setParametersDict(self, params):
        self.parametersDict = params
    
    def execute(self):
        #abstract method. MUST be reimplemented.
        pass
    
    def shouldBeRunAgain(self):
        #Abstract method. Should be reimplemented if necessary.
        return False
    
    def getName(self):
        return str(self.__class__).split('.')[-1].replace('\'>', '')
    
    def getProcessGroup(self):
        return 'Ungrouped'
    
    def getClassesToBeDisplayedAfterProcess(self):
        #returns classes to be loaded to TOC after executing this process.
        return self.classesToBeDisplayedAfterProcess
    
    def addClassesToBeDisplayedList(self,className):
        if className not in self.classesToBeDisplayedAfterProcess:
            self.classesToBeDisplayedAfterProcess.append(className)
    
    def clearClassesToBeDisplayedAfterProcess(self):
        self.classesToBeDisplayedAfterProcess = []
    
    def dependsOn(self):
        #Abstract method. Should be reimplemented if necessary.
        return []
    
    def addFlag(self, flagTupleList):
        try:
            return self.abstractDb.insertFlags(flagTupleList,self.getName())
        except Exception as e:
            QMessageBox.critical(None, self.tr('Critical!'), self.tr('A problem occurred! Check log for details.'))
            QgsMessageLog.logMessage(str(e.args[0]), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
    
    def getStatus(self):
        try:
            return self.abstractDb.getValidationStatus(self.getName())
        except Exception as e:
            QMessageBox.critical(None, self.tr('Critical!'), self.tr('A problem occurred! Check log for details.'))
            QgsMessageLog.logMessage(str(e.args[0]), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
    
    def getStatusMessage(self):
        try:
            return self.abstractDb.getValidationStatusText(self.getName())
        except Exception as e:
            QMessageBox.critical(None, self.tr('Critical!'), self.tr('A problem occurred! Check log for details.'))
            QgsMessageLog.logMessage(str(e.args[0]), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
    
    def setStatus(self, msg, status):
        try:
            self.abstractDb.setValidationProcessStatus(self.getName(), msg, status)
        except Exception as e:
            QMessageBox.critical(None, self.tr('Critical!'), self.tr('A problem occurred! Check log for details.'))
            QgsMessageLog.logMessage(str(e.args[0]), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
    
    def finishedWithError(self):
        self.setStatus('Process finished with errors.', 2) #Failed status
        self.clearClassesToBeDisplayedAfterProcess()        
    
    def outputData(self, type, inputClass, dataDict):
        '''
        type: postgis or qgsvectorlayer
        inputClass: name of the class
        dataDict: dict with the keys update, delete or insert. for each type, there is a proper data, ie:
            postgis: tuple of (id,geom)
            qgsvectorlayer: layer with geometry 
        '''
        edgvLayer = self.layerFactory.makeLayer(self.abstractDb, self.codeList, inputClass)
        crs = self.abstractDb.getSrid()
        outputLayer = edgvLayer.load(crs, uniqueLoad = True)
        if type == 'postgis':
            ret = self.outputPostgisData(outputLayer, inputClass,dataDict)
        else:
            ret = self.outputVectorData(outputLayer, inputClass,dataDict)
        
    def outputPostgisData(self, outputLayer, inputClass, dataDict):
        '''
        outputLayer: edgv layer previously loaded;
        inputClass: name of the class;
        dataDict: dict with the keys update, delete or insert. for each type, there is a key of names of the fields and values with a list of tupples.
        '''
        outputLayer.startEditing()
        for type in dataDict.keys():
            if type == 'INSERT':
                self.insertFeaturesFromPostgis(outputLayer, type, dataDict)
            elif type == 'UPDATE':
                self.updateFeaturesFromPostgis(outputLayer, type, dataDict)
            elif type == 'DELETE':
                self.deleteFeaturesFromPostgis(outputLayer, type, dataDict)

    def insertFeaturesFromPostgis(self, outputLayer, type, dataDict):
        for attributes in dataDict[type].keys():
            attrList = attributes.split(',')
            fieldDict = dict()
            for attr in attrList:
                fieldDict[attr] = outputLayer.fieldNameIndex(attr)
            featList = []
            for tuple in dataDict[type][attributes]:
                newFeat = QgsFeature(outputLayer.pendingFields())
                insertDict = dict()
                for i in range(attrList):
                    if attrList[i] == 'id':
                        pass
                    elif attrList[i] == 'geom':
                        wkbGeom = tuple(i)
                        geom = QgsGeometry()
                        geom.fromWkb(tuple[i],len(tuple[i]))
                        newFeat.setGeometry(geom)
                    else:
                        fieldId = outputLayer.fieldNameIndex(attrList[i])
                        newFeat.setAttribute(fieldDict[attrList[i]],tuple[i])
                featList.append(newFeat)
            outputLayer.addFeatures(featList)

    def updateFeaturesFromPostgis(self, outputLayer, type, dataDict):
        for attributes in dataDict[type].keys():
            attrList = attributes.split(',')
            fieldDict = dict()
            for attr in attrList:
                fieldDict[attr] = outputLayer.fieldNameIndex(attr)
            featList = []
            for tuple in dataDict[type][attributes]:
                insertDict = dict()
                for i in range(attrList):
                    if attrList[i] == 'id':
                        id = attrList[i]
                    elif attrList[i] == 'geom':
                        wkbGeom = tuple(i)
                        geom = QgsGeometry()
                        geom.fromWkb(tuple[i],len(tuple[i]))
                for i in range(attrList):
                    if attrList[i] not in ['id', 'geom']:
                        outputLayer.changeAttributeValue(id, fieldDict[attrList[i]], tuple[i])
                    elif attrList[i] == 'geom':
                        outputLayer.changeGeometry(id, geom)
    
    def deleteFeaturesFromPostgis(self, outputLayer, type, dataDict):
        for attributes in dataDict[type].keys():
            attrList = attributes.split(',')
            fieldDict = dict()
            for attr in attrList:
                fieldDict[attr] = outputLayer.fieldNameIndex(attr)
            featList = []
            for tuple in dataDict[type][attributes]:
                outputLayer.deleteFeature(tuple[0])
    
    def outputVectorData(self, outputLayer, inputClass, dataDict):
        '''
        outputLayer: edgv layer previously loaded;
        inputClass: name of the class;
        dataDict: dict with the keys UPDATE, DELETE or INSERT. For each type, there is a list of features to be output.
        '''
        outputLayer.startEditing()
        for type in dataDict.keys():
            if type == 'INSERT':
                self.insertFeatures(outputLayer, type, dataDict)
            elif type == 'UPDATE':
                self.updateFeatures(outputLayer, type, dataDict)
            elif type == 'DELETE':
                self.deleteFeatures(outputLayer, type, dataDict)

    def insertFeatures(self, outputLayer, type, dataDict):
        #TODO
        featureList = dataDict[type]
        pass

    def updateFeatures(self, outputLayer, type, dataDict):
        #TODO
        featureList = dataDict[type]
        pass

    def deleteFeatures(self, outputLayer, type, dataDict):
        #TODO
        featureList = dataDict[type]
        pass