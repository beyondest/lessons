

# Usual Formats in Unity
- `.wav` - Audio
- `.mat` - Materials
- `.fbx` - Model, Animations, Mesh (Filmbox)
- `.shadergraph` - Shader
- `.tif/.tiff` - Textures (Tagged Image File Format)
- `.controller` - Animators
- `.prefab` - Prefab
- `.wlt` - World Locking Tools (for AR)
- `.asset` - Universal resource formats
- `.hlsl` - HLSL code file

# HLSL: High-Level Shading Language
- Specialized for Direct3D API, GLSL for OpenGL and Vulkan, Metal Shading Language for Apple.
  
- **Recommended Books**  
  - "Real-Time Rendering"
  - "Introduction to Computer Graphics"
  - "Shaders for Game Programmers and Artists"
  - "Introduction to 3D Game Programming with DirectX 12"

- **Learning Steps**  
  - Unity Standard Shader and URP/Lit Shader
  - Shader Graph / HLSL

# Model Structure:

## Learning Steps:
1. Blender - Mesh & Model       (Maya/3DS Max/Cinema 4D)
2. Photoshop/GIMP - Texture
3. Material
4. Shader

# Read-Only Prefab
- With a white paper on the cube. Usually models.



# Model 
Basic concepts:  
- **Model** = Mesh + Animations + Coordinates .(Material = Texture + Shader (works on Mesh))

- **Skinning**  
  Skinning is the process of connecting each vertex of a mesh to one or multiple bones and then giving those bones a weight to affect that vertex.Only(?) Animated models have a skinned mesh.
- **Bones**  
  bones are represented by the Transforms of a model, so each vertex moves with a weighted combination of the Transforms it is skinned to. 
- **Rig** 
  Same as skeleton ? Physical structure of all bones

- **Avatar**
  abstract rig, or actual rig in game , which may be different (usaually part of) rig




