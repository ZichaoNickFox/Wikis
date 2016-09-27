<!-- MarkdownTOC -->

- sublime3 documents url
- commands
- build system
- key binding and context and scope
- console
- vintageous
- theme
- settings
- TODO

<!-- /MarkdownTOC -->
# sublime3 documents url
[sublime3 official Document](https://www.sublimetext.com/docs/3/index.html)
[sublime3 unofficial document中文版](http://sublime-text.readthedocs.io/en/latest/intro.html)
[sublime3 unofficial Document](http://docs.sublimetext.info/en/latest/extensibility/plugins.html)
[sublime3 API](https://www.sublimetext.com/docs/3/api_reference.html)


# commands
[official document](http://www.sublimetext.com/docs/3/commands.html)
[unofficial document](http://docs.sublimetext.info/en/latest/reference/commands.html)



# build system
[unofficial document 中文版](http://sublime-text.readthedocs.io/en/latest/reference/build_systems.html)
[一个php例子](http://www.cnblogs.com/picaso/p/3337866.html)
file_regex example
"^.+ in (.+) on line ([0-9]+)",
"^ *\\[javac\\] (.+):([0-9]+):() (.*)$"

虚幻build命令:E:/Unreal4/Epic Games/4.12/Engine/Binaries/DotNET/UnrealBuildTool.exe StrategyGame Development Win64 -project="D:/Unreal4Projects/StrategyGame/StrategyGame.uproject" -editorrecompile -progress -noubtmakefiles -NoHotReloadFromIDE

1>------ Build started: Project: OfficialGuide, Configuration: Development_Game Win32 ------
1>  Performing full C++ include scan (building a new target)
1>  Performing 15 actions (4 in parallel)
1>  PCH.OfficialGuide.h.cpp
1>D:\Unreal4Projects\OfficialGuide\Source\OfficialGuide\OfficialGuide.h(8): error C2059: 语法错误:“{”
1>D:\Unreal4Projects\OfficialGuide\Intermediate\Build\Win32\OfficialGuide\Development\OfficialGuide\PCH.OfficialGuide.h.cpp(1): error C2850: “PCH 头文件”: 只能在文件范围内使用；不能在嵌套结构内使用
1>ERROR : UBT error : Failed to produce item: D:\Unreal4Projects\OfficialGuide\Binaries\Win32\OfficialGuide.exe
1>  Total build time: 124.96 seconds
1>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.MakeFile.Targets(37,5): error MSB3075: The command ""E:\Unreal4\Epic Games\4.12\Engine\Build\BatchFiles\Build.bat" OfficialGuide Win32 Development "D:\Unreal4Projects\OfficialGuide\OfficialGuide.uproject" -waitmutex" exited with code 5. Please verify that you have sufficient rights to run this command.
========== Build: 0 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========

[forum discussion](https://answers.unrealengine.com/questions/92910/is-there-any-way-to-change-the-default-editoride-t.html)


# key binding and context and scope
[sublime自带的context](http://docs.sublimetext.info/en/latest/reference/key_bindings.html)
[特定类型文件的绑定](https://forum.sublimetext.com/t/file-type-specific-key-bindings/2839/3)
[特定类型文件的确定](https://forum.sublimetext.com/t/selector-on-a-keybind/3785/3)
[binding keys](http://sublimetext.info/docs/en/reference/key_bindings.html)
终端执行view.run_command("show_scope_name")就可以得到selector


# console
[在console中执行命令](http://docs.sublimetext.info/en/latest/extensibility/commands.html?highlight=console)


# vintageous
[vintageouse 命令，状态等等](http://nullege.com/codes/search/Vintageous)

# theme
[全面的介绍](http://docs.sublimetext.info/en/latest/reference/color_schemes.html?highlight=theme)
[betterFindBuffer 背景渲染BFBForceColorSchemeCommand](https://github.com/aziz/BetterFindBuffer/blob/master/find_results.py)

#settings
[Preference.sublime-settings选项](http://docs.sublimetext.info/en/latest/reference/settings.html)

#TODO
1. 找到build是不显示error的原因
1. 扩展openUrl插件，在build output中，找到对应位置。在md相对路径中，打开相对路径文件。
1. 优化markdowneditor, wrap行时，wrap宽度为实际宽度
1. 优化easymotion扩展到两个字母
1. 找到相对行的插件
1. 将shift+backspace绑定为delete
1. 命令模式中的H,-等，当作为r或f的第二个命令参数时，不进行Pane切换
1. vintageous ex-mode中没有:g/^$/d这样的命令
1. md中n跳转题目
可能实现不了1. 扩展buidView插件，显示warning为黄色，显示error为红色