







# Blueprint
[到点执行（闹钟）](https://docs.unrealengine.com/latest/INT/Gameplay/HowTo/UseTimers/Blueprints/)

# C++

* 从Play开始的，计算暂停，时间加快，时间减慢的时间
```c++
GetWorld()->GetTimeSeconds();
```

* 从Play开始的，不计算暂停，时间加快，时间减慢的时间
```c++
GetWorld()->GetRealTimeSeconds();
```

* register and unregister timer
倒计时案例
```c++
class AMyActor : public AActor {
FTimeHandler CountdownTimeHandler;
int32 CountdownTime;
void TickCallback();
void RegisterTimerHandler();
void UnregisterTimerHandler();
}

void AMyActor::BeginPlay() {
CountdownTime = 3;
RegisterTimerHandler();
}

void AMyActor::TickCallback() {
CountdownTime = CountdownTime - 1;
if (CountdownTime < 1) {
UnregisterTimerhandler();
}
}

void AMyActor::RegisterTimerHandler(){
GetWorldTimerManager().SetTimer(CountdownTimerHandler, this, &AMyActor::TickCallback, 1,0f, true);
}

void AMyActor::UnregisterTimerHandler(){
GetWorldTimerManager().ClearTimer(CountdownTimerHandler);
}
```

* 动画播放速度
```c++
SKeletalMeshComponent.GlobalAnimRateScale = .5f;
```
