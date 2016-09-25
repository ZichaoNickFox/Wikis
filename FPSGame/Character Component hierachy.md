











```c++
class AFPSCharacter : public Character {
UPROPERTY(VisibleAnywhere)
UCameraComponent* FPSCameraComponent;

// usually, body and arm are separated
// body set as ownerNoSee
// arm set as onlyOnwerSee
UPROPERTY(EditDefaultsOnly)
USkeletalMeshComponent* FPSArmMesh;
}

AFPSCharacter::AFPSCharacter(){
FPSCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
FPSCameraComponent->AttachToComponent(GetCapsuleComponent(), FAttachmentTransformRules::KeepRelativeTransform);
FPSCameraComponent->SetRelativeLocation(FVector(0,0,50 + BaseEyeHeight));
FPSCameraComponent->bUsePawnControlRotation = true;

FPSArmMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("FirstPersonMesh"));
FPSArmMesh->SetOnlyOwnerSee(true);
FPSArmMesh->AttachToComponent(FPSCameraComponent, FAttachmentTransformRules::KeepRelativeTransform);
FPSArmMesh->bCastDynamicShadow = false;
FPSArmMesh->CastShadow = false;

GetMesh()->SetOwnerNoSee(true);
}
```
