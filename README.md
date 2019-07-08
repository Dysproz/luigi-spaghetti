# luigi-spaghetti
This is quick demo of Luigi by Spotify with example of making spaghetti. Repository contains python script and reveal.js slides.

*~Warsaw, July 2019*

# Requirements
- **luigi** in version 2.8.7
- **Python** in version 3.6
- **reveal.js** in version 3.8.0

# What is done in demo?
Demo is a simple pipeline of preparing spaghetti.
Demo shows basic mechanism of luigi tasks and its' specifics.

Idea of pipeline structure may be described with this graph:
![Idea graph](https://github.com/Dysproz/luigi-spaghetti/blob/master/luigi_img/plan.png)

Which may be technically realized with these operations:
![Tech graph](https://github.com/Dysproz/luigi-spaghetti/blob/master/luigi_img/tech_plan.png)

It means that we want to:
- Create directory *./results/{id}/*
- create files with entries of prepared ingredients (like Chopped garlic, Cooked Meat etc.)
- Connect previously created files in one file *stuffing.txt*
- Connect file *stuffing.txt* and *pasta.txt* into final spaghetti file.

