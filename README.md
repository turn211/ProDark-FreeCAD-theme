## ProDark FreeCAD theme

FreeCAD Dark theme with 4k monitor small font fix (defaults to 10) but can be changed in `InitGui.py` with text editor.

## Installation

### Automatic

As of v0.19.2 ProDark theme is bundled in to FreeCAD.  
1. Go to `Edit > Preferences > General` and pick ProDark from Style sheet section. 
2. Change Size of toolbar icons: to Medium(24px) 

### Manual

<details>
  <summary>Instructions for installing the ProDark manually. This may be of use for users who want to test new changes or make their own changes to the theme.</summary>

#### Linux and macOS

1. Download ProDark repository via zip file or `git` in to your default FC folder
    `cd ~/.FreeCAD/Gui/Stylesheet` # you may need to create Gui/Stylesheet dirs beforehand
    `git clone https://github.com/turn211/ProDark-FreeCAD-theme.git`
2. Restart FreeCAD
3. Activate stylesheet by invoking `Edit > Preferences > General` and pick ProDark from Style sheet section. 
4. Change Size of toolbar icons: to Medium(24px) 
5. Click `Ok`

#### Windows 10

1. Install ProDark.qss into FreeCAD Folder\data\Gui\Stylesheets\ 
2. Install HighRezMonitor Folder with InitGui.py into C:\Users\UserName\AppData\Roaming\FreeCAD\Mod\
3. In FreeCAD go to `Edit > Preferences > General` and pick ProDark from Stylesheet, Change Size of toolbar icons: to Medium(24px) and Apply/Ok
4. To have Startpage and User Colors the same as Screenshots, choose same colors in `Edit > Preferences` as written in the [ProDark-FreeCAD-Theme_user_preferences_colors.txt](https://github.com/turn211/ProDark-FreeCAD-theme/blob/main/ProDark-FreeCAD-Theme_user_preferences_colors.txt) file

</details>

## Discussion

Feel free to discuss this theme and addon on [New ProDark Theme with 4k small text Mod](https://forum.freecadweb.org/viewtopic.php?f=34&t=55134&start=0)

## Screenshots

Right Click/View Image too see in 2K

![screenshot](images/Working_plane_and_color_setup.png "Working plane and color setup")
![screenshot](images/Startpage_and_Preferences.png "Startpage and Preferences")
![screenshot](images/Report_View_and_Python.png "Report View and Python")
![screenshot](images/Playing_Nice_with_Others.png "Playing Nice with Others")
![screenshot](images/FreeCAD_and_Blender.png "FreeCAD and Blender")
![screenshot](images/4K_Text_size_MOD.png "4K Text size MOD")

## License

CC0 1.0 Universal (see [LICENSE](LICENSE))
