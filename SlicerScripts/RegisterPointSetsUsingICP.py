def registerPointSetsUsingICP(nameModelNode1, nameModelNode2, nbrOfIterations, maximumNumberOfLandmarks):
  import math
  import numpy as np
  modelNode1 = getNode(nameModelNode1)
  modelNode2 = getNode(nameModelNode2)
  if modelNode1 and modelNode2:
    polyData1 = modelNode1.GetPolyData()
    polyData2 = modelNode2.GetPolyData()
    # Setup vtkIterativeClosestPointTransform
    icp = vtk.vtkIterativeClosestPointTransform()
    icp.SetSource(polyData1)
    icp.SetTarget(polyData2)
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
    modelNode1.SetAndObserveTransformNodeID(model1ToModel2.GetID())    
  else:
    print "Model node doesn't exist!"
    
registerPointSetsUsingICP('L_open','L_points_SNR-90_20608', 20, 200)    