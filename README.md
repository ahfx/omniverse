# omniverse
tinkering with omniverse

## add all subfolder extensions
kit.exe --ext-folder path/extensions
## add specific ext
kit.exe --empty --ext-path path/extensions/omni.ahfx.hello

## search path
C:\Users\[username]\Documents\Kit\shared\exts
If you run kit with -v or look into log file it writes (first line of stdout prints the location) you can see where it searches for extensions. You can also see that in properties page of extensions manager UI.
