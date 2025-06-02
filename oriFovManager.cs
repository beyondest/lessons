Found 1 leak(s) from callstack:
0x000001810713a993 (Mono JIT Code) Unity.Collections.Memory/Unmanaged/Array:Resize (void*,long,long,Unity.Collections.AllocatorManager/AllocatorHandle,long,int) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/Memory.cs:79)
0x000001810713a583 (Mono JIT Code) Unity.Collections.Memory/Unmanaged:Allocate (long,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/Memory.cs:20)
0x00000181caa9037b (Mono JIT Code) Unity.Collections.LowLevel.Unsafe.HashMapHelper`1<Unity.Entities.Entity>:Init (int,int,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/UnsafeHashMap.cs:92)
0x00000181caa8ff73 (Mono JIT Code) Unity.Collections.LowLevel.Unsafe.HashMapHelper`1<Unity.Entities.Entity>:Alloc (int,int,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/UnsafeHashMap.cs:114)
0x00000181caf432a3 (Mono JIT Code) Unity.Collections.NativeHashMap`2<Unity.Entities.Entity, Unity.Collections.NativeList`1<SparFlame.GamePlaySystem.EnemyAI.TargetLocPair>>:.ctor (int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/NativeHashMap.cs:152)
0x00000181caf3aa83 (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:OnCreate (Unity.Entities.SystemState&) (at D:/WS_Unity/WarOfLightAndShadow/Assets/Scripts/GamePlaySystem/Functionality/EnemyAI/TeamStateMachine/EnemyTeamAssignTargetSystem.cs:61)
0x00000181caf39fe3 (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:__codegen__OnCreate$BurstManaged (intptr,intptr)
0x00000181caf39e83 (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem/SparFlame.GamePlaySystem.EnemyAI.__codegen__OnCreate_00000231$BurstDirectCall:Invoke (intptr,intptr)
0x00000181caf39d2b (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:__codegen__OnCreate (intptr,intptr)
0x00000181caf39c43 (Mono JIT Code) (wrapper native-to-managed) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:__codegen__OnCreate (intptr,intptr)
0x0000017ea7a26b3c (Mono JIT Code) (wrapper managed-to-native) object:wrapper_native_00000181093B2E80 (intptr,intptr)
0x0000017ea7ac8491 (Mono JIT Code) Unity.Entities.SystemBaseRegistry:ForwardToManaged (intptr,Unity.Entities.SystemState*,void*) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/SystemBaseRegistry.cs:364)
0x0000017ea7ac7e93 (Mono JIT Code) Unity.Entities.SystemBaseRegistry:CallForwardingFunction (Unity.Entities.SystemState*,Unity.Entities.UnmanagedSystemFunctionType) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/SystemBaseRegistry.cs:333)
0x0000017ea7ac8293 (Mono JIT Code) Unity.Entities.SystemBaseRegistry:CallOnCreate (Unity.Entities.SystemState*) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/SystemBaseRegistry.cs:370)
0x0000017ea7ac694b (Mono JIT Code) Unity.Entities.WorldUnmanagedImpl:CallSystemOnCreateWithCleanup (Unity.Entities.SystemState*) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/WorldUnmanaged.cs:614)
0x0000017ea7b83e23 (Mono JIT Code) Unity.Entities.World:GetOrCreateSystemsAndLogException (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/World.cs:1282)
0x0000017ea7b823ab (Mono JIT Code) Unity.Entities.World:GetOrCreateSystemsAndLogException (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/World.cs:1321)
0x0000017ea7b8093b (Mono JIT Code) Latios.BootstrapTools:InjectSystems (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,Unity.Entities.World,Unity.Entities.ComponentSystemGroup,Unity.Collections.NativeHashMap`2<Unity.Entities.SystemTypeIndex, Unity.Entities.SystemTypeIndex>) (at 



Found 1 leak(s) from callstack:
0x000001810713a993 (Mono JIT Code) Unity.Collections.Memory/Unmanaged/Array:Resize (void*,long,long,Unity.Collections.AllocatorManager/AllocatorHandle,long,int) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/Memory.cs:79)
0x000001810713a583 (Mono JIT Code) Unity.Collections.Memory/Unmanaged:Allocate (long,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/Memory.cs:20)
0x00000181caa8feeb (Mono JIT Code) Unity.Collections.LowLevel.Unsafe.HashMapHelper`1<Unity.Entities.Entity>:Alloc (int,int,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/UnsafeHashMap.cs:113)
0x00000181caf432a3 (Mono JIT Code) Unity.Collections.NativeHashMap`2<Unity.Entities.Entity, Unity.Collections.NativeList`1<SparFlame.GamePlaySystem.EnemyAI.TargetLocPair>>:.ctor (int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.collections/Unity.Collections/NativeHashMap.cs:152)
0x00000181caf3aa83 (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:OnCreate (Unity.Entities.SystemState&) (at D:/WS_Unity/WarOfLightAndShadow/Assets/Scripts/GamePlaySystem/Functionality/EnemyAI/TeamStateMachine/EnemyTeamAssignTargetSystem.cs:61)
0x00000181caf39fe3 (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:__codegen__OnCreate$BurstManaged (intptr,intptr)
0x00000181caf39e83 (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem/SparFlame.GamePlaySystem.EnemyAI.__codegen__OnCreate_00000231$BurstDirectCall:Invoke (intptr,intptr)
0x00000181caf39d2b (Mono JIT Code) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:__codegen__OnCreate (intptr,intptr)
0x00000181caf39c43 (Mono JIT Code) (wrapper native-to-managed) SparFlame.GamePlaySystem.EnemyAI.EnemyTeamAssignTargetSystem:__codegen__OnCreate (intptr,intptr)
0x0000017ea7a26b3c (Mono JIT Code) (wrapper managed-to-native) object:wrapper_native_00000181093B2E80 (intptr,intptr)
0x0000017ea7ac8491 (Mono JIT Code) Unity.Entities.SystemBaseRegistry:ForwardToManaged (intptr,Unity.Entities.SystemState*,void*) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/SystemBaseRegistry.cs:364)
0x0000017ea7ac7e93 (Mono JIT Code) Unity.Entities.SystemBaseRegistry:CallForwardingFunction (Unity.Entities.SystemState*,Unity.Entities.UnmanagedSystemFunctionType) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/SystemBaseRegistry.cs:333)
0x0000017ea7ac8293 (Mono JIT Code) Unity.Entities.SystemBaseRegistry:CallOnCreate (Unity.Entities.SystemState*) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/SystemBaseRegistry.cs:370)
0x0000017ea7ac694b (Mono JIT Code) Unity.Entities.WorldUnmanagedImpl:CallSystemOnCreateWithCleanup (Unity.Entities.SystemState*) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/WorldUnmanaged.cs:614)
0x0000017ea7b83e23 (Mono JIT Code) Unity.Entities.World:GetOrCreateSystemsAndLogException (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,int,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/World.cs:1282)
0x0000017ea7b823ab (Mono JIT Code) Unity.Entities.World:GetOrCreateSystemsAndLogException (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,Unity.Collections.AllocatorManager/AllocatorHandle) (at ./Library/PackageCache/com.unity.entities/Unity.Entities/World.cs:1321)
0x0000017ea7b8093b (Mono JIT Code) Latios.BootstrapTools:InjectSystems (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,Unity.Entities.World,Unity.Entities.ComponentSystemGroup,Unity.Collections.NativeHashMap`2<Unity.Entities.SystemTypeIndex, Unity.Entities.SystemTypeIndex>) (at ./Library/PackageCache/com.latios.latiosframework/Core/Framework/BootstrapTools.cs:262)
0x00000181caecfe1b (Mono JIT Code) Latios.BootstrapTools:InjectUserSystems (Unity.Collections.NativeList`1<Unity.Entities.SystemTypeIndex>,Unity.Entities.World,Unity.Entities.Com

