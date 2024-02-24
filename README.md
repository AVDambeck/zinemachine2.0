# Zine Machine!	
The much improved version of [zinemachine 1.0](https://github.com/AVDambeck/ZineMachine)! Improvements include:

+ Being much faster! 
+ No more buggy html!
+ Better organized!
+ Unified template scheme! 
+ Fewer dependancies!

However it's still rough around the edges, especially in documentation. I've tried my best to make the code clean and interpretable if you are a nerd. But i'm still struggling to reach my intended audiance of dweebs. Sorry....  

Also theres one really big feature I havent made yet: signature logic. Books are printed in [signatures](https://en.wikipedia.org/wiki/Section_(bookbinding)). The math behind how you have to print these is intuitive but complicated. I want to encorperate the logic of it into a module so that artists can fully explore the possibilities of domestic printers. I have the math behind it worked out on a notebook page, I just need a long weekend to program it out. Like once do that work have the computer handle the logic for letter folio (semiletter booklet), extending to [quarto](https://en.wikipedia.org/wiki/Section_(bookbinding)) is easy! And from there the possibilities really expand: doing it in 6ths, doing it in 3rds and using a [stab binding](https://en.wikipedia.org/wiki/Section_(bookbinding)) 

Also a gui would probobly help a lot of people.... I've never really coded a gui before so I'd have to teach myself a lot of stuff.

# Installation
1. Clone the repo locally.
2. Install pypdf (python module).
3. Install pdftk. 
3. Good to go!

# Basic Usage
1. Put 8 jpgs that are 2.25x4.75in in inpagelets dir.
2. python makezine.py.
3. accordian stlye print file will be made at PRINT.pdf (it will overwrite previous files).

# Advanced Usage
1. vim makezine.py. :^)
2. Go to line 15. 
3. Change which template is being used. (see template dir for examples)
4. Repeate basic usage.

# Cross Platform Support
So I haven't specifically prioritized this, and also I don't have the hardware to test it. Also I have a supiriory complex because I use linux. My software is ***FREE*** as in ***FREEEDOMEME***!11!!!! 

## Mac
I think this will all run on mac except for the bash scripts? Idk I've never tried doing anything technical on a mac because Steve Jobs daddy doesn't want me too.

## Windows 
Running this native on windows, i think the same thing. I think the pdf tools are cross platform so in theory it might run. IMO tho ur probobly better off using a linux subsystem (or getting of your cringe ass os and install linux for real >:3) 

# Support
Best place is to reach out to me via [email](AudioVisual@Dambeck.org). I'm very friendly, just also very busy.

# Technical Notes
## AutoCrop
Debug mode disables clearing the cache so the files can be examined.
