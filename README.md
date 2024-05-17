# Combination Generator
[![Discord](https://img.shields.io/discord/1217057211575042058?logo=Discord&label=Discord&color=blue)](https://discord.gg/8Ab2uuqSYE)
![GitHub Release](https://img.shields.io/github/v/release/PetarMc1/combination-generator?include_prereleases&logo=github&color=red)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/PetarMc1/combination-generator?logo=github)
![GitHub Issues](https://img.shields.io/github/issues/PetarMc1/combination-generator?logo=github)
![GitHub License](https://img.shields.io/github/license/PetarMc1/combination-generator?color=blue)

The Combination Generator is a Python script designed to generate all possible combinations of letters and numbers from a given input string. This tool allows you to specify the 
length of the combinations you wish to generate. The script organizes the generated combinations into text files within a designated folder, with each file named after the 
original input string.


## How it works
Python script featuring a GUI for generating combinations of characters and numbers. Users input a string and combination length, then view and copy generated combinations.
The script simplifies exploring different combinations through an intuitive interface.


## Usage

Download the latest release from the GitHub repository's "Releases" section,
or [build the application](#building) from source code.


## Building

1. Clone the repository.

```bash
git clone https://github.com/PetarMc1/combination-generator
```



2. Install PyInstaller.

If you haven't installed PyInstaller yet, you can install it via pip:

```bash
pip install pyinstaller
```




3. Run PyInstaller command.

Use PyInstaller to convert the script into a `.exe` file with the `--windowed` flag to hide the console window.

```bash
pyinstaller --onefile --windowed combination_generator.py
```
This command will create an executable file (combination_generator.exe) without a console window when opened.




4. Find the `.exe`.

Once PyInstaller has finished, navigate to the `dist` directory inside the repo directory. You will find the executable (`.exe`) file (combination_generator.exe) in this directory.

