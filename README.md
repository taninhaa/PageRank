# PageRank

#### Introduction 
Our project was based on calculating the PageRank of Wikipedia pages in order to create a usefull tool that everyone can use.  
Actually, we have created a tool you can use on **your terminal** to search informations on a word.  
In this repository gitHub, you have access to **our codes to calculate the _PageRank_** with different methods.  
You also have access to the **bash script** we have made for our tool as well as **a report** we have made in french to explain our approach.

If you want to see our work and use our tool on your computer, follow the instructions below: 

#### Importation on your computer 

* Create a folder and open it from the terminal. 

* Then, use the command:

`git clone https://github.com/taninhaa/PageRank.git`

Once you have our project on your local repository, you can use our command **_wikisearch_**. 

#### Access to the command _wikisearch_

Open a terminal on you computer by using `Ctrl + Alt + T`. 
Change the directory until you get to the PageRank on your computer by using the command `cd`.  
You can now acess to the _wikisearch_ command by following:

`chmod 755 wikisearch`
or  
`chmod +x wikisearch`

To make this command global (usuable in all directory):

`sudo cp ./wikisearch ~/../../usr/bin/wikisearch` 
`sudo mkdir -p ~/../../usr/share/wikisearch/code ~/../../usr/share/wikisearch/data`
`sudo cp ./code/* ~/../../usr/share/wikisearch/code/` 
`sudo cp ./data/* ~/../../usr/share/wikisearch/data/`

For more information, you can install ower man page with:
`sudo cp ./man ~/../../usr/share/man/man1/wikisearch.1`

Finally you can use:
`wikisearch [-p|-perso] <argument>`. Here, argument is the word you decide to search. 

 ##### Let's make an example:
 We decide to search informations on the word "Hello". 

`wikisearch Hello`

We have the following result: 

![result11](https://user-images.githubusercontent.com/92987223/166294985-332460eb-c91d-4865-b175-cdbd012f168d.png)

You have to choose what page you want to have more informations on among those proposed.  
In our example, we want to know more about the page called _Hello World_ (the fourth page proposed) so we type the number associated `4`.  
Here are the informations given for the page: 

![result2](https://user-images.githubusercontent.com/92987223/166294060-5c64b256-22b3-4dfc-a6fd-dfcd9721759f.png)

You can press `i` to access to the wikipedia page on your browser or press `q` to quit. 

If you want personalised suggestions, you can type:
`wikisearch -perso Hello`

Use the command `man wiki` to have more informations on how to use the command _wikisearch_.
