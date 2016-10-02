



















# 介绍 #
HUD管理所有界面上Canvas的东西。画他们，并且是游戏内逻辑与Canvas的中间层。

# FPSGameHUD #
1、不要忘了在蓝图中设置相应的资源
2、不要忘了在project setting中设置相应的hud

# StrategyGameHUD #
充当的中间层角色：
void HideAllActionButtons()
bool IsPauseMenuUp()
充当的管理和画Canvas角色：
void BuildMenuWidget();
void DrawMousePointer()
void DrawMiniMap();
void DrawLives();
void DrawHealthBar();
void DrawActorHealth();

# UI
[将UI显示在屏幕上](https://docs.unrealengine.com/latest/INT/Engine/UMG/UserGuide/CreatingWidgets/)
[显示鼠标指针]