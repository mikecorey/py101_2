# Python Programming and Data Engineering Foundations

## Course Overview

This intensive 10-day course introduces adult learners to computer fundamentals, computational thinking, Python programming, data analysis, and production-style data workflows.

The course assumes no previous programming experience. Students begin with basic computer concepts such as files, folders, applications, and command-line navigation. They progressively develop the ability to write, debug, test, and organize Python programs that ingest, transform, validate, analyze, and publish structured data.

The course emphasizes hands-on practice. By the end of the course, students will be prepared to contribute to Python-based projects in a managed enterprise data environment under the guidance of an experienced developer.

## Course Duration

* 10 instructional days
* 8 hours per day
* 80 total instructional hours
* One four-hour morning session
* One four-hour afternoon session

## Intended Audience

This course is designed for:

* Adults with little or no programming experience
* Analysts transitioning into technical roles
* Engineers or subject-matter experts who need to work with data
* Team members who will develop or maintain Python-based data workflows
* Users who need to work effectively in notebook, code repository, and data-pipeline environments

## Prerequisites

No programming experience is required.

Students should be able to:

* Use a keyboard and mouse
* Access websites using a browser
* Follow written instructions
* Perform basic arithmetic
* Save and open documents

## Course Learning Outcomes

By the end of the course, students will be able to:

1. Navigate a computer file system and understand files, folders, paths, and extensions.
2. Use a terminal or command prompt to perform basic development tasks.
3. Explain foundational computer science concepts such as algorithms, abstraction, state, data structures, and complexity.
4. Write Python programs using variables, expressions, conditions, loops, functions, and collections.
5. Read and write CSV, JSON, and text files.
6. Use Python libraries to clean, combine, summarize, and validate tabular data.
7. Understand schemas, records, tables, relationships, joins, and aggregations.
8. Organize Python code into reusable functions and modules.
9. Use exceptions, logging, assertions, and tests to diagnose problems.
10. Use Git-based version control for basic development workflows.
11. Build reproducible, idempotent data transformations.
12. Model a multi-step data process as a dependency graph.
13. Document a Python project so another developer can understand and run it.
14. Build and present a complete data-processing capstone project.

# Instructional Format

## Standard Four-Hour Session

Most morning and afternoon sessions use the following structure:

| Time      | Activity                                                  |
| --------- | --------------------------------------------------------- |
| 0:00–0:30 | Instructor lesson and demonstration                       |
| 0:30–1:00 | Guided student exercise                                   |
| 1:00–1:15 | Break                                                     |
| 1:15–1:45 | Instructor lesson and demonstration                       |
| 1:45–2:15 | Guided student exercise                                   |
| 2:15–2:30 | Break                                                     |
| 2:30–3:00 | Instructor lesson and demonstration                       |
| 3:00–3:30 | Guided or independent exercise                            |
| 3:30–4:00 | Applied challenge, review, questions, and knowledge check |

This format provides at least 90 minutes of direct instruction and 90 minutes of exercises during each standard session.

The capstone sessions use longer development periods with brief instructor check-ins.

# Course Schedule

## Day 1: Computer Fundamentals and First Python Programs

### Morning Session: Understanding the Computer

#### Learning Objectives

Students will be able to:

* Identify the major components of a computer system.
* Explain the difference between hardware, software, operating systems, and applications.
* Create, rename, move, copy, and delete files and folders.
* Understand absolute and relative file paths.
* Recognize common file extensions.
* Perform basic terminal navigation.

#### Instructional Topics

**Lesson 1: How Computers Work**

* Hardware and software
* CPU, memory, storage, and networks
* Operating systems
* Applications and processes
* Input, processing, output, and storage

**Exercise**

Students identify computer components and trace what happens when a document or application is opened.

**Lesson 2: Files and Folders**

* Files, directories, and folder hierarchies
* File names and extensions
* Absolute and relative paths
* Local storage and network storage
* Safe file-management practices

**Exercise**

Students create a course folder structure, move files between folders, rename files, and locate files using paths.

**Lesson 3: Introduction to the Terminal**

* Graphical interfaces versus command-line interfaces
* Current working directory
* Listing directory contents
* Changing directories
* Creating and removing folders
* Running commands safely

**Exercise**

Students reproduce their course folder structure using terminal commands.

#### Applied Challenge

Students receive a disorganized folder containing several file types and reorganize it according to written requirements.

---

### Afternoon Session: Introduction to Python

#### Learning Objectives

Students will be able to:

* Explain what a programming language does.
* Run Python code in an interactive environment.
* Use `print()` to display information.
* Create variables.
* Recognize strings, integers, floating-point numbers, and Boolean values.
* Read basic Python error messages.

#### Instructional Topics

**Lesson 1: Programs and Algorithms**

* What programming is
* Instructions and execution order
* Algorithms
* Pseudocode
* Syntax and semantics
* Source code and interpreters

**Exercise**

Students write pseudocode for familiar activities such as making coffee, logging into a computer, or calculating a total.

**Lesson 2: First Python Statements**

* Running Python
* Code cells and scripts
* The `print()` function
* Comments
* Statements and expressions

**Exercise**

Students create and run a short program that displays a formatted personal introduction.

**Lesson 3: Variables and Data Types**

* Variable assignment
* Naming conventions
* Strings
* Integers
* Floating-point numbers
* Boolean values
* The `type()` function

**Exercise**

Students create variables representing an employee, project, cost, completion status, and number of records.

#### Applied Challenge

Students build a simple project-summary program that stores information in variables and prints a readable report.

## Day 2: Expressions, Decisions, and Program Flow

### Morning Session: Working with Values

#### Learning Objectives

Students will be able to:

* Perform mathematical calculations in Python.
* Combine and format strings.
* Convert between common data types.
* Compare values.
* Use Boolean expressions.

#### Instructional Topics

**Lesson 1: Operators and Expressions**

* Arithmetic operators
* Order of operations
* Assignment operators
* Integer and floating-point division
* Remainders
* Common calculation errors

**Exercise**

Students calculate totals, averages, percentages, and unit conversions.

**Lesson 2: Strings**

* String literals
* Concatenation
* String length
* Indexing and slicing
* Common string methods
* Formatted string literals

**Exercise**

Students clean and format names, identifiers, and status messages.

**Lesson 3: Comparisons and Booleans**

* Equality and inequality
* Greater-than and less-than comparisons
* `and`, `or`, and `not`
* Truth values
* Membership testing

**Exercise**

Students create Boolean expressions that determine whether records meet specified requirements.

#### Applied Challenge

Students create a data-quality checker that evaluates whether several manually entered values are complete and within acceptable ranges.

---

### Afternoon Session: Conditional Logic

#### Learning Objectives

Students will be able to:

* Use `if`, `elif`, and `else`.
* Create nested conditions.
* Combine multiple business rules.
* Trace the execution path of a program.

#### Instructional Topics

**Lesson 1: Basic Conditional Statements**

* Decision-making in programs
* Indentation
* `if` statements
* `if` and `else`
* Execution paths

**Exercise**

Students classify numeric values as positive, negative, or zero.

**Lesson 2: Multiple Conditions**

* `elif`
* Range checks
* Compound Boolean expressions
* Avoiding unnecessarily complex conditions

**Exercise**

Students classify records into categories based on several rules.

**Lesson 3: Validation and Defensive Programming**

* Checking inputs before using them
* Empty values
* Invalid types
* Boundary conditions
* Fail-fast behavior

**Exercise**

Students build a small validation program for a fictional equipment record.

#### Applied Challenge

Students create a rule-based record classifier that assigns a status such as valid, warning, or rejected.

## Day 3: Collections and Repetition

### Morning Session: Python Data Structures

#### Learning Objectives

Students will be able to:

* Store multiple values in Python collections.
* Select an appropriate collection for a problem.
* Add, update, retrieve, and remove collection elements.
* Represent a structured record using a dictionary.

#### Instructional Topics

**Lesson 1: Lists and Tuples**

* Ordered collections
* Indexing
* Slicing
* Adding and removing values
* Mutable and immutable objects
* When to use lists and tuples

**Exercise**

Students maintain a list of measurements and calculate basic summary values.

**Lesson 2: Dictionaries**

* Keys and values
* Retrieving and updating values
* Dictionary methods
* Representing records
* Missing keys

**Exercise**

Students represent employees, assets, or transactions as dictionaries.

**Lesson 3: Sets and Collection Selection**

* Unique values
* Removing duplicates
* Membership testing
* Set operations
* Choosing among lists, tuples, dictionaries, and sets

**Exercise**

Students compare two lists of identifiers and determine shared, missing, and unique values.

#### Applied Challenge

Students convert several unstructured values into a collection of consistently structured dictionary records.

---

### Afternoon Session: Loops and Iteration

#### Learning Objectives

Students will be able to:

* Repeat operations using `for` and `while` loops.
* Iterate through lists and dictionaries.
* Use counters and accumulators.
* Stop or skip loop iterations.
* Write basic list comprehensions.

#### Instructional Topics

**Lesson 1: `for` Loops**

* Iteration
* Loop variables
* Iterating through strings and lists
* `range()`
* Accumulators

**Exercise**

Students process a list of values and calculate totals, counts, minimums, and maximums.

**Lesson 2: Iterating Through Records**

* Looping through dictionaries
* Lists of dictionaries
* Nested loops
* `enumerate()`
* `zip()`

**Exercise**

Students process a collection of records and generate a formatted report.

**Lesson 3: Loop Control and Comprehensions**

* `break`
* `continue`
* Loop conditions
* Infinite loops
* List comprehensions
* Readability considerations

**Exercise**

Students filter and transform values using both traditional loops and comprehensions.

#### Applied Challenge

Students create a small data-processing program that filters invalid records, transforms valid records, and calculates summary statistics.

## Day 4: Functions, Program Design, and Debugging

### Morning Session: Functions and Abstraction

#### Learning Objectives

Students will be able to:

* Create and call functions.
* Pass values through parameters.
* Return values.
* Explain local and global scope.
* Break a large problem into smaller functions.

#### Instructional Topics

**Lesson 1: Creating Functions**

* Function definitions
* Function calls
* Parameters and arguments
* Return values
* Single-responsibility functions

**Exercise**

Students convert repeated calculations into reusable functions.

**Lesson 2: Function Design**

* Required and optional parameters
* Default arguments
* Keyword arguments
* Pure functions
* Side effects
* Function composition

**Exercise**

Students build a series of functions that validate and transform one record.

**Lesson 3: Scope, Documentation, and Type Hints**

* Local scope
* Global scope
* Variable lifetime
* Docstrings
* Type hints
* Function contracts

**Exercise**

Students add documentation and type hints to previously written functions.

#### Applied Challenge

Students refactor a long procedural program into a collection of small, documented functions.

---

### Afternoon Session: Errors, Debugging, and Testing

#### Learning Objectives

Students will be able to:

* Distinguish syntax, runtime, and logic errors.
* Interpret Python tracebacks.
* Use debugging techniques.
* Handle expected errors with exceptions.
* Write basic automated tests.

#### Instructional Topics

**Lesson 1: Understanding Errors**

* Syntax errors
* Runtime errors
* Logic errors
* Reading tracebacks
* Locating the source of a failure

**Exercise**

Students diagnose and repair several intentionally broken programs.

**Lesson 2: Exception Handling**

* `try`
* `except`
* `else`
* `finally`
* Raising exceptions
* Handling only expected failures

**Exercise**

Students safely process values that may be missing, malformed, or invalid.

**Lesson 3: Testing**

* Why software is tested
* Test cases
* Expected and actual results
* Assertions
* Unit tests
* Normal, boundary, and failure cases

**Exercise**

Students write tests for validation and transformation functions.

#### Applied Challenge

Students receive a malfunctioning data-processing program and must debug it, correct it, and demonstrate its behavior with tests.

## Day 5: Files, Modules, and Structured Data

### Morning Session: Reading and Writing Files

#### Learning Objectives

Students will be able to:

* Open and close files safely.
* Read and write text files.
* Work with file paths programmatically.
* Read and write CSV and JSON data.
* Understand text encoding at a basic level.

#### Instructional Topics

**Lesson 1: Text Files and Paths**

* File paths
* The `pathlib` module
* Read, write, and append modes
* Context managers
* Newline behavior

**Exercise**

Students read a text file, count lines and words, and write a summary file.

**Lesson 2: CSV Files**

* Rows and columns
* Headers
* Delimiters
* Reading CSV records
* Writing CSV output
* Common CSV problems

**Exercise**

Students load a CSV file, validate its columns, and produce a filtered CSV file.

**Lesson 3: JSON Files**

* JSON objects and arrays
* Python-to-JSON type relationships
* Nested structures
* Serialization and deserialization

**Exercise**

Students load a configuration file and write processed results to JSON.

#### Applied Challenge

Students convert a CSV dataset into a cleaned JSON dataset while recording rejected rows separately.

---

### Afternoon Session: Modules and Program Organization

#### Learning Objectives

Students will be able to:

* Import Python modules.
* Use selected standard-library modules.
* Create a reusable Python module.
* Separate configuration, processing, and output logic.
* Recognize package dependencies.

#### Instructional Topics

**Lesson 1: Imports and the Standard Library**

* Modules
* Packages
* `import`
* `from ... import`
* Aliases
* Standard-library examples

**Exercise**

Students use standard-library modules for dates, statistics, paths, and structured data.

**Lesson 2: Creating Modules**

* Separating code across files
* Reusable functions
* Entry points
* The `__name__` check
* Avoiding duplicated code

**Exercise**

Students move validation functions into a separate module and import them into a main program.

**Lesson 3: Dependencies and Environments**

* Third-party packages
* Package installation
* Virtual environments
* Dependency versions
* Reproducibility
* Requirements files

**Exercise**

Students inspect and document the dependencies of a small project.

#### Applied Challenge

Students reorganize a single-file program into a small project containing modules, tests, data folders, and documentation.

## Day 6: Tabular Data and Relational Thinking

### Morning Session: Data Analysis with Python

#### Learning Objectives

Students will be able to:

* Load tabular data into a dataframe.
* Inspect rows, columns, and data types.
* Select and filter data.
* Create calculated columns.
* Identify missing and inconsistent values.

#### Instructional Topics

**Lesson 1: Dataframes**

* Rows, columns, and indexes
* Series and dataframes
* Loading CSV data
* Viewing samples
* Shape and column information

**Exercise**

Students load and inspect an unfamiliar dataset.

**Lesson 2: Selecting and Filtering**

* Selecting columns
* Filtering rows
* Boolean masks
* Sorting
* Renaming columns
* Creating calculated columns

**Exercise**

Students filter a dataset according to several business rules and calculate new fields.

**Lesson 3: Cleaning Data**

* Missing values
* Duplicate rows
* Incorrect data types
* String normalization
* Numeric conversion
* Date conversion

**Exercise**

Students clean an intentionally inconsistent dataset.

#### Applied Challenge

Students produce a clean dataframe and a data-quality report describing every correction or rejection.

---

### Afternoon Session: Aggregation, Joins, and SQL Concepts

#### Learning Objectives

Students will be able to:

* Group and aggregate data.
* Combine related datasets.
* Explain primary and foreign keys.
* Describe common join types.
* Write basic SQL queries.

#### Instructional Topics

**Lesson 1: Grouping and Aggregation**

* Grouping records
* Counts
* Sums
* Means
* Minimums and maximums
* Multi-column grouping

**Exercise**

Students produce summary metrics by category, date, or organization.

**Lesson 2: Relationships and Joins**

* Tables and records
* Primary keys
* Foreign keys
* One-to-one and one-to-many relationships
* Inner and left joins
* Unmatched records

**Exercise**

Students join transaction data to reference data and investigate unmatched records.

**Lesson 3: SQL Foundations**

* `SELECT`
* `FROM`
* `WHERE`
* `ORDER BY`
* `GROUP BY`
* Aggregate functions
* SQL compared with dataframe operations

**Exercise**

Students answer the same data questions using both SQL and Python.

#### Applied Challenge

Students combine two datasets, calculate grouped metrics, and verify the results using a SQL query.

## Day 7: Data Transformations and Production-Style Workflows

### Morning Session: Building Reliable Data Transformations

#### Learning Objectives

Students will be able to:

* Separate data inputs, transformations, and outputs.
* Create deterministic transformations.
* Explain idempotency.
* Validate input and output schemas.
* Design a multi-stage data workflow.

#### Instructional Topics

**Lesson 1: Transformation Architecture**

* Source data
* Intermediate data
* Curated data
* Input-process-output models
* Transformation functions
* Separation of concerns

**Exercise**

Students divide an existing script into ingestion, cleaning, transformation, and publishing stages.

**Lesson 2: Reproducibility and Idempotency**

* Deterministic behavior
* Repeatable runs
* Avoiding hidden state
* Stable identifiers
* Duplicate prevention
* Safe reruns

**Exercise**

Students modify a process so running it twice produces the same correct result.

**Lesson 3: Schemas and Data Contracts**

* Required columns
* Data types
* Nullability
* Uniqueness
* Allowed values
* Input and output contracts

**Exercise**

Students implement schema checks and reject nonconforming input.

#### Applied Challenge

Students build a three-stage transformation that converts raw records into a validated, curated output dataset.

---

### Afternoon Session: Dependencies and Data Pipelines

#### Learning Objectives

Students will be able to:

* Model a workflow as a directed graph.
* Identify upstream and downstream dependencies.
* Explain how changes propagate through a pipeline.
* Design small, maintainable transformation steps.
* Distinguish batch processing from interactive analysis.

#### Instructional Topics

**Lesson 1: Dependency Graphs**

* Nodes and edges
* Directed acyclic graphs
* Upstream and downstream data
* Dependency order
* Circular dependency problems

**Exercise**

Students draw a dependency graph for a multi-step data workflow.

**Lesson 2: Pipeline Design**

* Small versus large transformations
* Reusable stages
* Intermediate outputs
* Naming conventions
* Failure isolation
* Incremental development

**Exercise**

Students redesign a monolithic script as several connected transformation steps.

**Lesson 3: Observability**

* Logging
* Record counts
* Rejected-record counts
* Timing information
* Warning and error messages
* Basic operational metrics

**Exercise**

Students add structured logging and processing metrics to a data pipeline.

#### Applied Challenge

Students execute a multi-stage workflow, intentionally introduce a failure, identify the affected downstream steps, and repair the pipeline.

## Day 8: Collaborative Development and Integrated Data Applications

### Morning Session: Version Control and Team Development

#### Learning Objectives

Students will be able to:

* Explain the purpose of version control.
* Create commits with meaningful messages.
* Compare versions of a file.
* Work with branches at a basic level.
* Review and discuss code changes.

#### Instructional Topics

**Lesson 1: Version-Control Concepts**

* Repositories
* Tracked and untracked files
* Commits
* History
* Reverting changes
* Meaningful commit messages

**Exercise**

Students initialize a repository, make changes, and create a sequence of commits.

**Lesson 2: Branches and Merging**

* Main development line
* Feature branches
* Merging
* Merge conflicts
* Conflict resolution

**Exercise**

Students make changes on a branch and merge them into the main branch.

**Lesson 3: Code Review and Collaboration**

* Reviewing changes
* Readability
* Naming
* Documentation
* Testing expectations
* Giving constructive feedback

**Exercise**

Students review a partner’s Python function using a structured checklist.

#### Applied Challenge

Students correct, test, document, and commit improvements to a small shared project.

---

### Afternoon Session: End-to-End Guided Project

#### Learning Objectives

Students will be able to:

* Apply the complete development workflow.
* Translate requirements into technical tasks.
* Build a multi-stage data-processing application.
* Verify output quality.
* Prepare a project for another developer to review.

#### Guided Project Scenario

Students receive:

* A raw operational dataset
* A reference dataset
* Written business rules
* Several intentional data-quality problems
* Required output metrics
* A target output schema

#### Project Stages

**Lesson and Exercise Cycle 1: Requirements and Design**

* Identify required inputs and outputs.
* Write pseudocode.
* Draw the dependency graph.
* Define validation rules.
* Divide the work into functions and modules.

**Lesson and Exercise Cycle 2: Implementation**

* Load source data.
* Normalize column names and values.
* Convert data types.
* Reject invalid records.
* Join related datasets.
* Calculate derived fields.

**Lesson and Exercise Cycle 3: Verification and Publication**

* Calculate aggregate metrics.
* Validate the output schema.
* Add logging.
* Write output files.
* Add tests and documentation.

#### Applied Challenge

Students complete the guided project and conduct a structured peer review.

#### Capstone Preparation

During the final 30 minutes, students:

* Review the capstone requirements.
* Examine the available datasets.
* Select a capstone problem.
* Identify the initial project scope.
* Form teams when team projects are permitted.

## Day 9: Capstone Design and Development

### Morning Session: Capstone Planning and Advanced Practices

#### Learning Objectives

Students will be able to:

* Translate an open-ended problem into a technical design.
* Select appropriate data structures and transformations.
* Define measurable acceptance criteria.
* Plan testing and validation.
* Begin implementing a maintainable solution.

#### Instructional Topics

**Lesson 1: Capstone Architecture**

* Problem definition
* User or stakeholder needs
* Inputs and outputs
* Pipeline stages
* Dependency diagrams
* Project scope control

**Exercise**

Students create a one-page capstone design containing:

* Problem statement
* Source datasets
* Required transformations
* Output dataset or report
* Dependency diagram
* Initial task list

**Lesson 2: Data Quality and Acceptance Criteria**

* Required fields
* Valid ranges
* Duplicate handling
* Missing-value strategy
* Expected row counts
* Output validation

**Exercise**

Students define at least five data-quality checks and five functional acceptance criteria.

**Lesson 3: Performance and Maintainability**

* Avoiding unnecessary loops
* Vectorized dataframe operations
* Reusing intermediate results
* Function size and responsibility
* Documentation
* Reasonable optimization

**Exercise**

Students review their design for potential performance and maintenance problems.

#### Capstone Kickoff

During the final portion of the morning, students:

* Create the project repository.
* Create the folder structure.
* Add a README outline.
* Load and inspect the source data.
* Commit the initial project structure.

---

### Afternoon Session: Capstone Development

The entire afternoon session is dedicated to capstone development.

#### Recommended Schedule

| Time      | Activity                                 |
| --------- | ---------------------------------------- |
| 0:00–0:15 | Team planning and task assignment        |
| 0:15–1:15 | Development sprint 1                     |
| 1:15–1:30 | Break                                    |
| 1:30–2:30 | Development sprint 2                     |
| 2:30–2:45 | Instructor checkpoint                    |
| 2:45–3:30 | Development sprint 3                     |
| 3:30–4:00 | Testing, commit, and daily status review |

#### Instructor Role

The instructor circulates among students and conducts short technical reviews focused on:

* Scope
* Program structure
* Data-quality rules
* Correct use of functions
* Appropriate use of dataframe operations
* Error handling
* Testing
* Documentation
* Version-control progress

#### End-of-Day Milestone

By the end of Day 9, each capstone should have:

* A working ingestion stage
* A mostly complete cleaning stage
* At least one completed transformation
* Initial validation checks
* A defined output structure
* At least three meaningful commits
* A list of remaining tasks

## Day 10: Capstone Completion and Presentation

### Morning Session: Capstone Completion

The entire morning session is dedicated to completing and preparing the capstone.

#### Recommended Schedule

| Time      | Activity                               |
| --------- | -------------------------------------- |
| 0:00–0:15 | Status review and task prioritization  |
| 0:15–1:15 | Final development sprint               |
| 1:15–1:30 | Break                                  |
| 1:30–2:15 | Testing and data validation            |
| 2:15–2:30 | Break                                  |
| 2:30–3:15 | Documentation and code cleanup         |
| 3:15–4:00 | Presentation preparation and rehearsal |

#### Required Completion Activities

Students must:

* Complete all required transformations.
* Remove or clearly identify unfinished experimental code.
* Verify output accuracy.
* Run all automated tests.
* Validate the final output schema.
* Review logs and processing metrics.
* Update the README.
* Prepare a dependency diagram.
* Prepare a short presentation.
* Commit the final version.

---

### Afternoon Session: Capstone Presentations

#### Presentation Format

Each student or team receives approximately 12–15 minutes:

* 8–10 minutes for the presentation and demonstration
* 3–5 minutes for questions

Presentation length may be adjusted based on class size.

#### Presentation Requirements

Each presentation must explain:

1. The problem being solved
2. The intended user or stakeholder
3. The source data
4. Major data-quality problems discovered
5. The transformation workflow
6. The dependency graph
7. Important Python design decisions
8. Validation and testing methods
9. Final outputs
10. Lessons learned
11. Potential future improvements

#### Demonstration Requirements

Students should demonstrate:

* The project structure
* One or more important Python functions
* The transformation process
* Data-quality checks
* Final output data
* Logs or processing metrics
* Test results

#### Final Course Reflection

The course concludes with a discussion of:

* Common mistakes made during the course
* Strategies for reading unfamiliar code
* How to continue practicing Python
* How to ask effective technical questions
* How to work safely in shared production environments
* The difference between exploratory work and production work

# Capstone Project

## Capstone Objective

Students will create a Python-based data project that ingests raw data, validates and transforms it, combines related information, calculates useful results, and produces a documented output.

The project should resemble a small production data workflow rather than a single-use classroom script.

## Suggested Capstone Scenarios

Students may select from scenarios such as:

* Equipment readiness reporting
* Maintenance history analysis
* Training completion monitoring
* Inventory reconciliation
* Financial transaction analysis
* Customer or service-request analysis
* Personnel qualification tracking
* Project milestone reporting
* Logistics and shipment analysis
* Sensor or event-log analysis

## Minimum Technical Requirements

The capstone must:

1. Read at least two source datasets.
2. Use CSV, JSON, or another approved structured format.
3. Validate required columns.
4. Convert at least two columns to appropriate data types.
5. Address missing or invalid values.
6. Detect or handle duplicate records.
7. Join or otherwise relate multiple datasets.
8. Create at least three derived fields.
9. Perform at least one grouped aggregation.
10. Produce a curated output dataset.
11. Produce a summary report or metrics table.
12. Use functions to organize major processing steps.
13. Include exception handling.
14. Include logging or processing-status messages.
15. Include at least five automated tests or assertions.
16. Include a README.
17. Include a dependency diagram.
18. Use version control with meaningful commits.

## Recommended Project Structure

```text
capstone_project/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── reference/
│   └── output/
├── src/
│   ├── ingest.py
│   ├── validate.py
│   ├── transform.py
│   ├── metrics.py
│   └── main.py
├── tests/
│   └── test_transformations.py
└── documentation/
    └── pipeline_diagram.png
```

# Assessment Strategy

## Recommended Grade Distribution

| Assessment Area                      | Percentage |
| ------------------------------------ | ---------: |
| Daily exercises and knowledge checks |        20% |
| Programming challenges               |        20% |
| Guided end-to-end project            |        15% |
| Capstone technical implementation    |        25% |
| Capstone testing and documentation   |        10% |
| Capstone presentation                |        10% |

## Capstone Evaluation Rubric

### Technical Correctness — 30%

* The program runs successfully.
* Required transformations are accurate.
* Outputs satisfy the stated requirements.
* Joins and aggregations produce correct results.

### Code Quality — 20%

* Functions have clear responsibilities.
* Variables and functions have meaningful names.
* Code is organized into logical modules.
* Unnecessary duplication is avoided.
* Comments and docstrings are useful.

### Data Quality — 15%

* Inputs are validated.
* Missing values are handled intentionally.
* Duplicates are addressed.
* Invalid records are reported or rejected.
* Output schemas are checked.

### Testing and Reliability — 15%

* Important functions have tests.
* Normal and failure cases are considered.
* Errors are handled appropriately.
* The process can be rerun safely.
* Logs or processing metrics are available.

### Documentation — 10%

* The README explains the project.
* Setup and execution steps are included.
* Inputs and outputs are described.
* The dependency diagram is understandable.
* Assumptions and limitations are documented.

### Presentation — 10%

* The problem and solution are clearly explained.
* The demonstration is organized.
* Technical decisions are justified.
* Questions are answered accurately.
* All team members participate when applicable.

# Daily Knowledge Checks

Each standard session should conclude with a brief knowledge check. Possible formats include:

* Five-question quiz
* Code tracing exercise
* Error diagnosis
* Explain-a-concept prompt
* One-function programming task
* Peer code review
* Exit ticket describing the most important concept learned

Knowledge checks should emphasize understanding rather than memorization.

# Instructional Approach

## Use a Gradual Progression

The course should move through four levels of support:

1. Instructor demonstration
2. Guided exercise
3. Partially completed exercise
4. Independent challenge

Students should not be expected to create complete programs from an empty file during the first several days.

## Use Consistent Example Domains

Exercises should use a small number of familiar domains such as:

* Employees
* Equipment
* Projects
* Inventory
* Transactions
* Training records
* Maintenance records

Using consistent domains reduces cognitive load and allows students to concentrate on programming concepts.

## Teach Error Messages Explicitly

Students should regularly practice:

* Reading the final line of a traceback
* Finding the referenced line number
* Identifying the exception type
* Inspecting relevant variable values
* Creating the smallest reproducible example
* Testing one correction at a time

## Transition from Notebooks to Structured Projects

Recommended progression:

* Days 1–3: Primarily interactive notebooks
* Day 4: Notebooks and small scripts
* Day 5: Scripts and modules
* Days 6–7: Dataframes and multi-stage projects
* Day 8: Repository-based integrated project
* Days 9–10: Capstone repository

## Reinforce Production Habits

Throughout the course, students should be reminded to:

* Preserve raw source data.
* Avoid manually changing source files.
* Use code to make repeatable changes.
* Validate inputs before processing.
* Keep credentials and sensitive values out of source code.
* Use meaningful names.
* Commit small, working changes.
* Test assumptions.
* Document important decisions.

# Required Software and Materials

Recommended instructional environment:

* Modern web browser
* Python 3
* Notebook environment
* Python code editor
* Terminal or command prompt
* Git client
* Dataframe library
* Lightweight SQL database
* CSV and JSON sample datasets
* Diagramming tool
* Shared course repository or file location

## Recommended Python Libraries

The course should remain focused and avoid introducing unnecessary packages. A suitable core set is:

* Python standard library
* `pathlib`
* `csv`
* `json`
* `datetime`
* `logging`
* `statistics`
* `pandas`
* `pytest`

# Scope Expectations

Ten days is sufficient to create functional entry-level Python and data-workflow proficiency, but not independent mastery.

Successful graduates should be able to:

* Understand and modify existing Python transformations.
* Build small transformations from clear requirements.
* Investigate common failures.
* Work with tabular datasets.
* Follow an established project structure.
* Use tests, logs, documentation, and version control.
* Ask informed questions when working on larger production systems.

Graduates will still require mentoring for complex architecture, large-scale optimization, security-sensitive development, advanced data modeling, and production incident response.
