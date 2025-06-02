


```csharp
// v is the physics mass component of the object
  if (testC.ValueRO.Moved)
            {
                v.ValueRW.InverseMass = 1;
                return;
            }

            v.ValueRW.InverseMass = 0;
            testC.ValueRW.Moved = true;
            transform.ValueRW.Position += new float3(0, -10, 0);
``` 
This code teleports the object through the floor by setting its inverse mass to 0 and moving it downwards by 10 units. 
You need to set the inverse mass back to 1 after the object has been moved, so that collisions can be detected again.