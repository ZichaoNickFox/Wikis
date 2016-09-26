




















# 介绍 #
## GameMode ##
GameMode定义PlayerController, DefaultCharacter, GameState等等
GameMode类似于GameManager
StrategyGame中与Team有关的都写在GameMode中
存贮所有玩家信息的写在GameState中


### 设置全局对象类型 ###
```c++
AMyGameMode::AMyGameMode(const FObjectInitializer& ObjectInitializer) {
PlayerControllerClass = AStrategyPlayerController::StaticClass();
SpectatorClass = AStrategySpectatorPawn::StaticClass();
DefaultPawnClass = AStrategySpectatorPawn::StaticClass();
GameStateClass = AStrategyGameState::StaticClass();
HUDClass = AStrategyHUD::StaticClass();
}
```

## GameState ##
GameState类似于Model,存贮世界变量信息

## Character ##
* from HUD
```c++
AMyCharacter aMyChar = Cast<AMyCharacter>PlayerOwner->GetCharacter();
```


## PlayerController ##

# 得到对象（能用GetWorld()的情况) #
## GameMode ##
```c++
// 必须是Server才能这么得到
AMyGameMode* GameMode = GetWorld()->GetAuthGameMode();

// 也是调用上边一个函数
AMyGameMode* GameMode = UGameplayStatic::GetGameMode();
```

## GameState ##
from Component
```c++
AMyGameState const* const GameState = GetWorld()->GetGameState<AStrategyGameState>();
```

## PlayerController ##
from component
```c++
AMyPlayerController* PlayerController = NULL;
APawn* Owner = Cast<APawn>(GetOwner());
PlayerController = Cast<APlayerController>(Owner->GetController());
return PlayerController;
```

# 得到对象（不能用GetWorld()的情况）#
UObject中GetWorld()永远返回nullptr，只能传一个对象过去，如在State模式的每个State里边
