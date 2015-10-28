# Copy paste this script into the 3D Slicer Python console
def registrationResultAsHeatMap(fromModelNodeName,
                                toModelNodeName):
  import math
  import numpy as np
  fromModelNode = getNode(fromModelNodeName)
  toModelNode = getNode(toModelNodeName)
  if fromModelNode and toModelNode:
    fromPolyData = fromModelNode.GetPolyData()
    toPolyData = toModelNode.GetPolyData()
    cellLocator = vtk.vtkCellLocator()
    cellLocator.SetDataSet(toPolyData)
    cellLocator.BuildLocator()    
    distances = []
    distancesSquared = []    
    for idx in range(fromPolyData.GetNumberOfPoints()):
      point = fromPolyData.GetPoint(idx)
      closestPoint = [0.0, 0.0, 0.0]
      distanceSquared = vtk.mutable(0.0)
      subId = vtk.mutable(0)
      cellId = vtk.mutable(0)
      cell = vtk.vtkGenericCell()
      cellLocator.FindClosestPoint(point, closestPoint, cell, cellId, subId, distanceSquared)
      distancesSquared.append(distanceSquared)
      distances.append(math.sqrt(distanceSquared))     
    distanceArray = vtk.vtkDoubleArray()
    distanceArray.SetNumberOfValues(len(distances))
    distanceArray.SetName('Distances')
    for i in range(len(distances)):    
      distanceArray.SetValue(i, distances[i])
    fromPolyData.GetPointData().SetScalars(distanceArray)      
    fromPolyData.Modified()   
  else:
    print "Model node(s) doesn't exist!" 
    
registrationResultAsHeatMap('breast_open','ComputedSurface')    