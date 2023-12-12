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
import vtk

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkConeSource, vtkSphereSource, vtkCylinderSource, vtkCubeSource
from vtkmodules.vtkIOImage import vtkPNGReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkCamera,
    vtkLight,
    vtkTexture
)

def main():

    # # Create a cone
    # coneSource = vtkConeSource()
    # coneSource.SetHeight(2) 
    # coneSource.SetRadius(1)
    # coneSource.SetResolution(10)

    # # Create a mapper
    # coneMapper = vtkPolyDataMapper()
    # coneMapper.SetInputConnection( coneSource.GetOutputPort() )

    # # Create an actor
    # coneActor = vtkActor()
    # coneActor.SetMapper(coneMapper)
    # coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    # coneActor.GetProperty().SetRepresentationToSurface()

    # Create a plane
    planeSource = vtkCubeSource()
    planeSource.SetXLength(10)
    planeSource.SetYLength(10)
    planeSource.SetZLength(0.1)

    # Create a mapper
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection( planeSource.GetOutputPort() )

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    # planeActor.GetProperty().SetRepresentationToSurface()


    reader = vtkPNGReader()
    reader.SetFileName("./images/troll.png")

    # Texture Object
    texture = vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())
    texture.InterpolateOn()
    # Assign texture to the plane actor
    planeActor.SetTexture(texture)
    # Fit texture to plane
    # tcoords = vtk.vtkTextureMapToPlane()
    # tcoords.SetInputConnection(planeSource.GetOutputPort())
    # planeActor.GetMapper().SetInputConnection(tcoords.GetOutputPort())

    ren = vtkRenderer()
    # ren.AddActor( coneActor )
    ren.AddActor( planeActor )
    ren.SetBackground(1, 1, 1)

    cam = ren.GetActiveCamera()

    # Set the camera position
    cam.SetPosition(0, 0, 15)
    cam.SetViewUp(0, 1, 0)
    cam.SetParallelProjection(True)
    

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