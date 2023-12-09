###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical 
# and can be found in most VTK programs

# Imports
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource, vtkCylinderSource, vtkCubeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkCamera,
    vtkLight
)

def main():

    # Create a cone
    coneSource = vtkConeSource()
    coneSource.SetHeight(2) 
    coneSource.SetRadius(1)
    # coneSource.SetResolution(1)
    coneSource.SetResolution(10)
    # coneSource.SetResolution(100)

    # Create a mapper
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection( coneSource.GetOutputPort() )

    # Create an actor
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    # Create a sphere
    sphereSource = vtkSphereSource()
    sphereSource.SetRadius(2)
    # sphereSource.SetPhiResolution(1)
    sphereSource.SetPhiResolution(10)
    # sphereSource.SetThetaResolution(100)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetPosition(0, 0, 5)  

    # Create a cylinder
    cylinderSource = vtkCylinderSource()
    cylinderSource.SetRadius(2)
    cylinderSource.SetHeight(3)
    # cylinderSource.SetResolution(1)
    cylinderSource.SetResolution(10)
    # cylinderSource.SetResolution(100)

    cylinderMapper = vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinderSource.GetOutputPort())

    cylinderActor = vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.SetPosition(0, 0, -5)

    # Create a cube
    cubeSource = vtkCubeSource()
    cubeSource.SetXLength(2)

    cubeMapper = vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cubeSource.GetOutputPort())

    cubeActor = vtkActor()
    cubeActor.SetMapper(cubeMapper)
    cubeActor.GetProperty().SetRepresentationToWireframe()
    cubeActor.SetPosition(0, 5, 0)

    # Create the Renderer and assign actors 
    ren = vtkRenderer()
    ren.AddActor( coneActor )
    ren.AddActor( sphereActor )
    ren.AddActor( cylinderActor )
    ren.AddActor( cubeActor )
    ren.SetBackground( 1, 1, 1)

    # Set the camera position
    # cam1 = vtkCamera()
    # cam1.SetPosition(10,10,0)
    # cam1.SetViewUp(0,1,1)
    # ren.SetActiveCamera(cam1)

    # defaultCamera = ren.GetActiveCamera()

    # # Set the camera position
    # defaultCamera.SetPosition(10, 10, 0)
    # defaultCamera.SetViewUp(0, 1, 1)
    # defaultCamera.SetParallelProjection(True)
    
    cam1 = ren.GetActiveCamera()
    light = vtkLight()
    light.SetColor(1,0,0)
    light.SetFocalPoint(cam1.GetFocalPoint())
    light.SetPosition(cam1.GetPosition())
    ren.AddLight(light)


    # Create the RendererWindow    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetWindowName('Cone')
    renWin.SetSize(500, 500)
    
    # # Now we loop over 360 degrees and render the cone each time.
    # for i in range(0,360):
    #     # render the image
    #     renWin.Render()
    #     # rotate the active camera by one degree
    #     ren.GetActiveCamera().Azimuth(1)

    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()