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

# GI Cache

- Set to `D:/unitypro/Unity_GI_Cache`
- If the cache is cleaned, the scene will turn dark. Reopening the scene by double-clicking on it in the project window will solve the issue.


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
``Ctrl + U``  Undo History View  


