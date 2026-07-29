We need to make a new address book.  A major overhaul.

Given our knowledge of Python, let's create a modern address book with the following features

- A user has a terminal where they will `input()` menu choices and add or update contacts

- A user should be able to create, read, update, delete, and search a contact.

- The address book should persist between sessions.  That is, if a user quits and reloads their address book is still there

Some key design requirements:

- Functions broken out for normalization, validation, loading etc.

- loops for handling user input

- Loading and saving data with methods beyond simple `.write()` calls

- Appropriate data structures
