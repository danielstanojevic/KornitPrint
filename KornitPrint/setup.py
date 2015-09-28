from cx_Freeze import setup, Executable

exe=Executable(
     script='kornit_print.py',
     base="Win32Gui",
     icon="icon/scanner.ico",
     targetName="Kornit Printing Tool.exe"
     )
includefiles=['ui/','icon/', 'images_rc.py', 'libEGL.dll', 'Kornit Printing Tool.lnk']
includes=['decimal', 'atexit']
excludes=['Tkinter']
packages=['ui']
setup(
     version = "0.1",
     description = "Tool so printers don't have to search for and wait for queries to execute through ms access cmd line",
     author = "David Hoy",
     name = "Kornit Printing Tool",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles,'includes':includes}},
     executables = [exe]
     )