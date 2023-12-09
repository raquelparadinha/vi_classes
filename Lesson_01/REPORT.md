# Lesson 01 Report

## First Example

To set a height of 2 and a radius of 1 for the the Cone, we only need to use the methods `SetHeight` and `SetRadius`, respectively.

``` 
coneSource.SetHeight(2) 
coneSource.SetRadius(1)
```

The method `SetResolution` is used to set the number of facets used to represent the cone.
We tested this method with 3 different arguments, 1, 10 and 100, so we cloud see clearly the difference it makes.

After using the `SetSize` method of the vtkRenderWindow to set the window size to 300x300, we can see that the default window size is the same, once it doesn't change with this action.  

## Camera control

When we add the given version of the camera to our code, we see the figures from a different perspective and with the following changes. Initially we would see only the sphere, being the 3 figures in line. With the camera we started to see the base of the cone, which is in the middle of the other 2 figures. With the next changes, Position of (10,10,0) and a View Up Vector (0,1,1), the view passed to see the figures from a perspective more from above and from other front.

