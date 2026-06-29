# Last.FM Discord Widget
This repository will contain information on how to set up a [Last.FM](https://www.last.fm) Widget on your Discord profile (similar to the "Wuthering Waves" widget).

I wanna give a big thanks to [Chloe Cinders](https://chloecinders.com/blog/discord-widgets) for making a blog post about this, and [No Text To Speech](https://youtube.com/@NoTextToSpeech) for making a video tutorial on Chloe's blog post.

## Requirements
Python (I developed this with Python 3.14.3)

"dotenv" Python library (pip install dotenv)

A Discord [developer application](https://discord.com/developers/applications)

## Resources
[Chloe Cinders' Blog Post](https://chloecinders.com/blog/discord-widgets)

[No Text To Speech's YouTube video on Widgets](https://www.youtube.com/watch?v=gYv7D83u7yQ)

[Discord Developer Portal](https://discord.com/developers/applications)

[Last.FM API Account Creation](https://last.fm/api/account/create)

[Tutorial Video](https://files.vivzio.live/api/shares/gPKgv1Cq/files/82e93edd-a1ed-4353-9f04-eb931798cfca?download=false)
###### *I apologize for the very poor video editing, I currently do not have my main editing software installed :(*

## Automatic Stat Updates
The way I do it is by simply using Task Scheduler (because I'm on Windows 10) to run the script every minute (Seems a bit excessive, I know, but it keeps it up to date!) in an invisible command prompt (So I don't get interrupted whilst doing something).

Here are a few links that would help you automatically update your statistics:

### [Windows](https://community.esri.com/t5/python-documents/schedule-a-python-script-using-windows-task/ta-p/915861) (Use pythonw.exe if you don't want a command prompt to appear)

### [MacOS + Linux](https://www.advsyscon.com/blog/python-job-scheduling/)

### Android

[Step 1 - Install Termux](https://termux.dev/en/)

[Step 2 - Install Python on Termux](https://wiki.termux.com/wiki/Python)

[Step 3 - Install Git](https://www.reddit.com/r/termux/comments/18hea2i/comment/kd5z8j5/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) (Make sure when you're running git commands, to replace "git" with "gh")

[Step 4 - Clone this repo into Termux](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) (Or just download the repo ZIP, unzip it, and use it from there)

[Step 5 - Follow the Linux tutorial for scheduling a Python script](https://www.advsyscon.com/blog/python-job-scheduling/)

### iOS . . . You're kinda out of luck . . . I think . . .
