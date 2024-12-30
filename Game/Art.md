# Art Notes

## Specific Noun
- Zbrush : A way to add details to 3D models: `Scupturing tiling textures using Zbrush`
- Ubisoft has foliage or biome artists

## Environment

###
Art Station Challenge: Game Environment
Basic Idea : Spend less time in sculpting the grid in 3D software, and more time in art.

- Gray Box / Block Out Process:
  1. Focus on layout and compostition when you are doing your gray box.
  2. Prioritize assets based on blockout use an screen space "Real Estate"
  3. Keep it super simple and efficient! Avoid distractions like light bakes at this stage.
    - E.g. Use rocks to block sun to get that feel of sun coming through trees
- Alpha Stage-Replace main gray box with sculpted meshes(house, walls, stairs, etc).
  Core Idea: Use prefab or blueprints to save time.
  1. Build things in a modular way , and trans into Unity or Unreal Engine.
  2. Build model as large as possible, and use the largest one as standard for smaller ones.
  3. Smash trees and rocks to the ground, it doesn't have to be stitched to look like completely airtight to the geometry.
  4. These days polygons are quite cheap in comparison to using fancy or complex shaders. 
  5. UE has auto LED system you can use to generate multiple levels of detail for your meshes, for e.g., when you get far away from a mesh, its polygons will be reduced to a low poly version.
  6. Reuse everything you can to get the feeling you want to help build that momentum and motivation to carry yourself to the end.
- Beta Stage-Add organic elements to your environment(trees, grass, rocks, etc).

- Level Designer vs Level Artist:





---

### **环境设计 vs. 3D模型设计的关系**
1. **重合点：**
   - **环境设计**关注游戏中的场景布局、关卡结构、玩家路径、交互逻辑等，是一种更宏观的设计。
   - **3D模型设计**更关注具体物体的形状、材质、贴图等细节，是微观层面的制作。
   - **交叉点**：
     - 灰盒（Graybox）阶段会使用简单的几何体来规划关卡，这些几何体可以在3D建模软件或游戏引擎中制作。
     - 完成后的3D模型会导入到游戏引擎中，用于替换早期的占位几何体，最终形成完整的场景。

---

### **灰盒阶段 (Graybox Stage)**
- **目标：**快速搭建关卡的基础框架。
- **推荐工具：**
  - **Unity/Unreal Engine：**
    - 使用内置的Primitive（如Cube、Plane）搭建简单场景，方便调试玩家路径和交互逻辑。
  - **Blender/Maya：**
    - 如果对场景需要更复杂的几何细节（如桥梁、楼梯等特定结构），可以先在这些软件中建模，再导入到引擎中。
- **输出结果：**此阶段的场景非常简陋，只关注功能性。

---

### **Alpha阶段 (Alpha Stage)**
- **目标：**引入部分完成的3D模型，进一步完善场景。
- **推荐工具：**
  - **Blender/Maya：**
    - 制作高质量3D模型，比如建筑、道具。
  - **Unity/Unreal：**
    - 将完成的模型导入引擎中，结合材质和灯光进行初步的美术呈现。
  - **Quixel Megascans：**
    - 如果需要快速填充细节，可以用现成的高质量资源。
- **输出结果：**此阶段的场景开始接近游戏最终的美术方向，但仍可能缺少最终的优化。

---

### **Beta阶段 (Beta Stage)**
- **目标：**优化和完成所有细节，加入最终的光影、特效、交互功能。
- **推荐工具：**
  - **Blender：**
    - 制作最终模型、UV展开、贴图烘焙。
  - **Substance Painter/Designer：**
    - 创建和调整贴图，提升材质细节。
  - **Unity/Unreal：**
    - 完成所有模型整合，添加实时光影、后处理特效，以及优化性能（如LOD）。
- **输出结果：**接近最终游戏质量，包含所有美术和功能细节。

---

### **总结**
1. **Graybox阶段：**大部分工作在**Unity/Unreal**完成，必要时用**Blender**补充特定几何体。
2. **Alpha阶段：**大部分工作在**Blender**完成模型制作，**Unity/Unreal**整合测试。
3. **Beta阶段：**各软件协同工作，重点是**Blender**完成模型和贴图，**Unity/Unreal**完成场景整合与优化。

---

根据你的学习进度，如果精力有限，可以先专注于：
- 在Unity/Unreal中学习关卡布局和简单场景搭建。
- 在Blender中学习建模和贴图制作，为环境设计提供素材支持。 

这样能快速建立基础，同时兼顾效率和美术水平！如果有更多具体问题，可以继续探讨 😊