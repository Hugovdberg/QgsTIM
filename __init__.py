# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QgsTIM
                                 A QGIS plugin
 QGIS frontend for the TimML library
                             -------------------
        begin                : 2015-07-08
        copyright            : (C) 2015 by Hugo van den Berg
        email                : hugo.van.den.berg@brabantwater.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import qtqgisgui


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QgsTIM class from file QgsTIM.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .QgsTIM import QgsTIM
    return QgsTIM(iface)
