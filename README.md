TouCon Stage Game
=================

This software was used during TouCon, an event organized by [EMiNA Cyberjaya](http://eminacyber.com/), for the "Fight of Ikedaya Inn" stage activity. The software's purpose is to display quiz questions and answers on a projector display in an interactive and pleasing manner.

Usage
-----

The `randomizer/randomize.py` script reads questions and nodes from a CSV file, randomizes them, and outputs a JavaScript file with the data. It will also output a CSV file with the remaining questions that did not end up in the game.

Questions are specified in the `randomizer/questions.csv` file as question/answer columns. Nodes on the map are specified in the `randomizer/nodes.csv` file as NodeID/Xpos/Ypos columns. There is a bit of configuration stored within the `randomizer/randomize.py` file as well, in the `mapinfo` OrderedDict. The boss node is a node which will always be assigned the same question regardless of randomization, specified as the boss question (1-indexed).

After running the script, you can now open `index.html` in a modern web browser. Clicking on nodes will display a dialog box with the question. Clicking on the Answer button will show the answser. THe dialog box can be dismissed by clicking on the (X) button. The current map can be selected at the bottom left corner. The background music can be played/paused with the button at the bottom right corner.

Copyrights
----------
index.html, style.css, toucon.js, randomize.py follows the text in the `LICENSE` file.

questions.csv, questions.js, remaining.csv (c) EMiNA Cyberjaya.

Touken Ranbu, and related assets (c) DMM/Nitroplus.

jQuery (c) jQuery Foundation

bgm.ogg and helvetica.ttf are not provided due to copyright issues.
