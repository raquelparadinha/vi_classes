import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkSphereSource, vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkLight
)

def addLight(ren, position, color):
    # Create a light
    light = vtkLight()
    light.SetPosition(position)
    light.SetFocalPoint(0, 0, 0)
    light.SetColor(color)
    ren.AddLight(light)

    # Create a sphere representing the light
    sphereSource = vtkSphereSource()
    sphereSource.SetRadius(0.5)
    sphereSource.SetCenter(position)

    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetColor(color)
    sphereActor.GetProperty().SetLighting(False)  

    ren.AddActor(sphereActor)

def main():
    ren = vtkRenderer()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetWindowName('Cone 2.0')
    renWin.SetSize(500, 500)

    # Set up lights and spheres
    addLight(ren, (-5, 0, 0), (1, 0, 0))  # Red light
    addLight(ren, (0, 0, -5), (0, 1, 0))  # Green light
    addLight(ren, (5, 0, 0), (0, 0, 1))   # Blue light
    addLight(ren, (0, 0, 5), (1, 1, 0))   # Yellow light

    # Create a cone
    coneSource = vtkConeSource()
    coneSource.SetHeight(2) 
    coneSource.SetRadius(1)
    coneSource.SetResolution(50)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection( coneSource.GetOutputPort() )

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    ren.AddActor(coneActor)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

if __name__ == '__main__':
    main()
