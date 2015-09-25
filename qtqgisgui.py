"""
Created on 2015-09-25 12:56

@author: bergh1

"""
import sys
import qgis.gui

elements = ["qgscollapsiblegroupbox", "qgscolorbutton", "qgscolorbuttonv2",
            "qgsdatadefinedbutton", "qgsdatetimeedit", "qgsdoublespinbox",
            "qgsfieldcombobox", "qgsfieldexpressionwidget", 
            "qgsfilterlineedit", "qgsmaplayercombobox",
            "qgsprojectionselectionwidget", "qgsrelationeditorwidget",
            "qgsrelationreferencewidget", "qgsscalerangewidget",
            "qgsscalewidget", "qgsspinbox"]
for element in elements:
    sys.modules[element] = qgis.gui

