def getDistanceBetweenSlicerTransformNodes(nameA, nameB):
  import math
  
  a=getNode(nameA)
  b=getNode(nameB)
  
  ma = vtk.vtkMatrix4x4()
  mb = vtk.vtkMatrix4x4()
  
  a.GetMatrixTransformToWorld(ma)
  b.GetMatrixTransformToWorld(mb)
  
  pa=[ma.GetElement(0,3),ma.GetElement(1,3),ma.GetElement(2,3)]
  pb=[mb.GetElement(0,3),mb.GetElement(1,3),mb.GetElement(2,3)]
  
  return math.sqrt(vtk.vtkMath().Distance2BetweenPoints(pa,pb))