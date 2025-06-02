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

4. - Q: Cannot see Unity.Entities namespace in visual studio
   - A: `Preferences -> External Tools-> Regenerate project files`, reopen vs by double click

5. - Q: xx is missing the class attribute 'ExtensionOfNativeClass'!
   - A: Find xx.cs script, and then `Right click -> Find reference in scenes -> Delete the old scripts attached to gameobject`

6. - Q : Faster compilation time
   - A : Change `Project Settings -> Burst AOT Settings -> Optimize for fast compiation`, `Project Settings -> Editor -> Enter Play mode -> reload scene only ` disable `reload domain`
   - A : Use split assembies

7. - Q : Probuilder meshes warning: [Warning Edit] Renderer on GameObject "IndicatorEnemy" was not converted. The assigned mesh is null or no materials are assigned.
   - Q : [Error Edit] InvalidOperationException: No sharedMesh assigned to Unity.Physics.MeshCollider on IndicatorEnemy.
   - A : `Select object in sceneview, right click -> Probuilder -> Export`When using probuilder meshes in prefab, you MUST export the probuilder object into prefab, and use that prefab.
  
8. - Q : No camera outline in scene view
   - A : Turn on gizmos
  
9. - Q : Entity Manager need to be reasigned in update in monobehavior, or sometimes (I am not sure when exactly) it will be deallocated

10. - Q : Unity ECS Physics collider event trigger will generate events of 2 objects that are active or passive collider, which causes same event counting twice
        when using sight techniques, moreover, it will cause the enemy detects the ally when ally detects enemy, even they have different sight range
    - A : Only when EntityA entity == self entity(which has a statefuleventtriggerbuffer), this event is considered valid

11. - Q : IndexOutOfRangeException: Index -1 is out of range in container of '0' Length.
    - A : This is usually by wrong system update sequence, something conflict. Check your system update sequence

12. - Q : TLS Allocator ALLOC_TEMP_TLS, underlying allocator ALLOC_TEMP_MAIN has unfreed allocations, size 25600
Internal: Stack allocator ALLOC_TEMP_MAIN has unfreed allocations, size 25600
    - A : Answer : You can never use this.gameobject.setActive(true) in OnEnable() function, this will cause dead loop
        
13. - Q : Unity Ecs Random generate numbers gathered in a small range in some state
    - A : The seed is not right , some seed will generate numbers in a small range, try math.hash() to get a better seed.

14. - Q : Transparent material overlaps with other transparent material causing wrong rendering effect only in game view
    - A : Check if depth write is force enabled in both materials
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

``G`` Probuilder 6 Toggle Edit mode shortcut
``Shift + Drag move face`` Probuilder 6 extrude face shortcut



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
  






# UnityEngine API

## Basic API

- **Start**:
   Called before Update called the first time = called just when the gameobject it attached to is created the first time
- **OnDestroy**:
   Called when the script is destroyed.




# UI

### **`Sprite Mode`**
`Sprite Mode` 决定了你的 **Sprite 纹理** 如何被使用，在 `Inspector` 里可以选择：
- **Single（默认）**：整个图片作为一个单独的 Sprite 使用。
- **Multiple**：允许 **从一张大图裁剪多个 Sprite**（适用于 **Sprite Sheet** 或 **Tilemap**）。

| 模式 | 影响 |
|------|------|
| **Single** | 适用于普通 UI Image、按钮等，可以直接拖动到 `Source Image`。 |
| **Multiple** | 需要用 `Sprite Editor` 手动裁剪出多个 Sprite，否则不能作为 UI 直接使用。 |

**⚠️ 如果你的 `Sprite Mode` 设为 `Multiple`，但没有在 `Sprite Editor` 里手动裁剪，Unity 可能不会识别它，导致无法拖动到 `Source Image`。**

---

### **`Mesh Type`**
`Mesh Type` 决定了 **Sprite 渲染时的网格形状**，影响 **性能** 和 **边缘透明度**。

可以选择：
- **Full Rect**（默认）：使用矩形网格（最简单，但占用更多像素）。
- **Tight**：Unity 自动生成 **最小包围多边形网格**，减少透明区域，提高性能。

| 选项 | 影响 |
|------|------|
| **Full Rect** | UI 或 2D 游戏里，适用于 **矩形精灵**，边缘透明区域会被计算进网格，可能浪费渲染资源。 |
| **Tight** | 适用于 **不规则形状** 的图片，可以减少透明区域的绘制，提高性能。 |

#### **`Tight`**
- **如果你的图片有 Alpha 透明**，`Tight` 模式可能会导致透明部分不规则裁剪，影响某些 Shader 效果（例如 Outline 或 Glow）。
- **如果 Sprite 用作 UI（比如 `Image` 或 `Button`）**，`Full Rect` 更稳定，不会影响点击区域。

---

 **`Sprite Mode`**
- `Single`：普通 UI 或 2D 纹理使用。
- `Multiple`：用作 **Sprite Sheet** 时必须开启（否则无法拖入 `Source Image`）。
  
 **`Mesh Type`**
- `Full Rect`：适用于 UI 或者 **矩形 Sprite**，避免不规则网格带来的问题。
- `Tight`：适用于 **非规则形状**，减少透明区域的渲染，提高性能。



# Unity Subscenes
下面是对这些问题的详细说明和举例说明，引用了 Unity 官方文档中的相关内容。

---

## 1. 关于这句话的含义

> **Important**  
> Unity doesn't stream the content of opened subscenes. The entities in an open subscene are immediately available when you enter Play mode

这句话的意思是：

- **Opened（打开）的 Subscene**：指在 Editor 中你以“打开”状态显示 subscene（例如在 Hierarchy 中勾选了对应的复选框，使得其中的 GameObject 显示出来）。  
- 在这种状态下，**Unity 不会对其内容进行“流式加载”**。也就是说，当你点击 Play 时，subscene 内转换后的实体数据（Entities）会立即在场景中可用，不会经过几帧的延迟加载过程。  
- 与之相对的是 **关闭的 Subscene**：关闭状态下，subscene 的内容是在进入 Play 模式后通过异步流式加载（Streaming）进入的，可能需要几帧时间才能使其实体完全可用。

（参考：citeturn0fetch1）

---

## 2. Subscene 的 AutoLoad Mode 与 Checkbox 的影响

### AutoLoadMode 的作用

- **AutoLoadScene 字段（AutoLoad Mode）**：在 SubScene 组件上有一个 Auto Load Scene 选项。当该选项为 true 时，在运行时（或进入 Play 模式时）Unity 会自动流式加载（stream in）该 subscene 的内容。  
- 注意：这个字段主要影响 **流式加载** 的行为，也就是说，它决定了在运行时 Unity 是否自动加载该 subscene 的实体数据。

### Checkbox（勾选框）的作用

- Hierarchy 中 subscene 前的复选框**控制的是 subscene 的“打开”状态**。  
  - **打开（Open）**：显示出 subscene 内的所有 authoring GameObject，方便在 Editor 中编辑。  
  - **关闭（Closed）**：不在 Hierarchy 中显示具体内容，而是以一个整体的 subscene 形式存在，内容会在运行时通过流式加载进入。

- 因此，**复选框只是影响 subscene 是否以打开状态展示，而不直接决定其是否被加载**。  
  - 当 subscene 是打开状态时，内容在进入 Play 模式时已经转换好，实体数据会立即可用；  
  - 当 subscene 是关闭状态时，则会触发流式加载，其内容需要几帧才能完全加载进来。

（参考：citeturn0fetch1）

### Open 与 Load 的区别

- **Open（打开）**：主要描述的是编辑器中的状态。当你“打开”一个 subscene，意味着它的 authoring 数据（GameObject、组件等）显示在 Hierarchy 中，你可以进行修改。这种状态下，进入 Play 模式时，subscene 的实体会马上可用，不需要经过流式加载延迟。
- **Load（加载）**：指的是运行时将 subscene 内已转换的实体数据流式加载进 ECS 世界的过程。对于关闭状态的 subscene，加载过程是异步的，可能会有几帧延迟。

---

## 3. Subscene 与 Parent Scene 的关系

### Subscene 是否可以脱离 Parent Scene 存在？

- 在 Editor 中，subscene 是作为 Parent Scene 内的一个组件（SubScene 组件）存在的。也就是说，从层级上看，它依附于父场景。
- 但在运行时，subscene 会被转换成独立的实体场景（Entity Scene），并由 SceneSystem 管理。  
  - 虽然这种实体场景可以独立进行加载和卸载，但在编辑器中它们还是依赖于父场景的组织方式。
- **总结**：从编辑器的角度来说，subscene 不能脱离其 parent scene 存在；而在运行时，subscene 的数据流式加载与管理可以看作是独立的，但通常还是与父场景的加载逻辑相关联。

### Parent Scene 加载是否会加载其中的 Subscene？

- **自动加载**：如果 SubScene 组件的 AutoLoadScene 为 true，当父场景加载且 SubScene 组件启用时，Unity 会自动对该 subscene 进行流式加载或（如果是打开状态）立即提供其实体数据。  
- **组织方式**：通常情况下，当你加载一个包含 SubScene 的父场景时，相关的 subscene 也会被加载（按照它们各自的设置）。在构建后的游戏中，subscene 都会以关闭状态存在，因而需要经过流式加载过程。

（参考：citeturn0fetch1 以及 citeturn0fetch2）

---

## 4. 合理的 ECS RTS 游戏中的 Scene 结构示例

在一个基于 ECS 的 RTS（即时战略）游戏中，为了兼顾性能、开发效率以及资源管理，你可以考虑以下场景组织结构：

### 主场景（传统 Scene）

- **主要用途**：存放全局系统、游戏管理器、UI、持久化数据以及全局逻辑。
- **示例内容**：
  - 游戏管理器（Game Manager）、网络管理、音频管理。
  - UI 界面、摄像机控制、玩家数据。
  - 持续运行的 ECS 系统（例如单位管理、资源管理等）。
- **作用**：作为整个游戏的“容器”，管理游戏的生命周期和全局状态。

### Subscene 的组织与分配

在主场景中，通过 SubScene 组件引用多个子场景，这些 subscene 用来管理大批量数据，减少单个 authoring 场景内容过多导致的编辑器卡顿，并利用 ECS 的流式加载优势。

#### 举例说明

1. **地图与环境数据 Subscene**  
   - **内容**：地形、植被、环境装饰、障碍物等静态数据。  
   - **原因**：这些数据体积较大但一般不会频繁修改，适合在编辑器中单独管理，同时在运行时以流式加载方式进入 ECS 世界。  
   - **组织**：一个大的父场景中可以包含多个地图区域的 subscene，每个 subscene 对应地图中的一块区域，便于根据玩家视野进行动态加载和卸载。

2. **单位与建筑物数据 Subscene**  
   - **内容**：各个玩家单位、建筑、兵营、资源采集点等。  
   - **原因**：这些数据在游戏中频繁交互，但通常通过 ECS 组件来处理其行为，因此在运行时转换为实体数据后可以高效管理。  
   - **组织**：可以将各个阵营的单位放入不同的 subscene，或者根据战场区域进行分割，方便针对不同区域进行流式加载。

3. **动态特效与临时数据**  
   - **内容**：爆炸、烟雾、粒子特效等。  
   - **原因**：这些内容通常不需要事先通过 SubScene 进行静态烘焙，可以直接通过运行时系统创建和销毁，放在主场景中由专门的特效管理系统处理。
   - **组织**：建议放在主场景或单独的“特效管理”子场景中，但由于其临时性，不需要流式加载。

### 整体结构示例

- **主场景（Game Core Scene）**
  - 全局管理器、UI、主摄像机、运行时系统（例如 AI、物理、网络同步等）
  - **Subscene 1：地图区域 A**  
    - 地形、环境、植被、障碍物  
    - 依据玩家视角动态加载/卸载  
  - **Subscene 2：地图区域 B**  
    - 同上，另一块区域
  - **Subscene 3：单位与建筑数据（阵营 A）**  
    - 包含阵营 A 的所有建筑、单位等  
  - **Subscene 4：单位与建筑数据（阵营 B）**  
    - 包含阵营 B 的所有建筑、单位等  
  - **主场景中的其他 GameObject**：用于即时生成特效、UI 等

这种结构的好处是：
- **分离静态数据与动态数据**：静态环境和建筑数据放在 subscene 中，便于进行异步流式加载；动态产生的特效和交互逻辑放在主场景中，便于实时控制。  
- **分区域管理**：通过不同区域的 subscene，可以实现按需加载（Streaming），降低内存压力和提升性能。  
- **开发协作**：艺术家可以在各自的 subscene 中独立工作，而程序员则专注于全局系统和动态逻辑，减少相互干扰。

（参考：citeturn0fetch2 和官方关于 Subscene 与 Scene 概览的说明）

---

## 总结

- **“Opened subscene” 与 “Closed subscene” 的区别**：打开状态下（勾选复选框）的 subscene，其实体数据在进入 Play 模式时会立刻可用，而关闭状态下则需要异步流式加载。  
- **AutoLoadScene 与复选框**：AutoLoadScene 决定了 SubScene 组件在启用时是否自动加载对应的 entity scene，而复选框仅影响编辑器中是否显示子场景的 authoring 数据。  
- **Open 与 Load 的区别**：Open 是编辑器中的可视化与编辑状态；Load 指的是运行时将数据加载到 ECS 世界中的过程。  
- **Subscene 与 Parent Scene 的关系**：在编辑器中，subscene 依附于父场景；在运行时，它们的实体数据可以独立加载，但通常作为父场景的一部分管理。  
- **合理的 ECS RTS 游戏场景结构**：主场景负责全局逻辑与系统，而各个 subscene 根据区域、阵营或数据类型划分，分别管理环境、建筑、单位等内容，通过流式加载实现性能优化和动态管理。

希望以上说明能帮助你更好地理解 Unity ECS 中 Subscene 的加载机制及其在大型 RTS 游戏中的应用实践！




# Burst Compile compatible
### **1. `EntityQuery` 是否兼容 `BurstCompile`？**  
✅ **`EntityQuery` 是 `Burst` 兼容的，可以安全地作为 `ISystem` 的私有变量**，但它需要在 `OnCreate()` 里正确初始化，并且在 `OnUpdate()` 里使用时遵循一定的规则。

---

### **2. `EntityQuery` 在 `OnCreate()` 里获取后是固定的吗？**
- **是的，它的结构是固定的**（查询的组件类型不会变），但查询的**结果**（匹配的实体）是动态的，会随着 ECS 世界的变化而变化。
- **换句话说**：
  - **`EntityQuery` 本身不会变**，你不需要每帧重新创建它。
  - **它查询到的实体集合会变**，因为 ECS 世界中的实体会被创建/销毁/修改。

---

### **3. 正确的 `EntityQuery` 使用方式**
✅ **推荐的 `ISystem` 实现**
```csharp
[BurstCompile]
public partial struct MySystem : ISystem
{
    private EntityQuery entityQuery; // ✅ 兼容 Burst，可以安全存储

    [BurstCompile]
    public void OnCreate(ref SystemState state)
    {
        entityQuery = SystemAPI.QueryBuilder()
            .WithAll<Translation, Rotation>() // 只查询拥有 Translation 和 Rotation 组件的实体
            .WithNone<Disabled>() // 排除 Disabled 组件的实体
            .Build();
    }

    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        NativeArray<Entity> entities = entityQuery.ToEntityArray(Allocator.Temp);
        
        for (int i = 0; i < entities.Length; i++)
        {
            Entity entity = entities[i];
            // 对实体进行处理
        }

        entities.Dispose(); // 释放 NativeArray
    }
}
```

---

### **4. `EntityQuery` 的一些关键点**
| **问题** | **解答** |
|----------|---------|
| **在 `OnCreate()` 里获取 `EntityQuery`，是不是固定的？** | ✅ **是的**，它不会变，但查询到的**实体**会变 |
| **`EntityQuery` 需要手动更新吗？** | ❌ **不需要**，它会自动适应 ECS 世界的变化 |
| **可以在 `BurstCompile` 的代码里用 `EntityQuery` 吗？** | ✅ **可以** |
| **`EntityQuery` 里可以获取哪些数据？** | ✅ **实体列表** (`ToEntityArray()`)、✅ **组件数据** (`ToComponentDataArray<T>()`)、✅ **统计数量** (`CalculateEntityCount()`) |

---

### **5. `EntityQuery` 常见的错误**
🚨 **错误 1：每帧重新创建 `EntityQuery`**
```csharp
[BurstCompile]
public partial struct MySystem : ISystem
{
    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        // 🚨 每帧创建 EntityQuery，性能浪费
        var query = SystemAPI.QueryBuilder()
            .WithAll<Translation>()
            .Build();

        int count = query.CalculateEntityCount();
    }
}
```
❌ **问题**：
- `EntityQuery` 是可以存储的，**不需要每帧重新创建**，否则会导致 **GC 压力** 和 **不必要的查询开销**。

✅ **正确方式：在 `OnCreate()` 里创建，`OnUpdate()` 里使用**
```csharp
private EntityQuery entityQuery;

[BurstCompile]
public void OnCreate(ref SystemState state)
{
    entityQuery = SystemAPI.QueryBuilder()
        .WithAll<Translation>()
        .Build();
}

[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    int count = entityQuery.CalculateEntityCount(); // ✅ 这样才是高效的
}
```

---

🚨 **错误 2：错误使用 `entityQuery.ToEntityArray()`**
```csharp
[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    var entities = entityQuery.ToEntityArray(Allocator.Persistent); // 🚨 错误：不应该用 Persistent
    entities.Dispose(); // 如果忘了 Dispose()，就会造成内存泄漏！
}
```
❌ **问题**：
- `ToEntityArray()` 会分配内存，**但一般不应该使用 `Allocator.Persistent`**，因为你只会在当前帧使用这个数据。
- **必须 `Dispose()`，否则会内存泄漏！**

✅ **正确方式**
```csharp
[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    NativeArray<Entity> entities = entityQuery.ToEntityArray(Allocator.Temp);
    
    for (int i = 0; i < entities.Length; i++)
    {
        Entity entity = entities[i];
        // 处理实体
    }

    entities.Dispose(); // ✅ 释放内存
}
```
---

🚨 **错误 3：在 `BurstCompile` 代码里直接使用 `state.EntityManager`**
```csharp
[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    EntityManager entityManager = state.EntityManager; // 🚨 `EntityManager` 不是 Burst 兼容的！
    entityManager.DestroyEntity(entityQuery);
}
```
❌ **问题**：
- `EntityManager` 不是 `Burst` 兼容的，**不能直接在 `BurstCompile` 方法里使用**。
- 解决方案是使用 **`EntityCommandBuffer` (ECB)** 来处理实体操作。

✅ **正确方式：使用 `EntityCommandBuffer`**
```csharp
[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    var ecb = new EntityCommandBuffer(Allocator.TempJob);
    
    NativeArray<Entity> entities = entityQuery.ToEntityArray(Allocator.Temp);
    for (int i = 0; i < entities.Length; i++)
    {
        ecb.DestroyEntity(entities[i]);
    }

    ecb.Playback(state.EntityManager);
    ecb.Dispose();
    entities.Dispose();
}
```

---

### **6. 总结**
✅ `EntityQuery` **可以作为 `ISystem` 的私有变量，并且完全兼容 `BurstCompile`**。  
✅ 在 **`OnCreate()` 里创建**，然后在 **`OnUpdate()` 里使用**，不会影响性能。  
✅ `EntityQuery` **不会变，但查询到的实体会动态更新**，不需要每帧重新创建。  
✅ **查询实体时，使用 `ToEntityArray(Allocator.Temp)`**，避免内存泄漏。  
✅ **修改实体时，使用 `EntityCommandBuffer`，不要直接使用 `EntityManager`**。  

你现在的 `EntityQuery` 是要用来做什么的？是查询哪些实体？我可以帮你优化代码！ 🚀


# Allocator
## **Allocator 详解（与 C++ `new/delete`、`malloc/free` 的对比）**
在 Unity DOTS（ECS 和 Burst）中，`Allocator` 是用于 **管理 `NativeArray<T>` 等原生容器的内存分配策略**。它与 C/C++ 中的 `malloc/free`、`new/delete` 类似，但提供了更精确的 **生命周期管理** 和 **多线程安全支持**。

---

## **1. `Allocator` 的基本原理**
在 C++/C 中：
- `malloc/free` 是手动分配和释放堆内存，不调用构造函数和析构函数（低级）。
- `new/delete` 进行堆内存分配，同时调用构造函数和析构函数（高级）。
- **问题**：容易出现 **内存泄漏**（忘记 `free/delete`）、**碎片化**（频繁分配释放导致堆内存混乱）等问题。

在 Unity **ECS/DOTS** 里：
- `Allocator` 提供了 **更清晰的生命周期管理**，减少手动释放的负担。
- **不使用 GC（垃圾回收）**，提高性能，适合高频计算（如 AI、物理、路径寻路等）。
- Unity 内存管理采用 **Job System** 和 **Burst Compiler**，支持多线程访问 **（C++ `std::vector` 之类的东西无法安全地跨线程）**。

---

## **2. `Allocator` 的不同选项**
| Allocator 选项 | **C/C++ 对应的概念** | **特点** | **适用场景** |
|---------------|------------------|---------|-------------|
| `Allocator.Temp` | **`malloc/free`（短时）** | **超快但仅限当前帧，不能跨帧** | **只在当前 `OnUpdate()` 里用，计算完立刻释放** |
| `Allocator.TempJob` | **线程局部 `malloc/free`** | **支持 Job System，最多 4 帧后自动释放** | **Burst Job 或多线程任务** |
| `Allocator.Persistent` | **`new/delete`（长期分配）** | **手动管理生命周期，不自动释放** | **需要长期保存数据，如 ECS 组件数据** |

---

## **3. 详细分析 `Allocator.Temp`**
```csharp
NativeArray<float3> positions = new NativeArray<float3>(100, Allocator.Temp);
```
**特点：**
- **非常快**，但**只能在当前帧使用**（不能存储到 `ISystem` 里）。
- **自动释放**，**不需要手动 `Dispose()`**，但如果 `Dispose()` 了也不会报错。
- **不支持 Job System**（不能在 `Burst Job` 里使用）。
  
**C++ 对比：**
```cpp
float* data = (float*)malloc(100 * sizeof(float)); // 临时分配
// 使用 data...
free(data); // 手动释放
```
- `Allocator.Temp` 本质上类似 **短生命周期的 `malloc/free`**，但在 Unity 里 **自动管理**，不需要 `free`。

**⚠️ 限制：**
- **不能跨帧**（如果你尝试在 `OnCreate()` 里分配 `Temp`，然后 `OnUpdate()` 里用它，会出错）。
- **适用于临时计算，比如路径寻路、查询等**。

**✅ 适用场景**
```csharp
[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    NativeArray<Entity> entities = entityQuery.ToEntityArray(Allocator.Temp); // ✅ 只在当前帧使用
    entities.Dispose(); // ✅ 释放（虽然 Temp 会自动释放，但最好手动 Dispose）
}
```
---

## **4. 详细分析 `Allocator.TempJob`**
```csharp
NativeArray<float3> positions = new NativeArray<float3>(100, Allocator.TempJob);
```
**特点：**
- **支持 Job System**（可以在 `Burst Job` 里用）。
- **自动释放（4 帧后）**，但 **最好手动 `Dispose()`**。
- **比 `Temp` 稍慢，但仍然是短期存储**。

**C++ 对比：**
```cpp
thread_local float* data = (float*)malloc(100 * sizeof(float)); // 线程局部存储
// 计算任务
free(data); // 释放
```
- `TempJob` 允许 **跨帧使用（最多 4 帧）**，适用于 **短期 Job 计算**。

**⚠️ 限制：**
- **不能用于长期存储数据**，否则 **Unity 会报错**（"TempJob allocation is too old"）。
- **适用于 Job System 的数据传递**。

**✅ 适用场景**
```csharp
[BurstCompile]
public void OnUpdate(ref SystemState state)
{
    NativeArray<float3> positions = new NativeArray<float3>(100, Allocator.TempJob);
    var job = new SomeJob { Positions = positions };
    job.Schedule().Complete();
    positions.Dispose(); // ✅ 必须手动释放
}
```
---

## **5. 详细分析 `Allocator.Persistent`**
```csharp
NativeArray<float3> positions = new NativeArray<float3>(100, Allocator.Persistent);
```
**特点：**
- **手动管理内存**，不会自动释放（需要手动 `Dispose()`）。
- **适用于长期存储**，比如 ECS 组件数据、长期缓存的数据。

**C++ 对比：**
```cpp
float* data = new float[100]; // 长期存储
delete[] data; // 必须手动释放
```
- **Persistent 适用于游戏生命周期内的长期数据**。

**⚠️ 限制：**
- **如果忘记 `Dispose()`，就会导致内存泄漏**！
- **适用于 ECS 组件数据、长期缓存的数据**。

**✅ 适用场景**
```csharp
public void OnCreate(ref SystemState state)
{
    NativeArray<float3> positions = new NativeArray<float3>(100, Allocator.Persistent);
}

public void OnDestroy(ref SystemState state)
{
    if (positions.IsCreated) positions.Dispose(); // ✅ 释放内存
}
```
---

## **6. 总结：`Allocator` 选项对比**
| Allocator | **C++ 对应** | **特点** | **适用场景** |
|-----------|-------------|---------|-------------|
| `Allocator.Temp` | `malloc/free`（短期） | **超快，但只能在当前帧用** | **临时计算（如 `ToEntityArray()`）** |
| `Allocator.TempJob` | 线程局部 `malloc/free` | **支持 Job System，最多 4 帧** | **Burst Job 计算（如物理模拟）** |
| `Allocator.Persistent` | `new/delete`（长期） | **手动释放，长期存储** | **ECS 组件数据、长期缓存** |

---

## **7. `Allocator` 常见错误**
### **🚨 1. 使用 `Temp` 试图跨帧**
```csharp
private NativeArray<float3> positions;

public void OnCreate(ref SystemState state)
{
    positions = new NativeArray<float3>(100, Allocator.Temp); // 🚨 错误
}
public void OnUpdate(ref SystemState state)
{
    positions[0] = new float3(1, 1, 1); // 🚨 运行时报错："Temp allocation cannot persist beyond one frame"
}
```
✅ **修正：改用 `Persistent`**
```csharp
positions = new NativeArray<float3>(100, Allocator.Persistent);
```
---

### **🚨 2. `TempJob` 忘记释放**
```csharp
public void OnUpdate(ref SystemState state)
{
    NativeArray<float3> positions = new NativeArray<float3>(100, Allocator.TempJob);
    var job = new SomeJob { Positions = positions };
    job.Schedule().Complete();
    // 🚨 忘记 Dispose()，会导致内存泄漏
}
```
✅ **修正：手动释放**
```csharp
positions.Dispose();
```
---

## **8. 结论**
- **`Temp`** → **超快但仅限当前帧**（像 `malloc/free`）
- **`TempJob`** → **支持 Job System，最多 4 帧**（适合短期 Job 计算）
- **`Persistent`** → **长期存储，手动释放**（类似 `new/delete`）

如果你的数据需要 **长期存储**，用 `Persistent`。如果只在当前帧内计算，**用 `Temp` 或 `TempJob`**。 🚀