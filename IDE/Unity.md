# Q&A
1. - Q: The scroll zoom works, but the right-click and "W" (forward) or "S" (backward) just sudden   stopped working. When I press "W" and right-click, it's deleting the scene.  
   - A: Click on the center of the gizmo on the top right, and it will return to normal.
   - Further Info:
        The gizmo has two modes: **Perspective** and **Isometric view**. When in isometric view, flythrough does not work while approaching objects.
2. - Q: Some objects not rendered properly and show only in pink
   - A: Material shader of that object is not compatible with your current render pipeline. Select that object material, and then go `edit->rendering->materials->convert selected to ...`
   - Further Info:  
        Standard shader for built-in render pipeline;  
        URP for URP;  
        HURP for HURP;  

3. - Q: Why use hash of string instead of itself, and why prefer pre-hash string?
   - A: Faster. String operation is expensive, as well as hash method, but if you pre-hash and store it one time, it speeds up.

        
# Useful tips

- Expand all chiled items:  
  - Press **Alt** and click on the down triangle in the hierarchy window to expand all its child game objects.
- Unity Project Window Slide Bar
  - To the left, you will see the list view.
  - To the right, you will see the icon view.
- Script Naming:  
  - Script names must match the class name within the script, or errors will occur.
- Visualizing Nav Waypoints in the Scene Window without Affecting Game View:  
  - Change the icon next to the name in the inspector to visualize waypoints.
- Pivot/Center:  
  - If the pivot of a transform is not on the object you want when you click on it, switch from **Center** to **Pivot** in the scene buttons above.
- Reset the Transform:  
  - Each time you create a game object, remember to reset its transform.
- Overriding Prefabs:  
  - If you make changes to an instance, select **Override** in the inspector (below the name) and apply all changes.
-  How to Choose What to Show in the Main Zone/Scene View:
   1. Right-click on the scene tab in the main zone.
   2. Select the overlay menu.


# GI Cache

- Set to `D:/unitypro/Unity_GI_Cache`
- If the cache is cleaned, the scene will turn dark. Reopening the scene by double-clicking on it in the project window will solve the issue.

# Asset Download Folder
- Set to `D:/unitypro/Unity_GI_Cache/UnityAssets`
- Go to `Preference -> Package Manager -> My Assets`

# Update Loop:
1. **Rendering Update**: `Update()`. Called each frame, depends on the complexity of calculations and rendering.
2. **Physics Update**: `FixedUpdate()`. Called independently of rendering.



# Different Icon Meanings in the Hierarchy Window

- **Blue cube with black strip on top**: 
  - Imported 3D model, which cannot be modified in Unity editor.
- **Blue cube with diagonally striped gray side**: 
  - A prefab variant, like a child component of its parent prefab.
- **Blue cube**: 
  - A prefab.



# Shortcut
``Ctrl + 1``  Scene View  
``Ctrl + 2``  Game View  
``Ctrl + 3``  Inspector View  
``Ctrl + 4``  Hierarchy View  
``Ctrl + 5``  Project View  
``Ctrl + 6``  Animation View  
``Ctrl + 7``  Profiler View  
``Ctrl + 8``  Audio Mixer View  
``Ctrl + 9``  Lighint View  
``Ctrl + 0``  Project Manager View  
``Ctrl + U``  Undo History List View  



# Unity Animations

- 2 Core Concepts 
  - Animation Data (Animation clips)
    - Value
    - Bindings
  - Animation Blendings
    - Animation controller
    - Animation State

## Animator 

- **Animator Structure**
  - Animator (Controller)
    - Animator Layers
      - State Machines
        - States/State Machines
          - Animation Clips 
  
- **Animator Controller**
  - *Hierachy effect*: This controls the hierachy all below it, which means if a parent gameobject has an animator controller A, then A controls itself and its children; So any config applys on A will apply to every chiled object which has an avatar.
  - *Update Method*: 
    - Normal: Affected by rendering time, Update -> OnAnimatorMove -> OnAnimatorIK -> LateUpdate
    - Animate Physics: Bind with physics system, FixedUpdate -> OnAnimatorMove -> InternalUpdate of Physics System -> OnAnimatorIK 
    - Unscaled time: Independtly call in a constant frequency, not affected by Time.timeScale
  - Culling Mode (Performance Sensitive): Choose which property change will not be applied caused by animation when the hierarchy object is out of view of camera
  - Flow Control in code: Play/PlayFixed; CrossFade/CrossFadeFixed == State run; Transition


- **Blend**
  Basic concepts: use weights to combine animations that change same property
  - *Blend Tree*(only introduce 2d)
    - First Parameter: X  
    - Second Parameter: Y  
    - 2D means 2 parameters, drag red point to see which motion is now making a biggest difference.
  - *Transitions*
    - In phase settings
    - Interruption Source: choose which state's transition can interrupt this transition
    - Ordered Interruption: if enabled, lower priority transition cannot interrupt higher ones
    - Any State: A special state, represents every state added, which can transit from but cannot be transitted to
    - State Machine: A purely organizational tool which can be used for pack similar states up
  - *Layers*
    - Layers are used to blend animations that will happen in same time. e.g.: Heavy Breath, Injured Run/Walk
    - Addictive/Override: heavy breath animation as addictive(both in import settings and layer settings), base animation as override
    - Sync/Timing: normal run layer set sync, contains injured run layer; enable timing to make transitions happen in same time
    - IK Pass: enable evaluate ik in monobehavior




- **Choose blend type**  
  - FreeForm Cartesian and FreeForm Directional can have more than one motion in one direction.  
  - Simple Directional can only have one.  

- **Animation State**
  - Use Parameter to control 
  - Foot IK(Bug Fix): Only worked for Humanoid. Use to estimate when each feet is supposed to be planted on ground, and will lock foot position. Fix feet moving during idle animation and feet sliding during walk.
  - Write Defaults: Whether or not animation will change property A at moment B, animator will change it every frame. Enable this to write to default or disable this to keep previous value.
  - List of Transitions: will check it *in order*.
  
- **Animation Align up**  
  - In phase: `Transition offset`   
  - More gradually: `Transition duration`  


## Animation Window

- **Read-only Property**  
Animation clips imported with model is read-only. Show read-only property should be set to view them in Animation window.  
`Duplicate Animation Clip` to remove read-only property.  

- **Field Access in animation window**  
Animation clips can be imported in `Context` and `Asset` mode.  
Context: Select `gameobject` contained animation controller contained animation clip. Field of gameobject is accessable  
Asset: Select animation clip in `project window`. Field of gameobject is not accessable

- **Animation Speed**  
Second:Frame e.g. 1:34 means 1 second plus 34 frames  
`Sample Rate` is viewed by select show sample rate, which means how many frames per second.  

- **Record and Preview Mode**  
`Red` to Record, `Blue` to Preview. View `scene and animation` window both to see effects.  

- **Is Active**  
In context mode, a gameobject has an attribute called `is active`, only visible in animation window add component menu. This is to prevent gameobject being disabled which will cause a lot of `bugs`.  

- **Animation Curve Shape**
Right click on keypoint on curve, change `tangents` settings of both sides or just drag tangent handler

- **Ripple Editing**  
Moving one keyframe `Vertically` to cause other keyframes automatically moving vertically, like a ripple effect.   
Enable or disable in `...` up right side

- **Animation Event**  
When animation runs to a frame which has an event, it will call a function implemented by the animated gameobject's script, e.g. CallParticalEffect(). Event can be set in model import settings or just in gameobject context animation window, the former one is used like prefab, the latter one is used like instance.


## Animation Import 

- **Bake Animation**  
Convert IK(Maya, 3dx max, cinema 4d) or other simulation aniamtions into FK

- **Resample**  
Convert Euler angles in animations to quanternion angles

- **Compress**  
If animation is too complicated. Keyframe that is not too crucial to final effect will be removed, depending on available error.

- **Cut Animation Clip**  
Mocap data is often unexpected, you have to cut to get a piece of it.   
Basic Concepts:    
  1. *Standard point*: A start frame when the character’s right foot is planted on the floor and left knee is passing the right one , viewed perpendicular to the direction of motion. 
  2. *Root Motion*: Animation based movement rather than scripted movement, which make it looks more realistic. The final displacement and rotation is viewed in `Average Velocity` and `Average Angular Y Speed`.  
   
  Options:  
  - `Cycle offset`: set cycle offset to *standard point*. 
  - `Loop time`: this will smooth the motion loop by newValue = originalValue - normalizedTime * (endValue - startValue)
  - `Bake into Pose`: Freeze root motion in some specific directions, such as y or rotation mostly.
  - `Bake offset`: correct the root motion direction, making character only move towards expected direction.
  - `Mirror`
  - `Curve`

- **Avatar Creation**  
  If you want model imported is able to do animations, then it must contain an avatar.
  - Choose `animation type` : Generic or humanoid
  - Choose `Root node`
  - Set `Skin weights` (Performance sensitive)
  - Enable `Optimize Game Object` (Performance sensitive)
  - Set `exposed` body part: toggle the one you dont want to be optimized(whichi will remove this part to combine to others)  
  - Create and apply `avatar mask` if you want. Notice: avatar mask **only** affect transform property in *Animation blending* and *Animation import*, and it will not affect other properties which depend on transform.
  
- **Humanoid Rigs/Avatar**
  Huamnoid Avatar need to be configured after created, compared to generic type.
  - Mapping transform to correct position (Use auto mapping)
  - Pose T-Pose
  - Muscle Range settings
  







