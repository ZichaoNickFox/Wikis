






# 概述 #
有几种移动方式EMovementMode
Move_None:禁止移动
Move_Walking:在表面上移动，受摩擦力影响
Move_NavWalking:
Move_Falling:下落，受重力影响，如跳起或走到表面边缘后的状态
Move_Swimming:游泳，穿过fluid volume，受重力和浮力影响
Move_Flying:飞行，忽视重力
Move_Custom:

设置CharacterMoment方式：
```c++
SetMovementMode(MOVE_Walking)
```
