
# Q&A
1. Shadow Acne 
   - Q: Shadow acne / self-shadowing artifacts in render preview in Blender 4.2 EEVEE engine?
   - A: 
2. Frame Select or View Select or Focus is not working
   - Q: I can't focus on a selected object by numpad .
   - A: Unlock the view from other objects, usually camera
3. Tablet pressure is not working
   - A: Try to restart Blender with tablet plugged in, not just plug in tablet while blender is running.

# Basic Settings

- Unity System: `Scene -> Unit System` to change meter or unity scale.
- tay: equal to 2 * pi, in value box 
- pi: equal to pi, in value box
- Blender use radians for angles, not degrees.

# Shortcuts

## Basic
- `Ctrl + 2 fingers drag` : Zoom in/out
- `Shift + 2 fingers drag` : Shift view
- `T` : Toggle tools
- `Ctrl + Tab` : Open Mode Switcher Panel
- `~ + Selected` : Open View Control Panel
- `N` : Properties
- `S` : Scale
- `G` : Move, if press middle mouse, will move along axis; if press x/y/z, will move in that direction; if press shift, will move slowly
- `R` : Rotate, if press middle mouse, will rotate around axis,if press x/y/z, will rotate in that direction; if press shift, will rotate slowly, if press ctrl, will rotate in integers, if type 90, will rotate 90 degrees.
- `H` : Hide
- `Alt + H` : Show all
- `Shift + H` : Hide All
- `Tab` : Edit/Object mode switchup
- `Drag from the left up corner of the sub window` : Add new window
- `Numpad 1 - 9` : Change the view in different orientation, e.g., 1 for main view, 3 for side view, 7 for top view
- `Shift + ~` : Fly mode, if in z camera view, this will enable moving camera at the same time.
- `Numpad 0` : Camera view
- `Z` : Switch between different view modes





- `Shift + A` : Add object
- `K` : Insert keyframe and show menu
- `I` : Insert keyframe location
- `Press Object A, shift press Object B, Ctrl + P` : Make Object B parent of Object A
- `Shift + Left Arrow` : Go to the most left frame
- `Ctrl + ,` : open Preferences
- `Ctrl + Shift + I` : Import FBX file
- `Shift + right click` : Move the center cursor to the mouse position, the objects will summon in this position after that.


- `Ctrl + Double finger drag` : Zoom in x or Zoom in y, depending on which axis you are dragging
- `Double finger zoom` : Zoom both x and y
- `Ctrl + Space` : Fuul screen selected window



## Tricks
- `Press N, set Lock` : camera to view, and press Z to enter camera view mode. Then , move scene .
- `Shift + Tab` : Switch between Snap mode, this will snap the object to the nearest vertex, edge or face.
- `Alt + Z` : Enable X-Ray mode, this will show all vertices even behind the obstacle.
- `Ctrl + L` : Link materials of one object to others selected. Notice that the mother object has to be selected last.
- `Ctrl + A` : Apply, after changing the size of object, you need to apply the scale to make that remain 1.
- `M` : Add to new collection



# Unknown Name
- primitives
- cylinder
- susan



# Animation

## NLA Editor

- Replace mode not working, always blend animations:  After 4.2, if 2 animations have different changed variables, e.g., animation A change location, animation B change scale, than these 2 always blend when you play.
## Graph Editor

- `Normalize`: this will normalze all data in the graph to 0-1 range in spite of the data original range. This is useful when you want to edit the handle of curves rather than change the value. DO NOT CHANGE VALUE in this mode, cause it will remap to the original range and it is hard to see.



# Edit Mode

- Convert Rec faces to Curved faces(Cube to Capsule) : `Shift + 2` in edge edit mode, then select the edge of faces, than `Ctrl + B` than move mouse to adjust the curvature.





# Modeling


## Tricks
- **Shader smooth**: `Right Click the selected object` right click while selecting, this will smooth the corner without adding more polygons.
- **Proportional editing**: `O in edit mode` enable a circle to choose a area of points to edit in edit mode
- **Polygons Number Setting**: `F9` after adding, you have a chance to change polygons. If you deselect, press F9 to bring it back.
- **Snap**: `Shift + Tab in edit mode` when enabled and set to Face or Face Project, will project the selected vertices to the nearest face.
- **Extrude**: `E while selecting an edge in edit mode` will duplicate the edge and move it to where you want. 
- **Create bevel on a corner line**: `Ctrl + B` in edit mode, select the corner line, than move mouse to adjust the bevel. Scroll to adjust the bevel strength.
- **Merge vertices**: `M while selecting vertices in edit mode` in edit mode, select the vertices, than press M to select which merge method to use. This will reduce the number of vertices.


## Select
- `Alt + Left Click on edge` : Select all edges connected to the selected vertex.
- `Ctrl + math +/-` : Select next/previous edge next to current selection.


## Modifiers
- Subdivision Modifier: Viewpoint and Render for 2 different usage views, one for layout and another for render.


# Sculpting

## Tricks

- Sculpt Tool Panel: `Shift + Space` will show all sculpt tools in one panel.
- Brush Size and Strength: `F` or `Shift + F`
- Inflate Tool: `I` keep pressing on object and moving like you are inflating the object.
- Front Face Only: In blrush setting , enable `Front Face Only`.
- Isolation mode: `Numpad / while selecting` show only the selected object in sculpt mode.
- Mask Tool: will draw dark on the area, which is a mask not to sculpt.
- Reverse Mask Area: `Ctrl + I`


# Weight Painting

## Tricks
- Paint: `Drag` Red refer to 1, Blue refer to 0
- Opposite painit: `Ctrl + Drag`


# Geometry Node
Geometry node is a cutomized system that allow you to add a custom modifier(type of GeometryNode)
## Tricks
- Expose a value to modifier: Drag the value input port to group input port, then you can change the value in its own modifier.
- Duplicate a object which has a geometry node will link the geometry node to the duplicated object.
- Click the number next to the shield icon in  modifier -> geometry node will disable the link between geometry nodes.
- `Ctrl + Right Click Drag`: cut the link between different geometry nodes.
- `Ctrl + X`: delete the selected node with the link remained.


# Texture

## Align the real world size before doing anything after import a texture, this is very important.
e.g. the texture downloaded is 2.5mx2.5m brick wall texture
- create a plane, default 2mx2m, duplicate to make a 8mx4m wall
- link image texture to the plane
- select all the vertices of the plane, and press `U` , select `Smart UV Project`
- in uv editor, notice the right direction corresponding between the plane and the texture, by clicking `UV sync selection`
- notice that the edit square in uv editor view represents the 2m x 2m in blender scene, but the brick texture is 2.5mx2.5m, so we need to scale the edit square to 0.8, so as to align the real world size.

e.g. still, the texture downloaded is 2.5mx2.5m brick wall texture
- create a plane, resize to 8mx4m
- link image texture to the plane
- 8/2.5 = 3.2, 4/2.5 = 1.6, so we need to scale the edit square to 3.2 in x, 1.6 in y

now the 2 planes made prior will align the real world size

## Tricks
- `Ctrl + Shift + T while clicking on BSDF node` : The best way to import textures quickly, after enabled blender add-on node wrangler.



# Material

## Subsurface Scattering && Make shadow softer
Go to `Material -> Surface -> Subsurface`, change weight to 1 to enable, and set Radius below (corresponding to R,G,B) to 1, and set Scale (change the effect of the subsurface) to 0.05. Then shadows will become softer, and you can drag weight to 0 to see the difference.



# Camera

- **Camera View Zone** : press `numpad 0` to enter camera view, and then press `home` to center the yellow view zone, and use middle mouse to adjust the zone size.


# Lighting

- **Use black wall to control room light intensity** : Create a black wall on which the light cast on, and adjust the black value to control the light intensity.



# Rendering

- **Face Orientation**: click on `face orientation` and check if there are any red faces in your render sence, if there are, you need to select them in edit mode, and click on `Inside`

## Steps before rendering
- **Check the render settings**
- **Check the face orientation**
- **Check the lighting**
- **Check the objects position, is there any overlapping or weird objects?**
- **Check the objects that should not be rendered in the scene, and click off camera button in the collection menu**
- **Check the camera view**