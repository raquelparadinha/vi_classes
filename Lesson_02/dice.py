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
from vtkmodules.vtkIOImage import vtkJPEGReader
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

# returns the actor of the face
def make_face(rotation, translation, texture_filename):
    # Create a plane
    planeSource = vtkCubeSource()
    planeSource.SetXLength(10)
    planeSource.SetYLength(10)
    planeSource.SetZLength(0.1)

    # Create a texture
    textureReader = vtkJPEGReader()
    textureReader.SetFileName(texture_filename)

    texture = vtkTexture()
    texture.SetInputConnection(textureReader.GetOutputPort())
    texture.InterpolateOn()

    # Create a mapper
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection(planeSource.GetOutputPort())

    tcoords = vtk.vtkTextureMapToPlane()
    tcoords.SetInputConnection(planeSource.GetOutputPort())
    planeMapper.SetInputConnection(tcoords.GetOutputPort())

    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.GetProperty().SetRepresentationToSurface()
    planeActor.SetTexture(texture)

    transform = vtk.vtkTransform()
    transform.Translate(translation[0], translation[1], translation[2])
    transform.RotateX(rotation[0])
    transform.RotateY(rotation[1])
    transform.RotateZ(rotation[2])
    planeActor.SetUserTransform(transform)

    return planeActor

def main():
    texture_filenames = ["Im1.jpg", "Im2.jpg", "Im3.jpg", "Im4.jpg", "Im5.jpg", "Im6.jpg"]
    texture_filenames = ["./images/" + filename for filename in texture_filenames]

    actors = []
    actors.append(make_face([90, 0, 0], [0, 5, 0], texture_filenames[0]))
    actors.append(make_face([-90, 0, 0], [0, -5, 0], texture_filenames[5]))
    actors.append(make_face([0, 90, 0], [5, 0, 0], texture_filenames[1]))
    actors.append(make_face([0, -90, 0], [-5, 0, 0], texture_filenames[4]))
    actors.append(make_face([0, 0, 0], [0, 0, 5], texture_filenames[2]))
    actors.append(make_face([0, 0, 0], [0, 0, -5], texture_filenames[3]))

    ren = vtkRenderer()
    for actor in actors:
        ren.AddActor(actor)
    ren.SetBackground(0.2, 0.2, 0.2)

    cam = ren.GetActiveCamera()
    cam.SetPosition(0, 0, 30)
    cam.SetViewUp(0, 1, 0)
    cam.SetParallelProjection(True)
    

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

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()