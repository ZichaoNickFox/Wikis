







```c++
class AFPSProjectile : public AActor {
UPROPERTY(VisibleDefaultsOnly, Category = Projectile)
USphereComponent* CollisionComponent;

UPROPERTY(VisibleAnywhere, Category = Movement)
UProjectileMovementComponent* ProjectileMovementComponent;

}

AFPSProjectile::AFPSProjectile() {
CollisionComponent = CreateDefaultSubobject<USphereComponent>(TEXT("SphereComponent"));
CollisionComponent->SetSphereRadius(15.0f);
RootComponent = CollisionComponent;

ProjectileMovementComponent = CreateDefaultSubobject<UProjectileMovementComponent>(TEXT("MovementComponent"));
ProjectileMovementComponent->SetUpdatedComponent(CollisionComponent);
ProjectileMovementComponent->InitialSpeed = 3000.0f;
ProjectileMovementComponent->MaxSpeed = 3000.0f;
ProjectileMovementComponent->bRotationFollowsVelocity = true;
ProjectileMovementComponent->bShouldBounce = true;
ProjectileMovementComponent->Bounciness = 0.3f;
}

```

