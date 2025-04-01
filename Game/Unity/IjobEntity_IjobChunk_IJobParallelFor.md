       
       
       
        public struct Job2<TInteractAbility> : IJobChunk where TInteractAbility : unmanaged, IComponentData, IInteractAbility
        {
            public ComponentTypeHandle<TInteractAbility> InteractAbility;
            
            public void Execute(in ArchetypeChunk chunk, int unfilteredChunkIndex, bool useEnabledMask, in v128 chunkEnabledMask)
            {
                var abilities = chunk.GetNativeArray(ref InteractAbility);
                for (int i = 0; i < chunk.Count; i++)
                {
                   var ability = abilities[i];
                   ability.Count++;
                   ability.Speed++;
                   abilities[i] = ability;
                }
            }
        }


