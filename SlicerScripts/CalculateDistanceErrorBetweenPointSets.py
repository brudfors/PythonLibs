# Remember to harden transform
def calculateDistanceErrorBetweenPointSets(nameModelNode1, nameModelNode2):
  import math
  import numpy as np
  modelNode1 = getNode(nameModelNode1)
  modelNode2 = getNode(nameModelNode2)
  if modelNode1 and modelNode2:
    polyData1 = modelNode1.GetPolyData()
    polyData2 = modelNode2.GetPolyData()
    # Build locator from polyData2
    cellLocator = vtk.vtkCellLocator()
    cellLocator.SetDataSet(polyData2)
    cellLocator.BuildLocator()
    # For each point in polyData1 calculate and store distance
    # to the closest point in polyData2
    distances = []
    for idx in range(polyData1.GetNumberOfPoints()):
      point = polyData1.GetPoint(idx)
      closestPoint = [0.0, 0.0, 0.0]
      distanceSquared = vtk.mutable(0.0) 
      subId = vtk.mutable(0) 
      cellId = vtk.mutable(0) 
      cell = vtk.vtkGenericCell()
      cellLocator.FindClosestPoint(point, closestPoint, cell, cellId, subId, distanceSquared)
      distances.append(math.sqrt(distanceSquared))     
    print "Mean distance error is: " + str(np.mean(distances))
  else:
    print "Model node doesn't exist!"
    
calculateDistanceErrorBetweenPointSets('L_open','L_points_SNR-90_20608')    