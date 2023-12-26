This was a first attempt at a monthly planner. I managed to create some functionality but came to realised
the structure of the program was flawed. It collects the days of months as a list of integers to be displayed.

The list of integers have no access to what month, day or year it is so it is nearly impossible to store text
related to this date in any meaningfull way.

I plan to rewrite in c# (to practice c# skills) and to use WPF as a GUI. I think each day of the month should be an
object instance of its own. Each date can have its own properties i.e text, importance level as well as methods like
print, delete etc.

I am pretty sure this will be a better data structure that will lend itself to be stored in a database more effectivly.
