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
This Python script works by prompting you to input a string containing letters and numbers, as well as the desired length of combinations. It then utilizes the `itertools` module 
to generate all possible combinations of the specified length from the input string, allowing for repetition of characters. After generating the combinations, the script saves 
the unique combinations to a text file. Each file is named after the input string and stored in a `combinations` folder within the working directory. 


## How to run the script

1. Clone Repository.
```bash
git clone https://github.com/PetarMc1/combination-generator -b v1.0.0
```

2. Run Script: Open a terminal and run the script.
```bash
python main.py
```

3. Follow Prompt and View Results
You will find the generated combination files in the `combinations` folder.

## Contributing
Check the [Contributing Guidelines](/CONTRIBUTING.md)

## Licence
The Combination Generator is licensed under the [MIT](/LICENCE) Licence
