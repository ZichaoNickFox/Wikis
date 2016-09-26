










# StrategyGame #

## 状态类 ##
```c++
UCLASS(Abstract, BlueprintType)
class UStrategyAIAction : public UObject {
// 返回true，说明这个状态希望维持，false说明这个状态希望结束
virtual bool Tick(float DeltaTime);
// 状态开始的时候调用
virtual void Activate();
// 是否应该开始这个状态
virtual void ShouldActivate();
// 被动退出这个状态。
virtual void Abort();
// 是否可以安全退出这个状态
virtual bool IsSafeToAbort();
}
```

## 状态机（AIController） ##
```c++
class AStrategyController : public AAIController {
private:
// 当前状态
UStrategyAIAction* CurrentAction;
}
// 在Tick中进行状态维持和转换
void AStrategyController::Tick() {
// 1、查看是否需要结束状态机
if (GetPawn()->IsDead()) {
// 结束状态机
}
// 2、查看是否需要结束当前状态
if (CurrentAction && !CurrentAction->Tick() && CurrentAction->IsSafeToAbort()) {
CurrentAction->Abort();
CurrentAction = nullptr;
}
// 3、选择适当的新状态。注意，状态是互斥的，同时只能有一个ShouldActivate()是true的状态
for (AllowedState in AllAllowedStates) {
if (AllowedState->ShouldActivate()) {
if (CurrentAction && CurrentAction->IsSafeToAbort()) {
CurrentAction->Abort();
CurrentAction = nullptr;
}
CurrentAction = AllowedState;
CurrentAction->Activate();
break;
}
}
}
```
