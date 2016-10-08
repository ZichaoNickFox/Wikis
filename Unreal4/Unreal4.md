
# Usage #
1. [Class Interface Struct Enum EventDispatcher](Usage/ClassInterfaceStructEnum.md)
1. [Component](Usage/Component.md)
1. [math](Usage/math.md)
1. [InputBinding](Usage/InputBinding.md)

# Camera
1. [Camera Viewport](Usage/Camera.md)
[设置Level的默认Camera](https://docs.unrealengine.com/latest/INT/Gameplay/HowTo/UsingCameras/Blueprints/)

# Character
1. [Pawn](Usage/Pawn.md)
1. [Movement](Usage/PawnMovementComponent.md)
1. [得到移动方向 计算速度与当前朝向夹角：](https://docs.unrealengine.com/latest/INT/Engine/Animation/AnimHowTo/PropertyBasedBlending/AnimBP/index.html)
见最后一张图。
得到移动方向：GetActorRotation
计算速度与当前朝向夹角：CalculateDirection，输入是Character当前速度和Rotator。会返回-180~180度。左后是-135，左是-90，左前是-45，前是0，右前是45。
1. animation常用英文：
crouch蹲着，jog慢跑，prone趴着，ironsight瞄准

1. [Usage/Actor](Usage/Actor.md)
1. [ActorComponent](Usage/ActorComponent.md)
1. [Movement Rotation Scale RotatingComponent](Usage/MovementRotationandScale.md)
1. [FVector FPlane](Usage/FVector.md)
1. [GameMode GameState GameInstance GetWorldInstances](Usage/GameMode.md)
1. [FString Log Debug Color FText](Usage/FStringLogDebugFColorFText.md)
1. [Spawn NewObject](Usage/Spawn.md)
1. [Destroy](Usage/Destroy.md)

# Collision
1. [原理概述](https://www.unrealengine.com/blog/collision-filtering)
1. [Collision Trace FBox](Usage/Collision.md)

1. [HUD UI Slate UMG](Usage/HUD.md)
1. [Slate](Usage/Slate.md)
1. [UMG](Usage/UMG.md)
1. [Time](Usage/Time.md)
1. [Delegate](Usage/Delegate.md)
1. [Build UnrealPak Module Plugins Platform File](Usage/GameModule.md)
1. [PlayerController](Usage/PlayerController.md)
1. [DataStructure](Usage/DataStructure.md)
1. [Trigger](Usage/Trigger.md)
1. [ParticleSystem](Usage/ParticleSystem.md)
1. [Damage](Usage/Damage.md)
1. [Assert](Usage/Assert.md)
1. [SmartPointer](Usage/SmartPointer.md)
1. [PlayerCharacter](Usage/PlayerCharacter.md)
1. [UCharacterMovementComponent](Usage/UCharacterMovementComponent.md)
1. [Level]()


#Animation
1. [FSP状态机案例，5种状态，idle, run, jumpStart, jumpLoop, jumpEnd](https://docs.unrealengine.com/latest/INT/Programming/Tutorials/FirstPersonShooter/4/index.html)
1. [Blend2D 二维动画混合官方案例](https://docs.unrealengine.com/latest/INT/Engine/Animation/AnimHowTo/PropertyBasedBlending/Setup/index.html)
1. 设置Character的Animation Blueprint:
Once you have created the Animation Blueprint that defines the motion of your character, you will need to make sure you assign it to the Anim Blueprint Generated Class property, found under the Mesh Component of the Character Blueprint. 

1. [UCLASS USTRUCT UINTERFACE UFUNCTION UPROPERTY Metadata](Usage/InteractwithC++.md)
1. [Communication](Usage/Communication.md)
1. [StaticMesh](Usage/StaticMesh.md)

# fog
1. [Fog文档](https://docs.unrealengine.com/latest/INT/Engine/Actors/FogEffects/index.html)
1. [设置默认背景](https://answers.unrealengine.com/questions/116963/how-to-change-the-default-scene-background-color.html)

# AI #
1. [AI](AI/AI.md)
1. [Navigation](AI/Navigation.md)
1. [Sensing](AI/Sensing.md)
1. [AIController](AI/AIController.md)

# FPS game #
1. [Character Component hierachy](FPSGame/CharacterComponentHierachy.md)
1. [Projectile hierachy](FPSGame/ProjectileHierachy.md)
1. [Fire](FPSGame/Fire.md)
1. [CrossHair](FPSGame/Crosshair.md)

# Resource
1. [支持的图片格式](https://docs.unrealengine.com/latest/INT/Engine/Content/Types/Textures/Importing/index.html)
1. [载入StarterContent](https://forums.unrealengine.com/showthread.php?64254-How-do-I-add-starter-content-to-a-project-manually)
1. [使用EngineResourece](https://answers.unrealengine.com/questions/197982/game-and-engine-folder-missing-from-content-browse.html)

# 设计模式 #
1. [State Pattern](DesignPattern/StatePattern.md)

# Engine
1. [下载源码文档](https://docs.unrealengine.com/latest/INT/GettingStarted/DownloadingUnrealEngine/)

# Models
1. [Model网站](https://www.quora.com/Where-can-I-find-free-assets-for-Unreal-Engine-4)
1. [现成资源](https://www.reddit.com/r/gamedev/comments/36km9u/200_completely_free_mobile_scifi_rpg_assets_ue4/)
1. [自己做](https://www.mixamo.com/3d-characters)

# vs
1. [配置ue4 for vs](https://docs.unrealengine.com/latest/INT/Programming/Development/VisualStudioSetup/)
1. [使用vs2013](https://answers.unrealengine.com/questions/31887/visual-studio-2012-on-unreal-engine-402.html)
1. [generateprojectfiles.bat unrealVS](https://docs.unrealengine.com/latest/INT/Programming/UnrealBuildSystem/ProjectFileGenerator/)
1. [删除vs2015](http://tieba.baidu.com/p/3996550898)
1. [source文件夹下的ProjectName.target.cs](https://docs.unrealengine.com/latest/INT/Programming/UnrealBuildSystem/TargetFiles/index.html)
1. vs插件：va, vsvim, easymotion
1. [编译游戏项目](https://docs.unrealengine.com/latest/INT/Programming/Development/CompilingProjects/)
1. 生成项目文件UnrealBuildTool.exe -2013 -projectfiles -project="E:/Unreal4Projects/OfficialGuide/OfficialGuide.uproject" -game -engine -progress