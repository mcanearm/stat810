## STATS 810. Unix advice

* The most important thing in terms of Linux is to learn the stuff that makes your life easier, but try to never use ‘sudo‘ when you don’t have to.
Having to use ‘sudo‘ regularly is a sign of a mis-managed environment, and in fact, as a novice user, you shouldn’t even be able to use ‘sudo‘ anyway.
Linux command line is important, but just as important is getting really familiar with file structures and programs, how SSH works, and the nuts of bolts of working on a shared environment.

* Don’t be afraid to write small programs in Python, but use them on the command line.
There’s fast and easy ways to do things, but you can write programs in Python and use system args to interoperate bash and Python processes seamlessly.
Same goes for R, but frankly, Python is just easier to use in a Unix/server environment and if you use R in an industry context, the people in charge of supporting you are going to hate it.

* My biggest mistakes always came from inappropriately changing file permissions. Don’t do it if you can avoid it. Also, you can actually ruin your life really quickly with ‘sudo rm path -rf‘ (I hate even typing it). You have to be extremely careful with Linux commands in the Spiderman sense - with great power comes great responsibility.

----

* I don't know anyone who has ever regretted learning to use the command line.

----

1. Customize your '.bash_profile' or '.zshrc'

2. Keep all files you care about backed up on the cloud, e.g., GitHub or Dropbox. Then, you can use 'rm -rf' as much as you like!

3. Keep a file, or files, recording useful commands and installation procedures.

4. Invest in CLI until it is quicker than GUI for you. From then on, enjoy the payoff!

5. Learn IDEs as well (e.g., vscode) but not at the expense of CLI.

