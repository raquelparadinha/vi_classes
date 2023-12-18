import vtk

# Create a sphere with specific theta and phi resolutions
sphereSource = vtk.vtkSphereSource()
sphereSource.SetThetaResolution(20)  # Set number of divisions along longitude
sphereSource.SetPhiResolution(20)   # Set number of divisions along latitude
sphereSource.Update()

# Create a cone
coneSource = vtk.vtkConeSource()

# Create glyph3D
glyph = vtk.vtkGlyph3D()
glyph.SetSourceConnection(coneSource.GetOutputPort())
glyph.SetInputConnection(sphereSource.GetOutputPort())
glyph.SetScaleFactor(0.2)  # Scale the size of the cones
glyph.SetVectorModeToUseNormal()  # Orient cones to point outwards
glyph.Update()

# Create a mapper and actor for the glyphs
glyphMapper = vtk.vtkPolyDataMapper()
glyphMapper.SetInputConnection(glyph.GetOutputPort())

glyphActor = vtk.vtkActor()
glyphActor.SetMapper(glyphMapper)

# Create a mapper and actor for the sphere (to render it solid)
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindow.SetSize(500, 500)
# Add the actors to the scene
renderer.AddActor(glyphActor)
renderer.AddActor(sphereActor)  # Add the solid sphere actor to the renderer
renderer.SetBackground(0, 0, 0)  # Background color

# Render and interact
renderWindow.Render()
renderWindowInteractor.Start()
