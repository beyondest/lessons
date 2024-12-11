
# Q&A
1. Shadow Acne 
   - Q: Shadow acne / self-shadowing artifacts in render preview in Blender 4.2 EEVEE engine?
   - A: 
2. Frame Select or View Select or Focus is not working
   - Q: I can't focus on a selected object by numpad .
   - A: Unlock the view from other objects, usually camera

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
- `R` : Rotate, if press middle mouse, will rotate around axis
- `H` : Hide
- `Alt + H` : Show all
- `Shift + H` : Hide All
- `Tab` : Edit/Object mode switchup
- `Drag from the left up corner of the sub window` : Add new window
- `Numpad 1 - 9` : Change the view in different orientation, e.g., 1 for main view, 3 for side view, 7 for top view




- `Shift + A` : Add object
- `K` : Insert keyframe and show menu
- `I` : Insert keyframe location
- `Press Object A, shift press Object B, Ctrl + P` : Make Object B parent of Object A
- `Shift + Left Arrow` : Go to the most left frame
- `Ctrl + ,` : open Preferences
- `Ctrl + Shift + I` : Import FBX file



- `Ctrl + Double finger drag` : Zoom in x or Zoom in y, depending on which axis you are dragging
- `Double finger zoom` : Zoom both x and y



## Tricks
- `Press N, set Lock` : camera to view, and press Z to enter camera view mode. Then , move scene .
- `Shift + Tab` : Switch between Snap mode, this will snap the object to the nearest vertex, edge or face.
- `Alt + Z` : Enable X-Ray mode, this will show all vertices even behind the obstacle.


# Unknown Name
- primitives
- cylinder
- susan



# Animation
## NLA Editor

### Q&A:
- Q: Replace mode not working, always blend animations
- A: After 4.2, if 2 animations have different changed variables, e.g., animation A change location, animation B change scale, than these 2 always blend when you play.

# Edit Mode

- Convert Rec faces to Curved faces(Cube to Capsule) : `Shift + 2` in edge edit mode, then select the edge of faces, than `Ctrl + B` than move mouse to adjust the curvature.





# Modeling


## Tricks
- **Shader smooth**: `Right Click the selected object` right click while selecting, this will smooth the corner without adding more polygons.
- **Proportional editing**: `O in edit mode` enable a circle to choose a area of points to edit in edit mode
- **Polygons Number Setting**: `F9` after adding, you have a chance to change polygons. If you deselect, press F9 to bring it back.
- **Snap**: `Shift + Tab in edit mode` when enabled and set to Face or Face Project, will project the selected vertices to the nearest face.


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