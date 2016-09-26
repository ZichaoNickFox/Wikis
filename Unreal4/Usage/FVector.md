












# FVector #
```c++
// 静态
// (0,0,0)
FVector::ZeroVector
// (1,0,0)
FVector::ForwardVector
// (0,0,1)
FVector::UpVector
// (0,1,0)
FVector::RightVector

// 长度
// sqrt(x*x + y*y + z* z)
float Size();
// sqrt(x*x + y*y)
float Size2D();
// x*x + y*y + z*z
float SizeSquared();
// x*x + y*y
float Size2DSquared();
```


* clamp
```c++
// clamp XYZ below max size
FVector GetClampedToMaxSize(float maxSize) const;
```

* 标准化，点积，叉积
左手坐标系叉积满足左手法则
右手坐标系叉积满足右手法则
```c++
FVector(1,1,0).GetSafeNormal();
FVector::CrossProduct(FVector v1, FVector v2);
FVector::DotProduct(FVector v1, FVector v2);
```

# FPlane #
* 初始化
```c++
// 点法式
FPlane(FVector OriginPoint, FVector Direction)
```

* 根据平面MyPanel得到该平面的原点PlaneOrigin和法线PlaneNormal
http://www.cnblogs.com/graphics/archive/2009/10/17/1585281.html
```c++
const FVector PlaneNormal = FVector(MyPlane.X, MyPlane.Y, MyPlane.Z);
const FVector PlaneOrigin = PlaneNormal * MyPlane.W;
```

* 求射线MyRay与平面MyPlane交点坐标
http://www.cnblogs.com/graphics/archive/2009/10/17/1585281.html
```c++
FVector Distance = FVector::DotProduct(PlaneNormal, (PlaneOrigin - RayOrigin)) / FVector::DotProduct(PlaneNormal, RayDirect);
return RayOrigin + RayDirection * Distance;
```
