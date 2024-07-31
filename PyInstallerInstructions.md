## Using PyInstaller
When you create a .exe on Windows with pyinstaller, there are two things you have to consider.

Firstly, you cannot use the `--onefile` option of pyinstaller, because the customtkinter library 
includes not only .py files, but also data files like .json and .otf. PyInstaller is not able to 
pack them into a single .exe file, so you **have to use** the `--onedir` option.

And secondly, you have to include the customtkinter directory manually with the `--add-data` option 
of pyinstaller. Because for some reason, pyinstaller doesn't automatically include datafiles like 
.json from the library. You can find the installation location of the customtkinter library with the 
following command:

```bash
pip show customtkinter
```

Then add the library folder like this:
```
--add-data "<path_from_above>\customtkinter;customtkinter\"
```

For the full command, you get something like this:
```bash
pyinstaller --noconfirm --onedir -- windowed -- add-data "<path_from_above>/customtkinter;customtkinter/" "<path_to_python_script>"
```