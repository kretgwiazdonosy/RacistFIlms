# RacistFIlms
Racial detection in films
Are you openly a racist and do refuse to watch any movies with signs of racial tolerance? Or quite the contrary - you're itching to cancel upcoming film on Twitter for not having enough representation of your favourite colour? Well, it doesn't matter, since the tool you are looking at does not discriminate because of political views, but serves every side just as good as it can get. 

The RacistFilms Software is a tool that allows you to perform a quick analysis of race distribution in a film. The way it works is collecting rectangles which contain faces and then using deepface module to determine the ethnic details of a model. This operation is repeated for said number of frames (in default scenario - every 45 frames) up to the end of analyzed video, and then the program goes for the next vid in a directory. The data is being transformed into bar figures for easy comparison.

# Needed modules
Tool requires following modules (in the latest version available) to work:
- glob
- python OpenCV
- keyboard
- plotly
- deepface

# How to use?
1. Put the movies in .mp4 format in materials/videos directory
2. Start the program
3. Let it finish working
If you want to abort analysis (i. e. it takes too much time) just hold Q and wait. 

# Additional info
Although this tool works, I consider this project as aborted, not finished. The reasons are that there is still loads of messy code, the bars are ugly as fuck and the prompts are not translated. I know, it is something that could be fixed in one evening, and there is still possibility that I will make it look a little better, but for now I am just taking a break.

I am really glad that someone found this btw. I know, this program is simple and lacks on the technical side, nonetheless I still love the goofy idea of making a ranking of 'The Most Racist Films Ever'. And this is what I think programing is - fun, a creative playground. Being serious, I hope that using this program will bring you as much fun as it did for me. Also, I find myself obliged to say that this program shouldn't be use in any harmful way. None actor has ever deserved the hate just for playing a particular role, and my sweet non-existent God knows that I don't want to support any form of harassment. Keep the tool as it is - for fun and good times. 

Thanks for discovering me and finishing this wall of text. I do love you, man or woman reading this. Cya in the next repositories!
