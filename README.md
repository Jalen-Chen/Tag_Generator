# Tag_Generator
Tag_Gererator will create a Markdown file which contains all tags in your works.
The generotar supports multi-tags as well as multi-level tag.
Each tag within the tag file could link to its orginary file and user could open with a single click.

# Environment
You need Python3 installed in order to use this tool. To check your current Python version, run code below in your terminal:
```shell
python --version
```
There may have some issues with Python2, since Python3 do not compate with Python2 nicely.

# Usage 
Move 'tag_generator.py' to your current working directory, and run code below in your Terminal(macOS) or CMD:
```shell 
python tag_generator.py
```
The script will then check all tags in your files and generator a general outline representing your tag system. 

# Tag foramt
1. Tag should start and end with `#`.
> #Tag1#
2. Tag should use `/` to indicate higher level.
> #Tag1/Tag2#
3. You can add tags anywhere in your Markdown file.
## Attention
1. Since the file is processed by lines, please try to avoid expressions such as `#\S+#` used as commits in your code block.
2. Please make sure that there is no space inside your tag. Adding spaces after `#` will be recognised as Markdown Tittle Foramt instead of Markdown Tags.
3. Please do not use space when creating multiple level tags.
# Maintenance 
If you come accross any problem when using, please feel free to drop me an eamil at `jalen_chen@outlook.com`
