







# 注意 #
当点击内容浏览器，右边的内容中有蓝图时。其中的蓝图会运行下边函数。只有BeginPlay才会真正在Play时候执行。
所以在PostInitializeComponents里边check GameState肯定会挂。
所以在下边函数中判定是否有GameState等全局变量是应该的。
* PostLoad/PostActorCreated - Do any setup of the actor required for construction. PostLoad for serialized actors, PostActorCreated for spawned.
* AActor::OnConstruction - The construction of the actor, this is where Blueprint actors have their components created and blueprint variables are initialized
* AActor::PreInitializeComponents - Called before InitializeComponent is called on the actor's components
* UActorComponent::InitializeComponent - Each component in the actor's components array gets an initialize call (if bWantsInitializeComponent is true for that component)
* AActor::PostInitializeComponents - Called after the actor's components have been initialized
