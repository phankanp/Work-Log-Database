Create a command line application that will allow employees to enter their name, time worked, task worked on, and general notes about the task into a database. There should be a way to add a new entry, list all entries for a particular employee, and list all entries that match a date or search term. Print a report of this information to the screen, including the date, title of task, time spent, employee, and general notes.

# Steps

- As a user of the script, I should be able to choose whether to add a new entry or lookup previous entries.
- As a user of the script, if I choose to enter a new work log, I should be able to provide my name, a task name, a number of minutes spent working on it, and any additional notes I want to record.
- As a user of the script, if I choose to find a previous entry, I should be presented with four options: find by employee, find by date, find by time spent, find by search term.
- As a user of the script, if finding by employee, I should be presented with a list of employees with entries and be able to choose one to see entries from.
- As a user of the script, if finding by employee, I should be allowed to enter employee name and then be presented with entries with that employee as their creator.
- As a user of the script, if finding by date, I should be presented with a list of dates with entries and be able to choose one to see entries from.
- As a user of the script, if finding by time spent, I should be allowed to enter the amount of time spent on the project and then be presented with entries containing that amount of time spent.
- As a user of the script, if finding by a search term, I should be allowed to enter a string and then be presented with entries containing that string in the task name or notes.
- As a fellow developer, I should find at least 50% of the code covered by tests. I would use coverage.py to validate this amount of coverage.
- Menu has a &quot;quit&quot; option to exit the program.
- Records can be deleted and edited, letting user change the date, task name, time spent, and/or notes.
- Can find entries based on a ranges of dates. For example between 01/01/2016 and 12/31/2016.
- If multiple employees share a name (e.g. multiple people with the first name Beth), a list of possible matches is given.
- Records are displayed one at a time with the ability to page through records (previous/next/back).
- As a fellow developer of the script, I should see test coverage of 85% of the code or better.
