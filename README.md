<div align="center">
<h1>The Cabin</h1>
<strong>A terminal based text adventure where you have to escape a killer's cabin.</strong>
</div>

<br>

The Cabin is a terminal based game made in the Python, it was made for a computer science class and allowed me to learn a lot about the language. The game itself is a horror text adventure where you can perform actions, look at objects, and piece together the mystery of your arrival.

# INSTALL INSTRUCTIONS
## CURRENTLY LINUX ONLY, WINDOWS AND MACOS BUILDS SOON
<ul>
<li>Go to https://github.com/octantx/cabin-game/releases/tag/v1.0.0-beta and scroll right to the bottom</li>
<li>Click on the "cabin-v1.0.0.zip" to download</li>
<li>Extract to a preferable location</li>
<li>Open the newly extracted folder and double click the executable file</li>
<li>Wallah!</li>
</ul>

# BUILD INSTRUCTIONS
<ul>
<li> Ensure termcolor and pyinstaller are installed (the rest of the dependencies should come with Python 3, but please let me know if I missed one)</li>
<li> Go to https://github.com/octantx/cabin-game/releases/tag/v1.0.0-beta and scroll right to the bottom </li>
<li> Click on the source code file of your choice to download </li>
<li> Extract to a preferable location </li>
<li> Open the newly extracted folder and navigate to /final-build/ (this is where all of the source code is) </li>
<li> Make desireable changes </li>
<li> When ready to build, open your terminal or command prompt application and navigate to /final-build/ </li>
<li> Use the command "pyinstaller --onefile thecabin.py" to build the game </li>
<li> Navigate to /dist/ and place a copy of the /final-build/save.txt file there </li>
<li> The game should now be able to run with your changes! Let me know if there are any issues with these build instructions by opening an issue </li>
