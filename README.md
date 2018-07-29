# sublime_text_plugin
Sublime Text plugin to delete characters from specified position in all lines

How to use?
Copy the python file to <Sublime text installation path>/Packages/User

In line 8 of the file, enter the position of character you wish to delete, index starts from 0.
In the file where you want the deletion operation, go to View->Show console.
In the console, type view.run_command("delete")
