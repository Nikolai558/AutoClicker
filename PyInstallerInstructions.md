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
pyinstaller --noconfirm --clean --onedir --windowed -n "AutoClicker" --version-file "version_info.txt" --icon "./images/icons/auto_clicker_icon.ico" --contents-directory "_AutoClicker_internals" --add-data "images:images" --add-data "README.md:./README" --add-data "LICENSE:./LICENSE" --add-data "<path_from_above>/customtkinter;customtkinter/" "<path_to_script.py>"
```

---
## Step-By-Step Instructions
1) Create a Pull Request for `Releases <- Main`
2) Change the information required in `version_info.txt`
3) Update Changelog (if one exists)
4) Save and Commit Changes into the `Main` branch
5) Follow instructions above using pyinstaller.
6) Zip the AutoClicker file located in `dist`
7) Complete the Pull Request
8) Draft a new Release (version and tag should match version_info.txt)
9) Upload the Zip Folder
10) Publish the Release
