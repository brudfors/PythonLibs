def glyphPoints(modelNodeName, tolerance, scaleFactor):
  modelNode = getNode(modelNodeName)
  if modelNode:
    polyData = modelNode.GetPolyData()
    # Clean
    cleaner = vtk.vtkCleanPolyData()
    cleaner.SetInputData(polyData)
    cleaner.SetTolerance(tolerance)
    cleaner.Update()
    # Glyph
    glyph3D = vtk.vtkGlyph3D()
    glyph3D.SetInputData(cleaner.GetOutput())
    sphereSource  = vtk.vtkSphereSource()
    glyph3D.SetSourceConnection(sphereSource.GetOutputPort())
    glyph3D.SetScaleFactor(scaleFactor)
    glyph3D.Update()
    modelNode.SetAndObservePolyData(glyph3D.GetOutput())  