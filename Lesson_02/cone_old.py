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
    coneSource.SetResolution(10)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection( coneSource.GetOutputPort() )

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)


    sphereSource = vtkSphereSource()
    sphereSource.SetRadius(2)
    sphereSource.SetPhiResolution(10)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetPosition(0, 0, 0)

    sphereMapper2 = vtkPolyDataMapper()
    sphereMapper2.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor2 = vtkActor()
    sphereActor2.SetMapper(sphereMapper2)
    sphereActor2.SetPosition(0, 0, 0)


    cylinderSource = vtkCylinderSource()
    cylinderSource.SetRadius(2)
    cylinderSource.SetHeight(3)
    cylinderSource.SetResolution(10)

    cylinderMapper = vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinderSource.GetOutputPort())

    cylinderActor = vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.SetPosition(0, 0, -5)


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
    ren.SetViewport(0, 0, 0.5, 1)
    ren.SetBackground(0.5, 0.5, 0.5)
    ren.AddActor( sphereActor )

    cam = ren.GetActiveCamera()
    cam.SetFocalPoint(0, 0, 0)
    cam.SetPosition(0, 0, 8)
    cam.SetViewUp(0, 1, 0)

    light = vtkLight()
    light.SetColor(1, 1, 1)
    light.SetFocalPoint(cam.GetFocalPoint())
    light.SetPosition(cam.GetPosition())
    ren.AddLight(light)


    ren2 = vtkRenderer()
    ren2.SetViewport(0.5, 0, 1, 1)
    ren2.SetBackground( 0.2, 0.2, 0.2)

    sphereActor2.GetProperty().SetInterpolationToFlat()
    ren2.AddActor( sphereActor2 )

    cam2 = ren2.GetActiveCamera()
    cam2.SetFocalPoint(0, 0, 0)
    cam2.SetPosition(0, 0, 8)
    cam2.SetViewUp(0, 1, 0)
    cam2.Azimuth(90)

    ren2.AddLight(light)


    # Create the RendererWindow    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.AddRenderer(ren2)

    renWin.SetWindowName('Cone')
    renWin.SetSize(600, 300)
    
    # Now we loop over 360 degrees and render the cone each time.
    for i in range(0,360):
        # render the image
        renWin.Render()
        # rotate the active camera by one degree
        ren.GetActiveCamera().Azimuth(1)
        ren2.GetActiveCamera().Azimuth(1)

    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()



if __name__ == '__main__':
    main()