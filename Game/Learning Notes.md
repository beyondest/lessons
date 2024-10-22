# Learning Notes

## Usual Formats in Unity
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

## HLSL: High-Level Shading Language
- Specialized for Direct3D API, GLSL for OpenGL and Vulkan, Metal Shading Language for Apple.
  
### Recommended Books:
- "Real-Time Rendering"
- "Introduction to Computer Graphics"
- "Shaders for Game Programmers and Artists"
- "Introduction to 3D Game Programming with DirectX 12"

### Learning Steps:
1. Unity Standard Shader and URP/Lit Shader
2. Shader Graph / HLSL

## Model Structure:
- **Model** = Mesh + Animations + Coordinates
- **Material** = Texture + Shader (works on Mesh)

### Learning Steps:
1. Blender - Mesh & Model
2. Photoshop/GIMP - Texture
3. Material
4. Shader

## Read-Only Prefab
- With a white paper on the cube. Usually models.

## Animation Controller
### Notes:
- State machine

### Tips:
- If the default value is false, do not check the box next to the bool parameter.

## Update Loop:
1. **Rendering Update**: `Update()`. Called each frame, depends on the complexity of calculations and rendering.
2. **Physics Update**: `FixedUpdate()`. Called independently of rendering.

## Naming Conventions

|              | C#            | C++                            | Python       |
|--------------|---------------|--------------------------------|--------------|
| Public       | `myVariable`  | `myVariable` / `my_variable`   | `my_variable`|
| Private      | `m_MyVariable`| `m_MyVariable`                 | `_my_variable`|
| Class        |               | `MyClass`                      |              |

## C# Generics vs. C++ Templates

## How to Choose What to Show in the Main Zone/Scene View:
1. Right-click on the scene tab in the main zone.
2. Select the overlay menu.
