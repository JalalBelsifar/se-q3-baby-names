<img src="img/sad_baby.png" height="120px"/>

# Baby Names 

The Social Security administration has this neat data of which names are most popular for babies born each year in the USA (see [social security baby names](http://www.socialsecurity.gov/OACT/babynames/)). The files `baby1990.html`, `baby1992.html`, ... contain raw HTML, similar to what you get when visiting the above social security site. Take a look at the HTML and think about how you might scrape the data out of it.

You will need to add your own code to [babynames.py](./babynames.py) to complete this assignment.

## Part A
------

In the [babynames.py](./babynames.py) file, implement the `extract_names(filename)` function, which takes the filename of a single `babyXXXX.html` file and returns the data from the file as a single list &mdash; the year string at the start of the list, followed by the name-rank strings in alphabetical order. Make sure the returned list is a pure python list, not a 'stringified' version of the list.
```
['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', 'Abbey 695', ...] 
```
Modify `main(args)` so it calls your `extract_names(filename)` function and prints what it returns (main already has the code for the command line argument parsing). If you get stuck working out the regular expressions for the year and each name, regular expression pattern solutions are shown at the end of this README. Note that for parsing webpages in general, regular expressions don't do a good job, but these webpages have a simple and consistent format.

Rather than treat the boy and girl names separately, we'll just lump them all together. In some years, a name appears more than once in the HTML, but we'll just use one rank number per name. 

Build the program as a series of small milestones, getting each step to run/print something before trying the next step. This is the pattern used by experienced programmers &mdash; build a series of incremental milestones, each with some output to check, rather than building the whole program in one huge step.

Printing the data you have at the end of one milestone helps you think about how to restructure that data for the next milestone. Python is well suited to this style of incremental development. For example, first get it to the point where it extracts and prints the year. Here are some suggested milestones:

*   Extract all the text from the file and print it
*   Find and extract the year and print it
*   Extract the names and rank numbers and print them
*   Get the names data into a dict and print it
*   Build the `[year, 'name rank', ... ]` list and print it
*   Fix `main()` to use the extracted_names list

Before, we have made functions that just print their result. It's more reusable to have the function *return* the extracted data, so then the caller has the choice to print it or do something else with it (You can still print directly from inside your functions for your little experiments during development). This illustrates the principle of _Separation of Concerns_.  Have one function that delivers the data, and a different one to print or write the the data to a file. This builds _modularity_ into your program so that it is easier to maintain.

Have `main()` call `extract_names()` for each command line argument and print the results vertically. To make the list into a reasonable looking summary text, here's a clever use of `join()`: `text = '\n'.join(mylist)`

The summary text should look like this for each file:
```
2006
Aaliyah 91
Aaron 57
Abagail 895
Abbey 695
Abbie 650
...
```

## Part B
------

Suppose instead of printing the text, we want to write files containing the text. If the flag `--summaryfile` is present on the command line, do the following: for each input file `babyXXXX.html`, instead of printing, write a new file `babyXXXX.html.summary` that contains the summary text for that file.

Once the `--summaryfile` feature is working, run the program on all the files using `*` like this:  
`python babynames.py --summaryfile baby*.html`.  
This generates all the summaries in one step. (The standard behavior of the shell is that it expands the `baby*.html` pattern into the list of matching filenames, and then the shell runs babynames.py, passing in all those filenames in the `sys.argv` list.)

With the data organized into summary files, you can see patterns over time with shell commands, like this:
```
$ grep 'Trinity ' *.summary
$ grep 'Nick ' *.summary
$ grep 'Miguel ' *.summary
$ grep 'Emily ' *.summary
```

**Regular expression hints**
- year:  `r'Popularity\sin\s(\d\d\d\d)`
- names: `r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'`


## Testing with Unittest
This assignment has separate unit tests to help you during development. The unit tests are located in the `tests` folder; you should not modify these.  Make sure all unit tests are passing before you submit your solution. You can invoke the unit tests from the command line at the root of your project folder:
```console
$ python -m unittest discover tests
```
You can also run and debug these same tests using the `Test Explorer` extension built in to the VSCode editor, by enabling automatic test discovery.  This is a really useful tool and we highly recommend to learn it.

https://code.visualstudio.com/docs/python/testing#_test-discovery

- Test framework is `unittest`
- Test folder pattern is `tests`
- Test name pattern is `test*`

## Submitting your work
To submit your solution for grading, you will need to create a github [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).  Refer to the `PR Workflow` article in your course content for details.
