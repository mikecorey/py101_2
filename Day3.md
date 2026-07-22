# Day 3: Collections, Loops, and Processing Multiple Records

## Day 3 Purpose

During Days 1 and 2, students worked primarily with individual values and individual records.

Day 3 introduces the idea of working with groups of values and repeating operations across those groups.

This is a major transition in programming.

Students move from thinking:

```text
I have one value.
I evaluate one condition.
I produce one result.
```

to thinking:

```text
I have many values.
I need to process each one.
I may need to keep, reject, count, summarize, or transform them.
```

This is the foundation of real data processing.

Students will learn how to:

* Store multiple values in collections
* Choose appropriate Python collection types
* Retrieve and modify collection contents
* Represent structured records
* Process multiple records using loops
* Count, total, filter, and classify data
* Track intermediate results
* Use `break` and `continue`
* Write basic list comprehensions
* Build a small multi-record processing workflow

The primary mental model for Day 3 is:

```text
Collection of data
       ↓
Take one item
       ↓
Evaluate or transform it
       ↓
Store or summarize the result
       ↓
Repeat for remaining items
```

---

# Morning Session: Collections and Structured Data

## Morning Learning Objectives

By the end of the morning session, students will be able to:

1. Explain why collections are needed.
2. Create and modify Python lists.
3. Retrieve list elements using indexes.
4. Use slicing with lists.
5. Explain the difference between mutable and immutable data at a basic level.
6. Create and use tuples.
7. Create and use dictionaries.
8. Represent a structured record using a dictionary.
9. Use dictionary keys to retrieve and update values.
10. Use sets to represent unique values.
11. Choose an appropriate collection type for a problem.
12. Create collections containing other collections.

---

## Block 1: Lists and Ordered Collections

### Instruction: 30 Minutes

#### Topics

* Why collections are needed
* Individual variables versus grouped values
* Lists
* Ordered data
* Creating lists
* List indexes
* Zero-based indexing
* Negative indexing
* List slicing
* List length
* Updating list values
* Adding values
* Removing values
* Membership testing
* Empty lists
* Lists containing mixed types
* Why consistent data types are usually easier to work with
* Mutable data

#### Why Collections Matter

Until now, students may have written code like:

```python
score_1 = 78
score_2 = 84
score_3 = 91
score_4 = 88
```

This becomes difficult as the number of values increases.

A list allows related values to be grouped:

```python
scores = [78, 84, 91, 88]
```

The variable `scores` refers to a single list containing several values.

#### Ordered Collections

A list preserves the order of its items.

```python
departments = [
    "engineering",
    "operations",
    "finance",
    "logistics"
]
```

Each value has an index.

```text
Value: engineering  operations  finance  logistics
Index:      0           1          2         3
```

#### Accessing Items

```python
departments = ["engineering", "operations", "finance", "logistics"]

print(departments[0])
print(departments[2])
print(departments[-1])
```

#### List Length

```python
record_ids = ["EQ-101", "EQ-102", "EQ-103"]

print(len(record_ids))
```

The result is:

```text
3
```

#### Slicing

Lists use the same basic slicing pattern students saw with strings.

```python
values = [10, 20, 30, 40, 50]

first_three = values[0:3]
middle_values = values[1:4]
```

The ending index is not included.

#### Modifying a List

Lists are mutable.

```python
statuses = ["active", "inactive", "active"]

statuses[1] = "active"
```

The existing list has been changed.

#### Adding Items

```python
record_ids = ["EQ-101", "EQ-102"]

record_ids.append("EQ-103")
```

#### Inserting Items

```python
record_ids.insert(1, "EQ-101A")
```

#### Removing Items

```python
record_ids.remove("EQ-101A")
```

Or remove by position:

```python
removed_record = record_ids.pop()
```

#### Membership Testing

```python
supported_extensions = ["csv", "json", "txt"]

is_supported = "csv" in supported_extensions
```

This is cleaner than writing:

```python
is_supported = (
    extension == "csv"
    or extension == "json"
    or extension == "txt"
)
```

This connects directly to the validation work from Day 2.

#### Empty Lists

```python
errors = []
```

An empty list is useful when the program will collect values later.

For example:

```python
validation_errors = []

if record_id == "":
    validation_errors.append("Record ID is missing")
```

This is an important pattern students will use later.

### Guided Exercise: 30 Minutes

Students create several lists.

#### Exercise 1: Measurements

```python
temperatures = [72.5, 75.1, 81.2, 68.9, 77.0]
```

Students:

* Print the first value
* Print the last value
* Print the number of values
* Change one temperature
* Add another temperature
* Remove one temperature

#### Exercise 2: Supported File Types

```python
supported_types = ["csv", "json", "parquet"]
```

Students test whether:

* `"csv"` is supported
* `"txt"` is supported
* `"PARQUET"` is supported before and after normalization

#### Exercise 3: Validation Errors

Students begin with:

```python
validation_errors = []
```

They check several values:

```python
record_id = ""
file_size = 0
error_count = -2
```

Each problem adds a message to the list.

Example:

```python
if record_id.strip() == "":
    validation_errors.append("Record ID is missing")

if file_size <= 0:
    validation_errors.append("File size must be greater than zero")

if error_count < 0:
    validation_errors.append("Error count cannot be negative")
```

Students print:

* The error list
* The number of errors
* The first error

#### Exercise 4: Slicing

Given:

```python
record_ids = [
    "EQ-1001",
    "EQ-1002",
    "EQ-1003",
    "EQ-1004",
    "EQ-1005",
]
```

Students extract:

* First two records
* Last two records
* Middle three records

### Block 1 Applied Challenge

Students create a small list-based data-quality tracker.

The program contains:

```python
record_ids = [
    "EQ-1001",
    "",
    "EQ-1003",
    "BAD-1004",
]
```

Without loops yet, students manually inspect several positions and build:

```python
invalid_records = []
```

They add invalid values to the list and print:

* Number of records examined
* Number of invalid records
* Invalid record values

The purpose is to establish the collection model before automating the process with loops in the afternoon.

---

## Block 2: Tuples and Immutable Collections

### Instruction: 30 Minutes

#### Topics

* Tuples
* Ordered collections
* Tuple syntax
* Indexing
* Slicing
* Tuple unpacking
* Immutability
* Lists versus tuples
* Fixed groups of related values
* Returning multiple values conceptually
* Coordinates and structured pairs

#### Creating a Tuple

```python
location = (30.4, -86.9)
```

A tuple is similar to a list because:

* It is ordered.
* It supports indexing.
* It supports slicing.

But tuples cannot be modified after creation.

#### Accessing Values

```python
location = (30.4, -86.9)

latitude = location[0]
longitude = location[1]
```

#### Tuple Unpacking

```python
latitude, longitude = location
```

This places the first tuple value into `latitude` and the second into `longitude`.

#### Another Example

```python
dimensions = (1920, 1080)

width, height = dimensions
```

#### Immutability

This fails:

```python
dimensions[0] = 1280
```

because the tuple cannot be modified in place.

#### Why Use a Tuple?

A tuple is useful when:

* The number of values is fixed.
* Their order has a specific meaning.
* The values should not normally change.

Examples include:

* Coordinates
* Width and height
* Minimum and maximum values
* RGB color components
* Database result rows in some environments

#### Lists Versus Tuples

| Feature           | List                | Tuple          |
| ----------------- | ------------------- | -------------- |
| Ordered           | Yes                 | Yes            |
| Indexed           | Yes                 | Yes            |
| Can change        | Yes                 | No             |
| Add/remove values | Yes                 | No             |
| Common use        | Changing collection | Fixed grouping |

The instructor should avoid overemphasizing performance differences at this stage.

The practical distinction is enough:

> A list generally represents a collection that may change. A tuple generally represents a fixed grouping.

### Guided Exercise: 30 Minutes

#### Exercise 1: Geographic Coordinates

```python
location = (30.4213, -86.6170)
```

Students:

* Print latitude
* Print longitude
* Unpack the tuple
* Print a formatted coordinate

#### Exercise 2: Allowed Range

```python
temperature_range = (60, 80)
```

Students unpack:

```python
minimum_temperature, maximum_temperature = temperature_range
```

Then evaluate:

```python
temperature = 72

is_valid = (
    minimum_temperature
    <= temperature
    <= maximum_temperature
)
```

#### Exercise 3: Screen Resolution

```python
resolution = (1920, 1080)
```

Students calculate:

* Width
* Height
* Total number of pixels

#### Exercise 4: Compare List and Tuple Behavior

Students create:

```python
list_values = [10, 20, 30]
tuple_values = (10, 20, 30)
```

They attempt to change the first element of each and observe the difference.

### Block 2 Applied Challenge

Students represent several fixed configuration values using tuples:

```python
acceptable_temperature = (60, 80)
acceptable_voltage = (110, 125)
acceptable_completion = (0, 100)
```

Students unpack each pair and use the values in validation expressions.

The purpose is to show how related configuration values can be grouped and reused.

---

## Block 3: Dictionaries and Structured Records

### Instruction: 30 Minutes

#### Topics

* Dictionaries
* Keys and values
* Key-value relationships
* Creating dictionaries
* Retrieving values
* Updating values
* Adding keys
* Removing keys
* Checking for keys
* Dictionary length
* Dictionary methods
* Structured records
* Why dictionaries are useful for real-world data
* Comparing dictionaries to rows in a table
* Nested data structures

#### Why Dictionaries Matter

Lists are useful when values are primarily identified by position.

A dictionary is useful when values should be identified by meaningful names.

Instead of:

```python
record = ["EQ-1045", "active", 850, True]
```

students can write:

```python
record = {
    "record_id": "EQ-1045",
    "status": "active",
    "operating_hours": 850,
    "inspection_complete": True,
}
```

The second representation is much easier to understand.

#### Accessing Values

```python
print(record["record_id"])
print(record["status"])
```

#### Updating Values

```python
record["status"] = "inactive"
```

#### Adding a New Key

```python
record["error_count"] = 0
```

#### Dictionary Keys

Keys are commonly strings:

```python
record["record_id"]
record["status"]
record["error_count"]
```

They provide labels for the values.

#### Checking Whether a Key Exists

```python
has_status = "status" in record
```

#### Using `.get()`

```python
error_count = record.get("error_count")
```

A default can also be provided:

```python
error_count = record.get("error_count", 0)
```

The instructor should explain the difference carefully.

This:

```python
record["missing_key"]
```

may cause an error.

This:

```python
record.get("missing_key")
```

returns `None` if the key does not exist.

#### Dictionary Methods

Useful introductory methods include:

```python
record.keys()
record.values()
record.items()
```

Students do not yet need to master these, but they will use them during loops.

#### Dictionaries as Records

A dictionary maps naturally to a structured record:

```python
employee = {
    "employee_id": "EMP-203",
    "name": "Jordan Smith",
    "department": "engineering",
    "active": True,
}
```

This resembles:

* A row in a spreadsheet
* A JSON object
* A database record
* A structured message received from an API

This connection is important for later course material.

#### Nested Structures

A dictionary can contain another dictionary:

```python
record = {
    "record_id": "EQ-1045",
    "status": "active",
    "metrics": {
        "temperature": 72.5,
        "operating_hours": 850,
    },
}
```

Access:

```python
temperature = record["metrics"]["temperature"]
```

Students only need a basic introduction to nesting at this point.

### Guided Exercise: 30 Minutes

Students create a dictionary representing an equipment record.

```python
equipment = {
    "equipment_id": "EQ-1045",
    "status": "active",
    "operating_hours": 850,
    "maximum_hours": 1000,
    "inspection_complete": True,
    "temperature": 72.5,
}
```

Students:

1. Print the equipment ID.
2. Print the current status.
3. Update operating hours.
4. Add an error count.
5. Add a readiness field.
6. Determine whether the equipment is ready.
7. Store the result back in the dictionary.

Example:

```python
equipment["is_ready"] = (
    equipment["status"] == "active"
    and equipment["inspection_complete"]
    and equipment["operating_hours"]
        <= equipment["maximum_hours"]
)
```

#### Exercise 2: Project Record

Students create:

```python
project = {
    "project_id": "PRJ-2401",
    "name": "Network Modernization",
    "completed_tasks": 18,
    "total_tasks": 24,
    "approved": True,
}
```

They calculate completion percentage and add it:

```python
project["completion_percentage"] = (
    project["completed_tasks"]
    / project["total_tasks"]
    * 100
)
```

#### Exercise 3: Missing Keys

Students use:

```python
project.get("budget")
```

and compare that behavior with:

```python
project["budget"]
```

The instructor demonstrates the resulting error from the second form if the key does not exist.

### Block 3 Applied Challenge

Students convert a collection of individually named variables into a dictionary.

Starting values:

```python
record_id = "INGEST-2401"
file_name = "equipment.csv"
file_size_mb = 18.5
record_count = 12450
error_count = 2
approved = True
```

Students create:

```python
record = {
    ...
}
```

They then add:

* Supported file type
* Has errors
* Ready for processing
* Human-readable status

This prepares students for working with multiple dictionary records later in the day.

---

## Block 4: Sets and Choosing the Right Collection

### Instruction: 30 Minutes

#### Topics

* Sets
* Unique values
* Creating sets
* Duplicate removal
* Membership testing
* Adding values
* Removing values
* Set operations
* Intersection
* Union
* Difference
* Lists versus tuples versus dictionaries versus sets
* Choosing collections based on intent
* Combining collection types

#### What Is a Set?

A set represents a collection of unique values.

```python
departments = {
    "engineering",
    "operations",
    "finance",
}
```

Duplicate values are automatically collapsed.

```python
values = {"active", "active", "inactive"}
```

The resulting set contains only:

```text
active
inactive
```

#### Membership Testing

Sets are especially useful for checking whether a value belongs to a defined group.

```python
allowed_statuses = {
    "active",
    "inactive",
    "retired",
}

if status in allowed_statuses:
    print("Valid status")
```

This is considerably cleaner than:

```python
if (
    status == "active"
    or status == "inactive"
    or status == "retired"
):
    print("Valid status")
```

#### Adding Values

```python
allowed_statuses.add("maintenance")
```

#### Removing Values

```python
allowed_statuses.remove("retired")
```

#### Duplicate Removal

```python
record_ids = [
    "EQ-1001",
    "EQ-1002",
    "EQ-1001",
    "EQ-1003",
]

unique_ids = set(record_ids)
```

#### Set Intersection

Values appearing in both sets:

```python
required_skills = {
    "python",
    "sql",
    "git",
}

employee_skills = {
    "python",
    "excel",
    "sql",
}

matching_skills = required_skills & employee_skills
```

#### Set Difference

Required values not present:

```python
missing_skills = required_skills - employee_skills
```

#### Set Union

All unique values from both:

```python
all_skills = required_skills | employee_skills
```

#### Choosing a Collection

The instructor should emphasize intent.

Use a:

**List** when:

* Order matters
* Duplicate values may matter
* Values may be added or removed

**Tuple** when:

* Order matters
* The grouping is fixed
* Values should not change

**Dictionary** when:

* Values have meaningful names
* A structured record is needed
* Data contains fields

**Set** when:

* Values should be unique
* Membership testing is important
* Set comparisons are useful

#### Combining Collections

Real programs commonly combine them.

Example:

```python
records = [
    {
        "record_id": "EQ-1001",
        "status": "active",
    },
    {
        "record_id": "EQ-1002",
        "status": "inactive",
    },
]
```

This is:

```text
List
 ├── Dictionary
 └── Dictionary
```

This pattern will become extremely important.

It represents a collection of structured records.

### Guided Exercise: 30 Minutes

#### Exercise 1: Allowed Status Values

```python
allowed_statuses = {
    "active",
    "inactive",
    "retired",
}
```

Students test several values.

#### Exercise 2: Detect Duplicates

```python
record_ids = [
    "EQ-1001",
    "EQ-1002",
    "EQ-1003",
    "EQ-1002",
    "EQ-1004",
]
```

Students compare:

```python
len(record_ids)
```

with:

```python
len(set(record_ids))
```

If the values differ, duplicates exist.

#### Exercise 3: Compare Requirements

```python
required_fields = {
    "record_id",
    "status",
    "file_name",
    "record_count",
}

available_fields = {
    "record_id",
    "status",
    "file_name",
}
```

Students calculate:

```python
missing_fields = required_fields - available_fields
```

#### Exercise 4: Select the Collection

For each scenario, students select:

* List
* Tuple
* Dictionary
* Set

Scenarios include:

* Daily temperature measurements
* Latitude and longitude
* Employee record
* Allowed status codes
* Ordered processing steps
* Unique department names
* RGB color components
* Validation error messages

### Morning Applied Challenge: Build a Structured Dataset

Students create a list containing at least four dictionaries.

Example:

```python
records = [
    {
        "record_id": "EQ-1001",
        "status": "active",
        "error_count": 0,
    },
    {
        "record_id": "EQ-1002",
        "status": "active",
        "error_count": 3,
    },
    {
        "record_id": "EQ-1003",
        "status": "inactive",
        "error_count": 0,
    },
    {
        "record_id": "EQ-1004",
        "status": "active",
        "error_count": 7,
    },
]
```

Students should be able to explain:

* Why the outer structure is a list
* Why each record is a dictionary
* How to access the first record
* How to retrieve a field from the first record
* How to modify one field
* How to determine the number of records

Example:

```python
first_record = records[0]

print(first_record["record_id"])
```

This dataset becomes the conceptual bridge into the afternoon.

---

# Afternoon Session: Loops and Repeated Processing

## Afternoon Learning Objectives

By the end of the afternoon session, students will be able to:

1. Explain why loops are needed.
2. Use `for` loops to process sequences.
3. Use `range()` to repeat operations.
4. Use counters and accumulators.
5. Process lists of values.
6. Process lists of dictionaries.
7. Use `enumerate()` for indexes and values.
8. Use dictionary iteration.
9. Filter records with conditional logic.
10. Use `continue` and `break`.
11. Explain basic `while` loops.
12. Recognize infinite loops.
13. Use basic list comprehensions.
14. Build a complete multi-record processing workflow.

---

## Block 1: Repetition with `for` Loops

### Instruction: 30 Minutes

#### Topics

* Repetition in programs
* Manual repetition versus loops
* `for` loops
* Loop variables
* Iterables
* Processing one item at a time
* Indentation
* Execution order
* `range()`
* Counters
* Accumulators
* Running totals
* Calculating counts
* Finding minimum and maximum conceptually

#### Why Loops Matter

Without loops:

```python
print(records[0])
print(records[1])
print(records[2])
print(records[3])
```

This does not scale.

With a loop:

```python
for record in records:
    print(record)
```

The same logic works whether the list contains:

* 4 records
* 400 records
* 4 million records

The loop expresses:

> Perform this operation for each item in the collection.

#### Basic `for` Loop

```python
temperatures = [72, 75, 81, 69]

for temperature in temperatures:
    print(temperature)
```

#### Mental Model

```text
Take first value
      ↓
Run loop body
      ↓
Take next value
      ↓
Run loop body
      ↓
Continue until no values remain
```

#### Loop Variables

```python
for temperature in temperatures:
```

`temperature` temporarily refers to the current item.

On each iteration, it changes.

#### Indentation

```python
for temperature in temperatures:
    print(temperature)
    print("Processed")

print("All temperatures processed")
```

The final statement runs only after the loop finishes.

#### Using `range()`

```python
for number in range(5):
    print(number)
```

Produces:

```text
0
1
2
3
4
```

Students should recognize that the ending value is excluded.

#### Different Ranges

```python
range(1, 5)
range(0, 10, 2)
```

Conceptually:

```python
for number in range(1, 5):
    print(number)
```

produces:

```text
1
2
3
4
```

#### Counters

```python
count = 0

for record in records:
    count = count + 1
```

Or:

```python
count += 1
```

#### Accumulators

```python
values = [10, 20, 30]

total = 0

for value in values:
    total += value
```

At the end:

```text
total = 60
```

#### Calculating an Average

```python
values = [10, 20, 30]

total = 0

for value in values:
    total += value

average = total / len(values)
```

The instructor should mention built-in functions like `sum()` exist, but manually building the accumulator is useful for understanding the pattern.

### Guided Exercise: 30 Minutes

#### Exercise 1: Print Every Value

```python
scores = [82, 91, 77, 88, 95]
```

Students print each score.

#### Exercise 2: Count Values

Students count the number of records manually using a counter.

#### Exercise 3: Calculate a Total

```python
file_sizes = [12.5, 8.2, 4.7, 31.0]
```

Students calculate total storage.

#### Exercise 4: Calculate Average

Students calculate average file size.

#### Exercise 5: Count Passing Scores

```python
scores = [82, 61, 74, 95, 55, 88]
```

Students count scores of at least 70.

Example:

```python
passing_count = 0

for score in scores:
    if score >= 70:
        passing_count += 1
```

#### Exercise 6: Count Errors

```python
error_counts = [0, 2, 0, 5, 1, 0]
```

Students calculate:

* Number of records
* Number with errors
* Total number of errors

### Block 1 Applied Challenge

Students process a list of completion percentages:

```python
completion_values = [100, 82, 97, 45, 100, 68, 91]
```

They calculate:

* Total number of records
* Number complete
* Number incomplete
* Number at least 90% complete
* Sum of all percentages
* Average completion percentage

Students should use:

* At least one counter
* At least one accumulator
* At least one conditional inside the loop

---

## Block 2: Processing Structured Records

### Instruction: 30 Minutes

#### Topics

* Lists of dictionaries
* Processing records one at a time
* Retrieving fields inside a loop
* Conditional logic inside loops
* Updating dictionary values
* Building summary counts
* Collecting matching records
* Collecting rejected records
* `enumerate()`
* Iterating through dictionary keys and values

#### Lists of Dictionaries

A realistic dataset may look like:

```python
records = [
    {
        "record_id": "EQ-1001",
        "status": "active",
        "error_count": 0,
    },
    {
        "record_id": "EQ-1002",
        "status": "active",
        "error_count": 2,
    },
    {
        "record_id": "EQ-1003",
        "status": "inactive",
        "error_count": 0,
    },
]
```

The program processes each dictionary:

```python
for record in records:
    print(record["record_id"])
```

#### Accessing Fields

```python
for record in records:
    record_id = record["record_id"]
    status = record["status"]
    error_count = record["error_count"]

    print(record_id, status, error_count)
```

#### Applying Conditions

```python
for record in records:
    if record["error_count"] == 0:
        print(f'{record["record_id"]}: clean')
    else:
        print(f'{record["record_id"]}: has errors')
```

#### Updating Records

```python
for record in records:
    if record["error_count"] == 0:
        record["quality_status"] = "valid"
    else:
        record["quality_status"] = "review"
```

After the loop, every dictionary contains the new field.

#### Collecting Matching Records

```python
valid_records = []

for record in records:
    if record["error_count"] == 0:
        valid_records.append(record)
```

This is a core data-processing pattern:

```text
Input collection
      ↓
Evaluate each record
      ↓
Keep records that meet requirements
      ↓
Output collection
```

#### Collecting Rejected Records

```python
rejected_records = []

for record in records:
    if record["error_count"] > 5:
        rejected_records.append(record)
```

#### Using `enumerate()`

Sometimes both the position and the value are useful.

```python
for index, record in enumerate(records):
    print(index, record["record_id"])
```

Starting at 1 can improve human-readable output:

```python
for number, record in enumerate(records, start=1):
    print(f"{number}. {record['record_id']}")
```

#### Iterating Through a Dictionary

```python
record = {
    "record_id": "EQ-1001",
    "status": "active",
    "error_count": 0,
}
```

Keys:

```python
for key in record:
    print(key)
```

Key and value:

```python
for key, value in record.items():
    print(key, value)
```

This is useful when the fields themselves need to be inspected dynamically.

### Guided Exercise: 30 Minutes

Students begin with:

```python
records = [
    {
        "record_id": "EQ-1001",
        "status": "active",
        "error_count": 0,
        "completion": 100,
    },
    {
        "record_id": "EQ-1002",
        "status": "active",
        "error_count": 2,
        "completion": 95,
    },
    {
        "record_id": "EQ-1003",
        "status": "inactive",
        "error_count": 0,
        "completion": 100,
    },
    {
        "record_id": "EQ-1004",
        "status": "active",
        "error_count": 8,
        "completion": 76,
    },
]
```

Students calculate:

* Number of records
* Number active
* Number inactive
* Number with errors
* Total errors
* Number complete
* Number requiring review

Students then add:

```python
record["processing_status"]
```

Possible values:

* `ready`
* `warning`
* `rejected`

Example:

```python
for record in records:
    if record["status"] != "active":
        record["processing_status"] = "rejected"
    elif record["error_count"] > 5:
        record["processing_status"] = "rejected"
    elif record["error_count"] > 0:
        record["processing_status"] = "warning"
    elif record["completion"] < 100:
        record["processing_status"] = "warning"
    else:
        record["processing_status"] = "ready"
```

Students print a formatted report.

### Block 2 Applied Challenge

Students create three output collections:

```python
ready_records = []
warning_records = []
rejected_records = []
```

The program processes each record and places it into exactly one collection.

At the end, students display:

* Total input records
* Ready count
* Warning count
* Rejected count
* Percentage ready
* IDs of rejected records

This pattern directly prepares students for later data pipeline processing.

---

## Block 3: Controlling Loops with `continue`, `break`, and `while`

### Instruction: 30 Minutes

#### Topics

* Normal loop execution
* Skipping an iteration
* `continue`
* Ending a loop early
* `break`
* When early termination is useful
* `while` loops
* Condition-controlled repetition
* Counters with `while`
* Sentinel values
* Infinite loops
* Safe loop conditions
* Choosing `for` versus `while`

#### `continue`

`continue` skips the remainder of the current iteration and moves to the next item.

Example:

```python
records = [
    {"record_id": "EQ-1001", "active": True},
    {"record_id": "EQ-1002", "active": False},
    {"record_id": "EQ-1003", "active": True},
]

for record in records:
    if not record["active"]:
        continue

    print(f'Processing {record["record_id"]}')
```

Inactive records are skipped.

This is useful when invalid records should not continue into later calculations.

#### Validation Pattern

```python
for record in records:
    if record["record_id"] == "":
        print("Skipping record with missing ID")
        continue

    print(f'Processing {record["record_id"]}')
```

This reinforces defensive programming from Day 2.

#### `break`

`break` stops the loop completely.

```python
for record in records:
    if record["error_count"] > 100:
        print("Critical error threshold reached")
        break
```

Possible uses include:

* Stop after finding the desired record
* Stop after detecting a critical condition
* Stop interactive input when the user chooses to exit

#### Searching

```python
search_id = "EQ-1003"

for record in records:
    if record["record_id"] == search_id:
        print("Record found")
        break
```

Without `break`, the loop continues even after finding the desired record.

#### `while` Loops

A `while` loop repeats as long as its condition is true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

#### Mental Model

```text
Check condition
      ↓
True? → Run loop body
      ↓
Update state
      ↓
Check again
```

When the condition becomes false, the loop ends.

#### Infinite Loops

This is dangerous:

```python
count = 1

while count <= 5:
    print(count)
```

`count` never changes, so the condition remains true forever.

The instructor should emphasize:

> A `while` loop usually needs something in its body that moves the program toward the stopping condition.

#### Sentinel-Controlled Input

```python
command = ""

while command != "quit":
    command = input("Enter command: ").strip().lower()

    if command != "quit":
        print(f"You entered: {command}")
```

#### `for` Versus `while`

Use `for` when:

* You have a collection.
* You know what items should be processed.
* You want to process each item.

Use `while` when:

* Repetition depends on a condition.
* You do not necessarily know the number of repetitions in advance.

### Guided Exercise: 30 Minutes

#### Exercise 1: Skip Invalid Records

Given several records, students use `continue` to skip records with:

* Missing ID
* Negative record count
* Inactive status

#### Exercise 2: Search for a Record

Students search a list for:

```python
target_id = "EQ-1004"
```

When found, print the record and stop.

#### Exercise 3: Critical Error Stop

Process records until a record has:

```python
critical_error = True
```

Then stop processing.

#### Exercise 4: Basic `while`

Students create a countdown:

```python
count = 5

while count > 0:
    print(count)
    count -= 1
```

#### Exercise 5: User-Controlled Loop

Students repeatedly ask for a filename until the user enters:

```text
quit
```

### Block 3 Applied Challenge

Students build a simulated processing queue.

```python
records = [
    {
        "record_id": "EQ-1001",
        "status": "active",
        "critical_error": False,
    },
    {
        "record_id": "",
        "status": "active",
        "critical_error": False,
    },
    {
        "record_id": "EQ-1003",
        "status": "inactive",
        "critical_error": False,
    },
    {
        "record_id": "EQ-1004",
        "status": "active",
        "critical_error": True,
    },
    {
        "record_id": "EQ-1005",
        "status": "active",
        "critical_error": False,
    },
]
```

Rules:

* Missing IDs are skipped.
* Inactive records are skipped.
* Valid active records are processed.
* A critical error immediately stops the entire process.

Students should predict which records are processed before running the code.

---

## Block 4: List Comprehensions and Multi-Record Processing Patterns

### Instruction: 30 Minutes

#### Topics

* Transforming collections
* Filtering collections
* Creating a new list from an existing list
* Traditional loop pattern
* List comprehensions
* Basic syntax
* Comprehensions with conditions
* When comprehensions improve readability
* When traditional loops are clearer
* Separating source and output collections
* Data-processing pipeline pattern
* Input, validation, transformation, output

#### Traditional Transformation Loop

```python
numbers = [1, 2, 3, 4]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

The result is:

```python
[1, 4, 9, 16]
```

#### Equivalent List Comprehension

```python
squares = [
    number ** 2
    for number in numbers
]
```

Or in one line:

```python
squares = [number ** 2 for number in numbers]
```

Students should understand the long-form loop first.

The comprehension is simply a more compact way to express a common pattern.

#### Filtering

Traditional:

```python
scores = [82, 61, 74, 95, 55, 88]

passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)
```

Comprehension:

```python
passing_scores = [
    score
    for score in scores
    if score >= 70
]
```

#### Transform and Filter

```python
temperatures = [72, 51, 81, 68]

normal_temperatures = [
    temperature
    for temperature in temperatures
    if 60 <= temperature <= 80
]
```

#### Extracting Fields from Records

```python
record_ids = [
    record["record_id"]
    for record in records
]
```

#### Filtering Dictionaries

```python
active_records = [
    record
    for record in records
    if record["status"] == "active"
]
```

#### When Not to Use a Comprehension

This is possible but hard to read:

```python
results = [
    complicated_transformation(record)
    for record in records
    if first_condition(record)
    and second_condition(record)
    and third_condition(record)
]
```

For beginners, complex logic should remain in a normal loop.

The rule should be:

> Use comprehensions when the operation remains immediately understandable.

#### Multi-Record Processing Pattern

Students should begin seeing data processing as stages.

```text
Raw records
    ↓
Validate
    ↓
Reject unusable records
    ↓
Transform valid records
    ↓
Collect results
    ↓
Calculate summary metrics
```

Example:

```python
clean_records = []
rejected_records = []

for record in records:
    if record["record_id"] == "":
        rejected_records.append(record)
        continue

    cleaned_record = {
        "record_id": record["record_id"].strip().upper(),
        "status": record["status"].strip().lower(),
    }

    clean_records.append(cleaned_record)
```

This pattern will appear repeatedly throughout the rest of the course.

### Guided Exercise: 30 Minutes

#### Exercise 1: Squares

Create squares from:

```python
numbers = [1, 2, 3, 4, 5]
```

using:

* Traditional loop
* List comprehension

#### Exercise 2: Filter Scores

Extract only passing scores.

#### Exercise 3: Normalize Status Values

Starting with:

```python
statuses = [
    " ACTIVE ",
    "inactive",
    "Active",
    " RETIRED ",
]
```

Create:

```python
normalized_statuses
```

using a comprehension.

#### Exercise 4: Extract Record IDs

From a list of dictionaries, create a list containing only record IDs.

#### Exercise 5: Active Record IDs

Create a list containing the IDs of only active records.

Example:

```python
active_record_ids = [
    record["record_id"]
    for record in records
    if record["status"] == "active"
]
```

### Block 4 Applied Challenge: Build a Small Transformation Pipeline

Students receive:

```python
raw_records = [
    {
        "record_id": " eq-1001 ",
        "status": " ACTIVE ",
        "error_count": 0,
        "completion": 100,
    },
    {
        "record_id": "",
        "status": "active",
        "error_count": 0,
        "completion": 85,
    },
    {
        "record_id": "EQ-1003",
        "status": " INACTIVE ",
        "error_count": 0,
        "completion": 100,
    },
    {
        "record_id": "eq-1004",
        "status": "active",
        "error_count": 4,
        "completion": 95,
    },
]
```

Students must:

1. Process every record.
2. Normalize record IDs.
3. Normalize status values.
4. Reject records with missing IDs.
5. Reject inactive records.
6. Assign warnings when error count is greater than zero.
7. Assign warnings when completion is below 100%.
8. Store cleaned records in a new collection.
9. Store rejected records separately.
10. Calculate summary statistics.

Possible output structures:

```python
clean_records = []
rejected_records = []
```

Each cleaned record should include:

```python
{
    "record_id": "...",
    "status": "...",
    "error_count": ...,
    "completion": ...,
    "processing_status": "...",
}
```

---

# Day 3 End-of-Day Integrated Challenge

## Multi-Record Intake Processor

Students build their first complete program that processes a small dataset rather than a single record.

### Input Dataset

```python
records = [
    {
        "record_id": " INGEST-2401 ",
        "source": "Maintenance",
        "file_name": "equipment.csv",
        "record_count": 12450,
        "completion": 100,
        "error_count": 0,
    },
    {
        "record_id": "INGEST-2402",
        "source": "LOGISTICS",
        "file_name": "shipments.JSON",
        "record_count": 8300,
        "completion": 98,
        "error_count": 2,
    },
    {
        "record_id": "",
        "source": "Finance",
        "file_name": "transactions.csv",
        "record_count": 4000,
        "completion": 100,
        "error_count": 0,
    },
    {
        "record_id": "INGEST-2404",
        "source": "Unknown",
        "file_name": "notes.txt",
        "record_count": 0,
        "completion": 70,
        "error_count": 9,
    },
]
```

### Allowed Values

```python
allowed_sources = {
    "maintenance",
    "logistics",
    "finance",
}

supported_extensions = {
    "csv",
    "json",
}
```

### Required Processing

For every record:

1. Strip whitespace from the record ID.
2. Normalize source to lowercase.
3. Normalize the filename.
4. Determine whether the record ID exists.
5. Determine whether the source is recognized.
6. Determine whether the file type is supported.
7. Verify record count is greater than zero.
8. Verify completion is between 0 and 100.
9. Verify error count is not negative.
10. Assign:

    * `ready`
    * `warning`
    * `rejected`
11. Add an explanatory message.
12. Store the record in the appropriate output collection.

### Output Collections

```python
ready_records = []
warning_records = []
rejected_records = []
```

### Summary Requirements

Students calculate and display:

* Total records received
* Number ready
* Number warning
* Number rejected
* Percentage ready
* Total record count across usable records
* Total errors
* Unique source systems
* IDs of rejected records

### Example Summary

```text
Data Intake Processing Summary
------------------------------
Records received: 4
Ready: 1
Warnings: 1
Rejected: 2

Ready percentage: 25.0%
Usable source records: 20,750
Total reported errors: 11

Unique sources:
maintenance
logistics
finance
unknown

Rejected record IDs:
<MISSING>
INGEST-2404
```

### Extension Challenge

Students create:

```python
problem_record_ids
```

using a list comprehension containing the IDs of all warning and rejected records.

---

# Day 3 Common Errors to Address

## Index Out of Range

Incorrect:

```python
values = [10, 20, 30]

print(values[3])
```

Valid indexes are:

```text
0
1
2
```

Students should understand:

> A list containing three items does not have index 3.

---

## Confusing an Index with a Value

```python
scores = [75, 82, 91]
```

This:

```python
scores[1]
```

means:

```text
the item at index 1
```

not:

```text
the score whose value is 1
```

---

## Forgetting That Lists Are Mutable

```python
statuses = ["active", "inactive"]

statuses[1] = "active"
```

This changes the existing list.

Students should recognize that modifications may affect later code using the same object.

---

## Confusing Dictionary Keys and Values

Given:

```python
record = {
    "status": "active"
}
```

Correct:

```python
record["status"]
```

Incorrect:

```python
record["active"]
```

`"status"` is the key.

`"active"` is the value.

---

## Accessing a Missing Dictionary Key

```python
record["error_count"]
```

may fail if the key is absent.

Use a validation check or:

```python
record.get("error_count")
```

when appropriate.

---

## Forgetting the Loop Indentation

Incorrect:

```python
for score in scores:
print(score)
```

Correct:

```python
for score in scores:
    print(score)
```

---

## Accidentally Putting Code Outside the Loop

```python
total = 0

for value in values:
    print(value)

total += value
```

Only the final value is added.

Correct:

```python
total = 0

for value in values:
    print(value)
    total += value
```

---

## Resetting a Counter Inside the Loop

Incorrect:

```python
for score in scores:
    passing_count = 0

    if score >= 70:
        passing_count += 1
```

The counter resets during every iteration.

Correct:

```python
passing_count = 0

for score in scores:
    if score >= 70:
        passing_count += 1
```

---

## Modifying a Collection While Iterating

The instructor should briefly warn students against patterns such as:

```python
for value in values:
    if value < 0:
        values.remove(value)
```

Changing the collection while iterating through it can lead to unexpected behavior.

A safer beginner pattern is to create a new collection:

```python
valid_values = []

for value in values:
    if value >= 0:
        valid_values.append(value)
```

---

## Infinite `while` Loop

Incorrect:

```python
count = 0

while count < 10:
    print(count)
```

Correct:

```python
count = 0

while count < 10:
    print(count)
    count += 1
```

---

## Using `break` Instead of `continue`

Students should distinguish:

```python
continue
```

means:

```text
skip this item and continue processing
```

while:

```python
break
```

means:

```text
stop processing the entire loop
```

---

# Day 3 Instructor Demonstration Strategy

The instructor should gradually increase the amount of data being processed.

## Step 1: One Value

```python
temperature = 72
```

## Step 2: Several Values

```python
temperatures = [72, 75, 81, 69]
```

## Step 3: Process Each Value

```python
for temperature in temperatures:
    print(temperature)
```

## Step 4: Add Conditional Logic

```python
for temperature in temperatures:
    if 60 <= temperature <= 80:
        print("Normal")
    else:
        print("Outside expected range")
```

## Step 5: Represent Structured Records

```python
record = {
    "record_id": "EQ-1001",
    "temperature": 72,
}
```

## Step 6: Create Multiple Records

```python
records = [
    {
        "record_id": "EQ-1001",
        "temperature": 72,
    },
    {
        "record_id": "EQ-1002",
        "temperature": 85,
    },
]
```

## Step 7: Process the Dataset

```python
for record in records:
    if 60 <= record["temperature"] <= 80:
        record["status"] = "normal"
    else:
        record["status"] = "warning"
```

This progression helps students understand that a dataset is not fundamentally mysterious.

At this stage, it can be understood as:

```text
A collection of structured records
```

---

# Day 3 Knowledge Check

Students should be able to answer or demonstrate the following:

1. What problem does a list solve?
2. What does zero-based indexing mean?
3. What is the difference between a list and a tuple?
4. Why would a dictionary be used for a record?
5. What is a dictionary key?
6. What is a dictionary value?
7. What does `.get()` do?
8. When would a set be useful?
9. How can a set help identify duplicates?
10. What does a `for` loop do?
11. What is a loop variable?
12. What is an accumulator?
13. What is a counter?
14. What does `continue` do?
15. What does `break` do?
16. When would a `while` loop be more appropriate than a `for` loop?
17. Why can a `while` loop become infinite?
18. What is a list comprehension?
19. Why might a normal loop be preferable to a complicated comprehension?
20. How would you represent multiple structured records in Python?

---

# Day 3 End-of-Day Outcomes

By the end of Day 3, students should be able to move beyond programs that process only one record.

They should be comfortable with:

* Lists
* Tuples
* Dictionaries
* Sets
* Nested collections
* Lists of dictionaries
* `for` loops
* `while` loops
* Counters
* Accumulators
* Filtering
* Record classification
* `break`
* `continue`
* Basic list comprehensions

Students should now understand a basic data-processing model:

```text
Collection of raw records
          ↓
Loop through records
          ↓
Validate each record
          ↓
Normalize or transform values
          ↓
Classify the record
          ↓
Store results
          ↓
Calculate summary information
```

This prepares students for Day 4, where they will begin extracting repeated logic into functions, designing reusable components, debugging larger programs, and introducing automated testing.
