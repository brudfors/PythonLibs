def colorPointData(modelNode, min, max, newMin, newMax):
  polyData = modelNode.GetPolyData()
  # Create rainbow color table  
  colorTable=slicer.vtkMRMLColorTableNode()
  colorTable.SetTypeToRainbow ()  
  # Calculate normalizing constants
  n = (newMax-newMin)/(max-min)
  # Create color array
  colorArray = vtk.vtkDoubleArray()
  colorArray.SetNumberOfComponents(4)
  colorArray.SetName('Colors')
  polyData.GetPointData().SetScalars(colorArray)    
  # Normalize and add color scalar
  color = [0, 0, 0, 0]
  for i in range(polyData.GetNumberOfPoints()):
    ras = polyData.GetPoint(i)
    tableValue = 1 + (ras[1] - min) * n
    colorTable.GetColor(int(tableValue), color) # 0 -> 255
    colorArray.InsertTuple(i, color)
    
p=getNode('Points_2015-09-11_17-43-49')
colorPointData(p, -30, 0, 0, 255)

m=p.GetModelDisplayNode()
m.SetActiveScalarName('Colors')
m.SetScalarVisibility(True)

p=getNode('Points_2015-09-11_16-28-47')
colorPointData(p, -27, 27, 0, 255)