








# Camera #
[设置Level的默认Camera](https://docs.unrealengine.com/latest/INT/Gameplay/HowTo/UsingCameras/Blueprints/)
* set camera to non-character actors
```c++
// get player controller:
1. nclude "Kismet/GameplayStatics.h"
APlayerController* ourPlayerController = UGameplayStatics::GetPlayerController(this, 0);

// get playerController's view target
AActor* viewTarget = ourPlayerController->GetViewTarget();

// set view target to playerController
AActor* camera;
ourPlayerController->SetViewTarget(camera);

// set view target to playerController with blend
const float smoothBlendTime = 2.0f;
ourPlayerController->SetViewTargetWithBlend(camera, smmothBlendTime);
```


* set camera to non-character actors
```c++
// spring arm
USpringArmComponent* springArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("CameraAttachmentArm"));
springArm->SetupAttachment(RootComponent);
springArm->RelativeRotation = FRotator(-45, 0, 0);
springArm->TargetArmLength = 400;
springArm->bEnableCameraLag = true;
springArm->CameraLagSpeed = 3;

// camera
UCameraComponent* camera = CreateDefaultSubobject<UCameraComponent>(TEXT("ActualCamera"));
camera->SetupAttachment(springArm, USpringArmComponent::SocketName)
```

* set camera to [Character](Character.md)
```c++
class AMyCharacter : public Character {
UPROPERTY(VisbleAnywhere)
UCameraComponent* CameraComponent;
}

AMyCharacter::AMyCharacter() {
CameraComponent = CreateDefaultSubObject<UCameraComponent>(TEXT("CameraComponent"));
CameraComponent->AttachToComponent(GetCapsuleComponent());
CameraComponent->SetRelativeLocation(FVector(0.0f, 0.0f, 50 + BaseEyeHeight));
CameraComponent->bUsePawnControlRotation = true;
}
```

* zoomIn zoomOut
这里的实现思路是修改相机的FOV，默认为90，当FOV缩小时，因为屏幕大小不变，所以镜头拉近了。
```c++
class AMyCameraPawn : public APawn {
float ZoomFactor;
}
void AMyCameraPawn::Tick(float DeltaTime) {
if (bZoomingIn)
{
ZoomFactor += DeltaTime / 0.5f;
} else {
ZoomFactor -= DeltaTime / 0.25f;
}

ZoomFactor = FMath::Clamp<float>(ZoomFactor, 0.0f, 1.0f);
CameraComponent->FieldOfView = FMath::Lerp<float>(90.0f, 60.0f, ZoomFactor);
}
```


# Viewport #
* 得到视口尺寸CurrentViewportSize
```c++
// 方法1
ULocalPlayer* const LocalPlayer = Cast<ULocalPlayer>(PlayerController->Player);
if (LocalPlayer == NULL || LocalPlayer->ViewportClient == NULL) {
return;
}
FVector2D CurrentViewportSize;
LocalPlayer->ViewportClient->GetViewportSize(CurrentViewportSize);

// 方法2
FVector2D ViewportSize;
GEngine->GameViewport->GetViewSize(ViewportSize);
```

