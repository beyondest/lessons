Learning Notes

Usual Formats in Unity
.wav            Audio
.mat            Materials
.fbx            Model,Animations,Mesh(Filmbox)
.shadergraph    Shader
.tif/.tiff      Textures(Tagged Image File Format)
.controller     Animators
.prefab         Prefab
.wlt            World Locking Tools, for AR
.asset          Universal resource formats
.hlsl           hlsl code file


HLSL: High-Level Shading Language
Specialized for Direct3D API, GLSL for OpenGL and Vulkan , Metal Shading Launguage for Apple
Books Before : 
"Real-Time Rendering"
"Introduction to Computer Graphics"
Books:
"Shaders for Game Programmers and Artists"
"Introduction to 3D Game Programming with DirectX 12"
Learning Steps: Unity Standard Shader and URP/Lit Shader; Then, Shader Graph/HLSL


Model = Mesh + Animations + Coordinates
Material = Texture + Shader, Work on Mesh

Learnign Steps: 
1.Blender mesh + model; 
2.Photoshop/GIMP texture; 
3.Material; 
4.Shader


Read-Only Prefab: with a white paper on the cube. Usually models.

Animation Controller :
notes:
1. state machine
tips
1.If default value is false, than do not click on the box next to bool parameter

Update Loop:
1.Rendering Update: Update. Called each frame. Depends on complexity of calculations and rendering. 
2.Physics Update: FixedUpdate. Called independently.



Naming Convetions   C#               C++                           Python
Public:             myVariable       myVariable/my_variable        my_variable
Private:            m_MyVariable     m_MyVariable                  _my_variable
Class:                              ------- MyClass-------

C# Generics v.s. C++ Template

How to choose what to show in the main zone/scene view
Rightclick on scene tab in main zone, and select overlay menu



