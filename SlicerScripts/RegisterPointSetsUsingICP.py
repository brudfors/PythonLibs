# Copy paste this script into the 3D Slicer Python console 
# and call it with the name of the two models you want to register.
# Will register fromModelNode to toModelNode.
def registerPointSetsUsingICP(fromModelNodeName, 
                              toModelNodeName, 
                              nbrOfIterations, 
                              maximumNumberOfLandmarks):
  import math
  import numpy as np
  fromModelNode = getNode(fromModelNodeName)
  toModelNode = getNode(toModelNodeName)
  if fromModelNode and toModelNode:
    fromPolyData = fromModelNode.GetPolyData()
    toPolyData = toModelNode.GetPolyData()
    # Setup vtkIterativeClosestPointTransform
    icp = vtk.vtkIterativeClosestPointTransform()
    icp.SetSource(fromPolyData)
    icp.SetTarget(toPolyData)
    icp.GetLandmarkTransform().SetModeToRigidBody()
    icp.SetMaximumNumberOfIterations(nbrOfIterations)
    icp.SetMaximumNumberOfLandmarks(maximumNumberOfLandmarks)
    icp.StartByMatchingCentroidsOn()
    icp.CheckMeanDistanceOn()
    icp.Modified()
    icp.Update()
    # Get resulting transform
    m = vtk.vtkMatrix4x4()
    m = icp.GetMatrix()
    # Model1ToModel2
    model1ToModel2 = slicer.util.getNode('Model1ToModel2')
    if not model1ToModel2:
      model1ToModel2=slicer.vtkMRMLLinearTransformNode()
      model1ToModel2.SetName("Model1ToModel2")
      slicer.mrmlScene.AddNode(model1ToModel2)
    model1ToModel2.SetMatrixTransformToParent(m)
    fromModelNode.SetAndObserveTransformNodeID(model1ToModel2.GetID())    
    # Build locator from toPolyData
    cellLocator = vtk.vtkCellLocator()
    cellLocator.SetDataSet(toPolyData)
    cellLocator.BuildLocator()
    # For each point in fromPolyData calculate and store distance
    # to the closest point in toPolyData
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
    print "Mean distance error is: " + str(np.mean(distances))
    print "RMSE: " + str(np.sqrt(np.mean(distancesSquared)))
    print "Std.dev. is: " + str(np.std(distances))
    print "Max is: " + str(np.max(distances))
    print fromModelNode.GetName() + ": " + str(fromPolyData.GetNumberOfPoints()) + " points"
    print toModelNode.GetName() + ": " + str(toPolyData.GetNumberOfPoints()) + " points"
  else:
    print "Model node doesn't exist!"    