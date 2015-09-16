def filterConoProbePoints(modelNode, csvPath, snrThreshold, distanceMinimumValue, distanceMaximumValue): 
  import csv  
  snr = []
  distance = []
  ras = []
  with open(csvPath, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      ras.append(row[0:3])
      snr.append(row[4])
      distance.append(row[3])
  # Create new vtkPolyData
  newPoints = vtk.vtkPoints()
  newVertices = vtk.vtkCellArray()               
  newPolyData = vtk.vtkPolyData()
  newPolyData.SetPoints(newPoints)
  newPolyData.SetVerts(newVertices)
  # Filter accordingly to the input parameters  
  for idx in range(len(distance)):    
    if (snr[idx] > snrThreshold and distance[idx] < distanceMaximumValue and distance[idx] > distanceMinimumValue):        
      addPointToPolyData(newPolyData, ras[idx])
  # Update recorded model and buffer
  modelNode.GetPolyData().DeepCopy(newPolyData)     
  modelNode.GetPolyData().Modified()  

def addPointToPolyData(polyData, ras):      
  pid = vtk.vtkIdList()
  pid.SetNumberOfIds(1);
  temp = polyData.GetPoints().InsertNextPoint(ras[0], ras[1], ras[2])    
  pid.SetId(0, temp)    
  polyData.GetVerts().InsertNextCell(pid)        
  polyData.Modified() 
    
def createModelNode(name, color):
  scene = slicer.mrmlScene
  modelNode = slicer.vtkMRMLModelNode()
  modelNode.SetScene(scene)
  modelNode.SetName(name)
  polyData = vtk.vtkPolyData()
  modelNode.SetAndObservePolyData(polyData)
  modelDisplay = slicer.vtkMRMLModelDisplayNode()
  modelDisplay.SetColor(color)
  modelDisplay.SetScene(scene)
  scene.AddNode(modelDisplay)
  modelNode.SetAndObserveDisplayNodeID(modelDisplay.GetID())
  scene.AddNode(modelNode)  
  
createModelNode('FilteredPoints', [1,0,0])
m = getNode('FilteredPoints')
filterConoProbePoints(m, 'H:/src/conoprobe/SlicerModules/ConoProbeConnector/Output/2015-09-14/Points_2015-09-14_19-15-57.csv', 93, 100, 400)