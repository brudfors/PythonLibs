def vtkVertexGlyphFilter(modelNode):
  glyphFilter = vtk.vtkVertexGlyphFilter()
  glyphFilter.SetInputData(modelNode.GetPolyData())
  glyphFilter.Update()
  modelNode.SetAndObservePolyData(glyphFilter.GetOutput())