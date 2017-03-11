# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2016-02-18
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Luiz Andrade - Cartographic Engineer @ Brazilian Army
        email                : luiz.claudio@dsg.eb.mil.br
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
from DsgTools.ValidationTools.ValidationProcesses.validationProcess import ValidationProcess

class IdentifyOutOfBoundsAnglesProcess(ValidationProcess):
    def __init__(self, postgisDb, iface):
        """
        Constructor
        """
        super(self.__class__,self).__init__(postgisDb, iface)
        self.processAlias = self.tr('Identify Out Of Bounds Angles')
        
        classesWithElemDictList = self.abstractDb.listGeomClassesFromDatabase(primitiveFilter=['a', 'l'], withElements=True, getGeometryColumn=True)
        classesWithElem = ['{0}:{1}'.format(i['layerName'], i['geometryColumn']) for i in classesWithElemDictList]
        self.parameters = {'Angle': 10.0, 'Classes': classesWithElem}

    def execute(self):
        """
        Reimplementation of the execute method from the parent class
        """
        QgsMessageLog.logMessage(self.tr('Starting ')+self.getName()+self.tr(' Process.'), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
        try:
            self.setStatus(self.tr('Running'), 3) #now I'm running!
            self.abstractDb.deleteProcessFlags(self.getName()) #erase previous flags
            classesWithElem = self.parameters['Classes']
            if len(classesWithElem) == 0:
                self.setStatus(self.tr('Empty database.'), 1) #Finished
                QgsMessageLog.logMessage(self.tr('Empty database.'), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
                return 1
            tol = self.parameters['Angle']
            error = False
            for classAndGeom in classesWithElem:
                # preparation
                cl, geometryColumn = classAndGeom.split(':')
                processTableName, lyr = self.prepareExecution(cl, geometryColumn)
                tableSchema, tableName = self.abstractDb.getTableSchema(processTableName)
                
                # running the process
                result = self.abstractDb.getOutOfBoundsAnglesRecords(tableSchema, tableName, tol)

                # dropping temp table
                self.abstractDb.dropTempTable(processTableName)
                
                # storing flags
                if len(result) > 0:
                    error = True
                    recordList = []
                    for tupple in result:
                        recordList.append((tableSchema+'.'+tableName, tupple[0], self.tr('Angle out of bound.'), tupple[1]))
                        self.addClassesToBeDisplayedList(tupple[0]) 
                    numberOfProblems = self.addFlag(recordList)
                    QgsMessageLog.logMessage(self.tr('{0} features from {1} have out of bounds angle(s). Check flags.').format(numberOfProblems, cl), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
                else:
                    QgsMessageLog.logMessage(self.tr('There are no out of bounds angles on {0}.').format(cl), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
            if error:
                self.setStatus(self.tr('There are features with angles out of bounds. Check log.'), 4) #Finished with errors
            else:
                self.setStatus(self.tr('There are no features with angles out of bounds.'), 1) #Finished
            return 1
        except Exception as e:
            QgsMessageLog.logMessage(':'.join(e.args), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
            self.finishedWithError()
            return 0