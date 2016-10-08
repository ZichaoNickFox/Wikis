
# 蓝图
[Character的常用设置](https://docs.unrealengine.com/latest/INT/Gameplay/HowTo/CharacterMovement/Blueprints/Setup_1/index.html)
[得到速度](https://answers.unrealengine.com/questions/298098/accessed-none-callfunc-getplayercharacter-returnva-1.html)

# Spawn #
[Spawn](Spawn.md)

# 设置Controller #
一般在Spawn之后设置PawnController
之前必须先设置了Pawn里边的AIControllerClass
执行SpawnDefaultController时，会自己生成一个AIControllerClass的Controller，并调用Controller的Possess方法
```c++
Char->SpawnDefaultController();
```

# Movement #
```c++
void AMyCharacter::MoveForward(float AxisValue) {
FVector Direction = FRotationMatrix(Controller->GetControlRotation()).GetScaledAxis(EAxis::X);
AddMovementInput(Direction, AxisValue);
}

void AMyCharacter::MoveRight(float AxisValue) {
FVector Direction = FRotationMatrix(Controller->GetControlRotation()).GetScaledAxis(EAxis::Y);
AddMovementInput(Direction, AxisValue);
}
```

# Rotation #
```c++
// approach1: bind to pawn build-in functions
void AMyPawn::SetupPlayerInputComponent(class UInputComponent* InputComponent) {
InputComponent->BindAxis("Turn", this, &AddControllerYawInput);
InputComponent->BindAxis("LookUp", this, &AddControllerPitchInput);
}
```

# Jump #
```c++
// approatch1 : bind to character build-in value
void AMyCharacter::SetupPlayerInputComponent(class UInputComponent* InputComponent) {
InputComponent->BindAction("Jump", IE_Pressed, this, &ACharacter::StartJump);
InputComponent->BindAction("Jump", IE_Released, this, &ACharacter::StopJump);
}

void AMyCharacter::StartJump() {
bPressedJump = true;
}

void AMyCharacter::StopJump() {
bPressedJump = false;
}
```
