














# Log #
## 打印在屏幕 ##
先打印出来的在下边
```c++
// no formated on screen log
GEngine->AddOnScreenDebugMessage(-1, 5, FColor::Yellow, TEXT("hello world"));

// formated on screen log
GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, FString::Printf(TEXT("Some variable values: x: %f, y: %f"), x, y));
```


## 打印在log中 ##
https://wiki.unrealengine.com/Logs,_Printing_Messages_To_Yourself_During_Runtime#Log_formatting
```c++
// log FString
FString content = "hello world";
UE_LOG(LogTemp, Warning, TEXT("%s"), *content);

// log int
UE_LOG(LogTemp, Warning, TEXT("%d"), 200);
```

## 设置log category ##
可以设置在YouGame.h，YouGame.cpp中，以便所有地方打log时都能用
也可以设置在定制的.h .cpp中，以便包含了这个头文件的文件打log时能用
.h
```c++
DECLARE_LOG_CATEGORY_EXTERN(LogInit, Display, All);
DECLARE_LOG_CATEGORY_EXTERN(LogAI, Display, All);
DECLARE_LOG_CATEGORY_EXTERN(LogFatalError, Display, All);
```
.cpp
```c++
DECLARE_LOG_CATEGORY(LogInit);
DECLARE_LOG_CATEGORY(LogAI);
DECLARE_LOG_CATEGORY(LogFatalError);
```

# FString #
* 初始化
```c++
// int值初始化
FString::FromInt(2);
// 字符串初始化
FString s = "hello world";
```


* FString conversion
https://wiki.unrealengine.com/String_Conversions:_FString_to_FName,_FString_to_Int32,_Float_to_FString


# FText #
[介绍 LOCTEXT NSLOCTEXT 转化Conversion 比较Comparison inHUD](https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/StringHandling/FText/index.html)
* 初始化，与FString相同
```c++
FText::FromtString(TEXT("xxx"));
```


# FColor #
```c++
FColor::Yellow
FColor(255,0,0);
```

# Debug #
* DrawDebug Function
```c++
// 画线
DrawDebugLine(
GetWorld(),
StartFVector,
EndFVector,
FColor::Yellow,
bPersistant = false,
fLifeTime = -1,
uint8DepthProperty = 0,
Thickness = 0
)

// 画点
// 第三个参数是尺寸，大了的话，是方形了
DrawDebugPoint(
GetWorld(),
InPlayerController->GetFocalLocation(),
20,
FColor::Red,
true
);

// 画有向箭头
// 第四个参数是射线箭头的尺寸
DrawDebugDirectionalArrow(
GetWorld(),
WorldBoundPoints[0],
FrustumRays[0] * 30000 + WorldBoundPoints[0],
5,
FColor::Green,
true
);
```
