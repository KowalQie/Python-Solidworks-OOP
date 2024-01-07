# Python-Solidworks-OOP
Manipulate dimensions of global variables in SolidWorks using Python 

Hello,
I want to introduce you to programm that can you use for manipulate the global variables in Solid Works part by using Python.

![Przechwytywanie](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/f7476a3d-32b9-462c-96ba-efa0ab30e316)

Here are the steps that you can follow to achieve this:

1.	Copy the code in the main.py to your Python IDE. Python IDE that i’m using is PyCharm.
The variables that i manipulate are defined in the line 6 – line 11:

![line 6 to line 11](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/e8845b45-16ad-4657-b6a9-1de0fa91d3a9)

Define and name the variables that you want to manipulate in SolidWorks and replace them in code. Then save the code in the
Here is the graphic representation of my variables:

![dim1](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/d6004a53-d058-41ee-81da-92baf0c3ab7f)


![dim2](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/8e6a3b8b-4222-4047-ac52-cdb2f07fd7b8)


![dim3](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/b5bde249-a735-4208-9ea0-0343625f0b52)


![dim4](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/8779094f-94fb-4edb-bfe7-b5fc9d58da1c)



3.	Run your code. You have to define values of your dimensions. 
Then, new file ‘dimensions.txt’ will be created in the same place where you save your code. 

4.	Open your Solid Works part.  Then choose: Tools -> Equations. The panel with all your global variables will open. 

5.	Click ‘Link with external file’ and search in the browser file the path for file ‘dimensions.txt’. Accept all chosen global variables.

![polacz](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/c44c44d6-8f00-45e6-93d3-fd7e91ab60d6)

6.	Then you have to choose the dimensions from the operations or sketches in the model in the Equations panel and describe what variable they refer to.

![polacz 2](https://github.com/KowalQie/Python-Solidworks-OOP/assets/152272520/52b00719-7ddf-427c-9ab3-b1873fe4cb38)

Congratulations !

Now you can run your code every time if you want to do some changes in your Solid Works model and Click Rebuild to refresh the view.




