











# 概述 #

## 代理的意思 ##
代理就是一个EventDispatcher
或者说是一个Obserable
回调是一种特殊的EventDispatcher，相当于执行回调的程序触发Dispatcher，而Dispatcher只有一个Observer。

## Level Blueprint与Level中的Blueprint和非Blueprint ##
一个Level中的Blueprint如果添加事件，则会在Level Blueprint的Event Graph中添加事件处理
一个Level中的非Blueprint如果添加事件，则会在Sub-Level Blueprint的Event Graph中添加事件处理

# 代理 #
## 动态广播代理 ##
https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/Delegates/Multicast/
c++
```c++
// 声明代理
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FWaveSpawnedDelegate)

class AMyStrategyBuilding_Brewery : public AMyStrategyBuilding {
public:
// 定义代理变量
// 这里要写为BlueprintAssignable
UPROPERTY(BlueprintAssignable)
FWaveSpawnedDelegate OnWaveSpawnedDelegate;
}

// 广播代理，不一定是定义代理变量的类发起广播
// 但处理代理必须是定义代理对象的子类
void SomeFunction() {
Brewery->FWaveSpawnedDelegate.Broadcast();
}
```
蓝图，必须是AMyStrategyBuilding_Brewery的派生类或者Level Blueprint
{{file:DynamicMulticastDelegate.png}}

## 回调函数 ##
```c++
DECLARE_DELEGATE(FCallbackDelegate)

class UMyObject : public UObject {
public:
FCallbackDelegate CallbackDelegate;
}

void UMyObject::BindLikeThis() {
CallbackDelegate Callback;
Callback.BindUObject(this, &UMyObject::CallbackHandleHere);
CallbackDelegate = Callback;
}

void UMyObject::UnbindLikeThis() {
CallbackDelegate.Unbind()
}

void UMyObject::CallbackHandleHere() {

}

void UMyObject::CallbackTrigger() {
CallbackDelegate.ExecuteIfBound();
}
```

