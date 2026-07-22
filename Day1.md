## Day 1: How Computers Work and Introduction to Python

### Day 1 Purpose

Day 1 gives students a practical mental model of what is happening beneath the applications they use every day.

The goal is not to teach electrical engineering or full computer architecture. Instead, students should finish the day understanding:

* How information is represented as bits and bytes
* How processors execute instructions
* The relationship between machine code and Python
* How memory differs from permanent storage
* How files are represented on a storage device
* How programs communicate across networks
* What happens when Python code is executed
* How to write and run simple Python programs

The morning session peels back the layers of a modern computer. The afternoon session connects those concepts directly to Python programming.

---

# Morning Session: What Happens Under the Hood?

## Learning Objectives

By the end of the morning session, students will be able to:

1. Explain that computers represent information using binary values.
2. Distinguish bits, bytes, kilobytes, megabytes, and gigabytes.
3. Describe the basic roles of the processor, memory, storage, and operating system.
4. Explain at a high level how a processor executes machine instructions.
5. Distinguish machine code, compiled languages, and interpreted languages.
6. Explain the difference between memory and permanent storage.
7. Describe how a filesystem maps file names and folders to stored data.
8. Explain the basic purpose of IP addresses, ports, protocols, and servers.
9. Trace what happens when a user opens a website or runs a program.

---

## Block 1: Bits, Bytes, and Digital Information

### Instruction: 30 Minutes

#### Topics

* Computers as machines that manipulate symbols
* Binary values: zero and one
* Bits as the smallest common unit of digital information
* Bytes as groups of eight bits
* Common size units:

  * Byte
  * Kilobyte
  * Megabyte
  * Gigabyte
  * Terabyte
* Binary numbers compared with decimal numbers
* Representing whole numbers in binary
* Representing text using numeric character codes
* High-level introduction to ASCII and Unicode
* Images as grids of numeric pixel values
* Audio as a sequence of numeric samples
* The importance of interpreting the same bits correctly

#### Key Concept

Bits do not inherently represent text, numbers, pictures, or sound. Their meaning depends on how software interprets them.

For example, a particular sequence of bits could represent:

* A number
* A letter
* Part of an image
* A processor instruction
* A portion of a compressed file

### Guided Exercise: 30 Minutes

Students complete several short activities:

1. Convert small decimal numbers to binary.
2. Determine how many possible values can be stored using:

   * One bit
   * Two bits
   * Four bits
   * Eight bits
3. Decode a short sequence of numeric character values into text.
4. Compare the approximate sizes of:

   * A text document
   * A photograph
   * A music file
   * A video file
5. Discuss why a file extension helps software determine how stored bits should be interpreted.

### Suggested Exercise Questions

* How many values can one byte represent?
* Why can the same byte sequence mean different things?
* Why does video usually require more storage than plain text?
* What information must software know before it can correctly interpret a file?

---

## Break: 15 Minutes

---

## Block 2: Processor, Memory, and Program Execution

### Instruction: 30 Minutes

#### Topics

* The processor as an instruction-execution machine
* Machine instructions
* Machine code
* Instruction sets
* Registers
* Arithmetic and logic operations
* Loading and storing values
* Comparing values
* Jumping to another instruction
* The fetch-decode-execute cycle
* Clock cycles and processor speed
* Processor cores
* Why a processor does not directly understand Python
* Source code versus machine code
* Compiled languages
* Interpreted languages
* Virtual machines and runtime environments
* Python as a high-level language
* The Python interpreter
* High-level introduction to Python bytecode

#### Simplified Execution Model

A processor repeatedly performs a cycle similar to:

1. Fetch the next machine instruction.
2. Decode what the instruction means.
3. Execute the instruction.
4. Move to the next instruction.

Python adds several layers above this process:

1. A programmer writes Python source code.
2. The Python runtime reads and processes that source code.
3. Python converts or translates the code into lower-level operations.
4. The processor ultimately executes machine instructions.

#### Important Distinction

The statement:

```python
total = price * quantity
```

is understandable to a human programmer, but the processor does not directly execute that line as written. The Python runtime performs the work required to turn it into operations the processor can execute.

### Guided Exercise: 30 Minutes

Students simulate a basic processor using a paper instruction set.

Example instructions:

```text
LOAD 5
STORE X
LOAD 3
ADD X
STORE RESULT
PRINT RESULT
```

Students:

1. Step through each instruction.
2. Track the value in a simulated processor register.
3. Track values stored in simulated memory.
4. Identify the final output.
5. Compare the low-level instructions with the equivalent Python statement.

Equivalent Python:

```python
x = 5
result = 3 + x
print(result)
```

### Discussion Questions

* Which version is easier for a human to read?
* Which version is closer to what a processor understands?
* What work does Python perform on behalf of the programmer?
* Why might low-level code run faster but be harder to develop?

---

## Break: 15 Minutes

---

## Block 3: Memory, Storage, and Filesystems

### Instruction: 30 Minutes

#### Topics

* Temporary memory versus permanent storage
* Random-access memory
* Variables as names associated with values in memory
* Running programs and processes
* Program memory
* Stack and heap as high-level concepts
* Solid-state drives and hard drives
* Storage blocks and sectors
* Reading and writing blocks of data
* Why storage devices do not inherently understand file names
* The purpose of a filesystem
* Filesystem metadata
* File tables and directory structures
* File names and extensions
* File size
* Creation and modification timestamps
* Permissions
* Folders as logical organization
* File paths
* Fragmentation as a conceptual issue
* Deleted files and reused storage
* Why renaming a file usually does not rewrite all of its contents

#### Practical Filesystem Mental Model

A storage device can be imagined as a very large collection of numbered storage locations or blocks.

The filesystem maintains organized records that describe:

* The file's name
* Where its data is stored
* How large it is
* Who may access it
* When it was created or changed
* Which folder contains it

The name displayed to the user is therefore not physically printed onto the storage device beside the file contents. The name is stored as metadata that points to the relevant data blocks.

#### Example

When a user renames:

```text
report1.csv
```

to:

```text
quarterly_sales.csv
```

the operating system will often update the file's metadata rather than rewriting the entire data file.

### Guided Exercise: 30 Minutes

Students work through a simplified paper filesystem.

They receive:

* A list of numbered storage blocks
* Several files occupying different blocks
* A simplified file allocation table
* A folder hierarchy
* File metadata records

Students complete tasks such as:

1. Locate the blocks belonging to a particular file.
2. Rename a file by changing metadata.
3. Move a file to another folder without changing its contents.
4. Delete a file entry and identify which blocks become available.
5. Explain why deleting a file does not always immediately erase every underlying bit.
6. Explain what happens when a program opens a file by name.

### Discussion Questions

* Why does a computer need a filesystem?
* What is the difference between a file's name and its contents?
* Why can moving a file on the same drive be fast?
* Why might moving a file to another drive take longer?
* Why can a file exist even though its data is not stored in one continuous location?

---

## Block 4: Networking and the Internet

### Instruction: 30 Minutes

#### Topics

* Computers communicating across networks
* Local networks and the internet
* Network interfaces
* Packets
* IP addresses
* Private and public IP addresses
* Domain names
* Domain Name System
* Ports
* Clients and servers
* Requests and responses
* Common protocols
* HTTP and HTTPS
* Encryption at a high level
* Routers
* Firewalls
* Latency and bandwidth
* Application programming interfaces as structured network communication

#### Simplified Website Request

When a user enters a website address:

1. The browser identifies the domain name.
2. DNS helps locate the corresponding IP address.
3. The browser connects to a server.
4. The browser sends an HTTP request.
5. The server processes the request.
6. The server returns a response.
7. The browser interprets and displays the response.

#### Connection to Future Python Work

Python programs can act as:

* Clients requesting data
* Servers responding to requests
* Data-processing applications
* Automation tools
* Interfaces between databases and services

### Guided Exercise: 30 Minutes

Students arrange cards representing the steps involved in opening a website.

Cards may include:

* User enters a URL
* Browser requests an IP address
* DNS returns an address
* Browser opens a connection
* Browser sends an HTTP request
* Server processes the request
* Server sends a response
* Browser displays the page

Students then identify:

* The client
* The server
* The address
* The protocol
* The request
* The response

### Morning Applied Challenge and Review: 30 Minutes

Students trace two complete scenarios.

#### Scenario 1: Opening a Spreadsheet

Students explain, at a high level:

1. Where the application is stored
2. How the operating system loads it
3. How data moves into memory
4. How the processor executes instructions
5. How the application locates a spreadsheet file
6. How the filesystem provides the file contents
7. How the application displays the data

#### Scenario 2: Opening a Website

Students explain:

1. How the computer identifies the destination
2. How a network connection is established
3. How a request is sent
4. How the server responds
5. How the browser converts the response into a displayed page

#### Morning Knowledge Check

Students should be able to explain the following in plain language:

* A bit
* A byte
* Machine code
* An interpreter
* Memory
* Storage
* A filesystem
* An IP address
* A port
* A client and server

---

# Afternoon Session: Introduction to Python

## Learning Objectives

By the end of the afternoon session, students will be able to:

1. Explain where Python fits between human-readable code and machine execution.
2. Run Python statements in an interactive environment.
3. Create and execute a Python script or notebook.
4. Use `print()` to display output.
5. Create variables.
6. Use strings, integers, floating-point numbers, and Boolean values.
7. Perform basic arithmetic.
8. Inspect the type of a value.
9. Read simple Python error messages.
10. Connect Python variables to the morning discussion of memory and data representation.

---

## Block 1: From Human Instructions to Python Code

### Instruction: 30 Minutes

#### Topics

* Programs as precise sets of instructions
* Algorithms
* Pseudocode
* Source code
* Programming languages
* Why Python is considered a high-level language
* The role of the Python interpreter
* Interactive execution
* Scripts
* Notebooks
* Statements
* Expressions
* Comments
* Execution order

#### Connecting to the Morning Session

Students should understand the following sequence:

```text
Human idea
    ↓
Algorithm or pseudocode
    ↓
Python source code
    ↓
Python runtime
    ↓
Lower-level operations
    ↓
Machine instructions
    ↓
Processor execution
```

#### Demonstration

The instructor writes:

```python
print("Hello, world!")
```

The class discusses:

* Which part is the function name
* Which part is data
* Which part is syntax
* What the Python runtime must do
* What eventually reaches the processor
* What appears as output

### Guided Exercise: 30 Minutes

Students:

1. Open the Python environment.
2. Run several `print()` statements.
3. Print numbers and text.
4. Add comments.
5. Intentionally create a minor syntax error.
6. Correct the error.
7. Predict output before executing code.

Example:

```python
print("Python is running.")
print(2 + 3)
print("The answer is", 2 + 3)
```

### Exercise Goal

Students should become comfortable executing code and seeing immediate results without needing to understand every detail of the development environment.

---

## Break: 15 Minutes

---

## Block 2: Variables and Values

### Instruction: 30 Minutes

#### Topics

* Values
* Variables
* Assignment
* Variable names
* Naming conventions
* Reassignment
* Strings
* Integers
* Floating-point numbers
* Boolean values
* The `type()` function
* Variables as names associated with objects or values
* Memory as a conceptual model
* The difference between a variable name and the stored value

#### Example

```python
employee_name = "Jordan"
years_of_service = 8
hourly_rate = 32.50
is_active = True
```

The instructor connects these values to the morning lesson:

* Text is encoded as numeric data.
* Numbers are stored using binary representations.
* Variables allow the programmer to refer to values using meaningful names.
* The Python runtime manages many memory details for the programmer.

### Guided Exercise: 30 Minutes

Students create variables describing a fictional project:

```python
project_name = "Sensor Upgrade"
team_size = 6
budget = 125000.00
is_complete = False
```

Students then:

1. Print each value.
2. Print each value's type.
3. Change one value.
4. Print the updated value.
5. Create a variable based on another variable.
6. Explain which values represent text, whole numbers, decimal numbers, and true-or-false conditions.

---

## Break: 15 Minutes

---

## Block 3: Expressions and Basic Calculations

### Instruction: 30 Minutes

#### Topics

* Expressions
* Arithmetic operators
* Addition
* Subtraction
* Multiplication
* Division
* Integer division
* Remainders
* Exponents
* Order of operations
* Combining variables in calculations
* Storing calculation results
* Common errors involving incompatible data types

#### Example

```python
unit_price = 12.50
quantity = 8
total_cost = unit_price * quantity

print(total_cost)
```

#### Connection to Processor Instructions

Students revisit the fact that a simple Python expression may require many lower-level operations:

* Locate the values
* Determine their types
* Perform the multiplication
* Allocate or reuse memory
* Associate the result with a variable name
* Convert the result into displayable text
* Send the output to the screen

### Guided Exercise: 30 Minutes

Students write calculations for:

* Total cost
* Average score
* Percentage complete
* Miles converted to kilometers
* Minutes converted to hours and remaining minutes
* Storage converted from bytes to kilobytes or megabytes

Example:

```python
completed_tasks = 18
total_tasks = 24
percent_complete = completed_tasks / total_tasks * 100

print(percent_complete)
```

---

## Block 4: Strings, Output, and First Program

### Instruction: 30 Minutes

#### Topics

* String literals
* Quotation marks
* Combining strings
* Converting values to strings
* Formatted string literals
* Readable program output
* Code execution from top to bottom
* Simple debugging
* Syntax errors
* Name errors
* Type errors
* Reading the final line of an error message

#### Example

```python
project_name = "Network Modernization"
completed_tasks = 18
total_tasks = 24
percent_complete = completed_tasks / total_tasks * 100

print(f"Project: {project_name}")
print(f"Completed tasks: {completed_tasks}")
print(f"Progress: {percent_complete:.1f}%")
```

### Guided Exercise: 30 Minutes

Students create a short system-information or project-summary program containing:

* At least four variables
* At least three data types
* At least two calculations
* At least four lines of formatted output
* At least one comment

Example output:

```text
Project: Network Modernization
Team size: 5
Completed tasks: 18 of 24
Progress: 75.0%
Status active: True
```

### Applied Challenge and Knowledge Check: 30 Minutes

Students build a simple data-storage calculator.

The program should:

1. Store a file name.
2. Store the file size in bytes.
3. Convert the size to kilobytes.
4. Convert the size to megabytes.
5. Print a formatted summary.
6. Identify the Python type of each variable.

Example:

```python
file_name = "equipment_records.csv"
size_bytes = 2_500_000

size_kilobytes = size_bytes / 1_000
size_megabytes = size_bytes / 1_000_000

print(f"File: {file_name}")
print(f"Bytes: {size_bytes}")
print(f"Kilobytes: {size_kilobytes}")
print(f"Megabytes: {size_megabytes}")
```

Students then explain:

* How the file name is represented conceptually
* How the numeric values are stored
* What the Python interpreter does
* What the processor ultimately executes
* Why the output is different from the values as represented internally

---

# Day 1 End-of-Day Outcomes

By the end of Day 1, students should have a useful conceptual model of a computer as a layered system:

```text
User
    ↓
Application or Python program
    ↓
Operating system and runtime
    ↓
Memory, filesystems, and networking
    ↓
Machine instructions
    ↓
Processor and hardware
```

Students should also be able to write and execute a small Python program using:

* Comments
* `print()`
* Variables
* Strings
* Integers
* Floating-point values
* Boolean values
* Arithmetic expressions
* Formatted output

The intended result is not mastery of computer architecture. Students should instead have enough understanding to recognize that Python programs operate within a larger system involving processors, memory, storage, filesystems, operating systems, and networks.
