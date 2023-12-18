import vtk

# Callback function to execute when a point is picked
def on_pick(event, picker):
    pick_pos = picker.GetPickPosition()
    print(f"Picked coordinates: {pick_pos}")
    # Update the position of the indicator sphere
    indicator_sphere_actor.SetPosition(pick_pos)
    indicator_sphere_actor.VisibilityOn()
    renderWindow.Render()

# Create a sphere
sphereSource = vtk.vtkSphereSource()
sphereSource.SetThetaResolution(20)
sphereSource.SetPhiResolution(20)
sphereSource.Update()

# Create a cone
coneSource = vtk.vtkConeSource()

# Create glyph3D
glyph = vtk.vtkGlyph3D()
glyph.SetSourceConnection(coneSource.GetOutputPort())
glyph.SetInputConnection(sphereSource.GetOutputPort())
glyph.SetScaleFactor(0.2)
glyph.SetVectorModeToUseNormal()
glyph.Update()

# Create a mapper and actor for the glyphs
glyphMapper = vtk.vtkPolyDataMapper()
glyphMapper.SetInputConnection(glyph.GetOutputPort())

glyphActor = vtk.vtkActor()
glyphActor.SetMapper(glyphMapper)

# Create a mapper and actor for the sphere
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)

# Create the indicator sphere
indicator_sphere_source = vtk.vtkSphereSource()
indicator_sphere_source.SetRadius(0.05)  # Small radius for the indicator
indicator_sphere_source.Update()

indicator_sphere_mapper = vtk.vtkPolyDataMapper()
indicator_sphere_mapper.SetInputConnection(indicator_sphere_source.GetOutputPort())

indicator_sphere_actor = vtk.vtkActor()
indicator_sphere_actor.SetMapper(indicator_sphere_mapper)
indicator_sphere_actor.GetProperty().SetColor(1, 0, 0)  # Red color
indicator_sphere_actor.VisibilityOff()  # Initially invisible

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Add the actors to the scene
renderer.AddActor(glyphActor)
renderer.AddActor(sphereActor)
renderer.AddActor(indicator_sphere_actor)  # Add the indicator sphere actor to the renderer

# Set up the point picker
pointPicker = vtk.vtkPointPicker()
renderWindowInteractor.SetPicker(pointPicker)
pointPicker.AddObserver("EndPickEvent", on_pick)

# Set the background color and render
renderer.SetBackground(0, 0, 0)
renderWindow.SetSize(500, 500)

# Render and interact
renderWindow.Render()
renderWindowInteractor.Initialize()
renderWindowInteractor.Start()
