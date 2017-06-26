# BurnTracker

A python program that assists users in losing weight by calculating daily caloric consumption and by tracking daily weight loss.

<img width="800" alt="screen shot 2017-06-26 at 2 03 23 pm" src="https://user-images.githubusercontent.com/20529105/27555802-cb9663a6-5a78-11e7-80d2-68f99c2a1dd8.png">


<img width="790" alt="screen shot 2017-06-26 at 2 08 28 pm" src="https://user-images.githubusercontent.com/20529105/27555849-f65ac1c2-5a78-11e7-9448-b6b70b952cb8.png">


The program's GUI was created with TKinter. 

Users first create a profile in which they enter in physical attributes necessary to calculate and track their progress to reach their fitness goals. (They can edit this data as it changes over time)

With this data, the program calculates a diet plan which includes the number of calories to consume daily in order to maintain a caloric deficit determined by the user. 

As users lose weight, the program adjusts their caloric intake to prevent weight plateaus. 

User profile data can be represented as a graph using matplotlib. 

User profile objects are pickled so the structures holding the data can be retrieved the next time the user accesses the program. 


*The pickled files must always remain in the same directory as the script or it will think you are trying to create a new profile.*



