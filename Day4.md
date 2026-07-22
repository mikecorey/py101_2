# Day 4: Functions, Program Design, Debugging, and Testing

## Day 4 Purpose

During Days 1–3, students learned how to:

* Represent information in Python
* Perform calculations
* Make decisions
* Store collections of data
* Process multiple records with loops

At this point, students can write useful programs, but those programs will naturally begin becoming long, repetitive, and difficult to understand.

Day 4 introduces the tools programmers use to control that complexity.

Students move from:

```text
One long script
      ↓
Lots of variables
      ↓
Repeated logic
      ↓
Difficult debugging
```

toward:

```text
Program
  ↓
Small functions
  ↓
Clear inputs and outputs
  ↓
Reusable processing steps
  ↓
Independently testable pieces
```

The day also introduces a critical professional programming skill:

> Code should not merely work. We should have a systematic way to demonstrate that it works.

Students will learn how to:

* Define and call functions
* Pass data into functions
* Return results
* Separate calculations from output
* Understand variable scope
* Design small functions with clear responsibilities
* Document functions
* Use basic type hints
* Read Python tracebacks
* Diagnose syntax, runtime, and logic errors
* Handle expected failures with exceptions
* Use assertions
* Write basic automated tests
* Refactor the Day 3 record-processing workflow into reusable components

---

# Morning Session: Functions and Program Design

## Morning Learning Objectives

By the end of the morning session, students will be able to:

1. Explain why functions are useful.
2. Define and call Python functions.
3. Distinguish parameters from arguments.
4. Return values from functions.
5. Explain the difference between `print()` and `return`.
6. Write functions that accept multiple inputs.
7. Use default and keyword arguments.
8. Explain local and global scope at a practical level.
9. Avoid unnecessary global variables.
10. Decompose a larger problem into smaller functions.
11. Write functions with a single clear responsibility.
12. Add docstrings and basic type hints.
13. Combine several functions into a processing workflow.

---

## Block 1: Creating and Calling Functions

### Instruction: 30 Minutes

#### Topics

* What a function is
* Why functions exist
* Repeated code
* Function definitions
* Function calls
* Parameters
* Arguments
* Function bodies
* Indentation
* Execution flow
* Returning to the calling code
* Functions with no parameters
* Functions with one or more parameters

### Why Functions Matter

Consider code that performs the same calculation several times:

```python
completed_tasks = 18
total_tasks = 24

percentage = completed_tasks / total_tasks * 100

print(f"{percentage:.1f}%")
```

Later:

```python
completed_tasks = 42
total_tasks = 50

percentage = completed_tasks / total_tasks * 100

print(f"{percentage:.1f}%")
```

Later again:

```python
completed_tasks = 87
total_tasks = 100

percentage = completed_tasks / total_tasks * 100

print(f"{percentage:.1f}%")
```

The calculation has been repeated.

If the calculation changes, every copy must be found and changed.

A function allows the logic to be defined once.

```python
def calculate_percentage(completed, total):
    percentage = completed / total * 100
    return percentage
```

It can then be reused:

```python
result_1 = calculate_percentage(18, 24)
result_2 = calculate_percentage(42, 50)
result_3 = calculate_percentage(87, 100)
```

### Anatomy of a Function

```python
def calculate_percentage(completed, total):
    percentage = completed / total * 100
    return percentage
```

Students identify:

```text
def
    ↓
Defines a function

calculate_percentage
    ↓
Function name

completed, total
    ↓
Parameters

:
    ↓
Begins function body

Indented statements
    ↓
Code belonging to function

return
    ↓
Sends a result back to caller
```

### Calling a Function

Defining a function does not automatically execute it.

```python
def say_hello():
    print("Hello")
```

Nothing is printed until:

```python
say_hello()
```

This distinction is important:

```text
Definition = describe what the function does

Call = actually execute the function
```

### Parameters and Arguments

In:

```python
def calculate_total(price, quantity):
    return price * quantity
```

`price` and `quantity` are parameters.

When calling:

```python
total = calculate_total(12.50, 8)
```

`12.50` and `8` are arguments.

A useful beginner explanation:

> Parameters are the names in the function definition. Arguments are the actual values supplied when calling the function.

### Execution Flow

Students should understand that execution temporarily moves into the function.

```text
Main program
     ↓
Call function
     ↓
Execute function body
     ↓
Return result
     ↓
Continue main program
```

Example:

```python
print("Starting")

def double_value(value):
    result = value * 2
    return result

answer = double_value(5)

print(answer)
print("Finished")
```

Conceptual execution:

```text
Starting
   ↓
Call double_value(5)
   ↓
value becomes 5
   ↓
result becomes 10
   ↓
return 10
   ↓
answer becomes 10
   ↓
print answer
   ↓
Finished
```

### Guided Exercise: 30 Minutes

Students convert calculations from earlier days into functions.

#### Exercise 1: Convert Megabytes to Gigabytes

```python
def megabytes_to_gigabytes(megabytes):
    gigabytes = megabytes / 1000
    return gigabytes
```

Test:

```python
result = megabytes_to_gigabytes(2500)

print(result)
```

#### Exercise 2: Calculate Completion Percentage

Students create:

```python
def calculate_completion(completed, total):
    return completed / total * 100
```

Test with several values.

#### Exercise 3: Determine Whether a Temperature Is Valid

```python
def is_temperature_valid(temperature):
    return 60 <= temperature <= 80
```

Students should notice that a function can return a Boolean value.

#### Exercise 4: Normalize a Status

```python
def normalize_status(status):
    return status.strip().lower()
```

Test:

```python
print(normalize_status(" ACTIVE "))
print(normalize_status("Inactive"))
print(normalize_status(" retired "))
```

#### Exercise 5: File Type Validation

Students create:

```python
def is_supported_file(file_name):
    file_name = file_name.strip().lower()

    return (
        file_name.endswith(".csv")
        or file_name.endswith(".json")
    )
```

### Block 1 Applied Challenge

Students revisit several calculations from Days 2 and 3 and identify repeated operations that could become functions.

They create at least four functions:

```python
normalize_record_id(...)
calculate_percentage(...)
is_supported_file(...)
is_valid_record_count(...)
```

Students test each function independently.

---

## Block 2: `return`, Multiple Inputs, and Function Behavior

### Instruction: 30 Minutes

#### Topics

* `return`
* `print()` versus `return`
* Returning strings
* Returning numbers
* Returning Boolean values
* Returning collections
* Returning dictionaries
* Multiple return values
* Early returns
* Default arguments
* Keyword arguments
* Designing predictable functions

### `print()` Versus `return`

This distinction is extremely important.

Consider:

```python
def calculate_total(price, quantity):
    print(price * quantity)
```

Calling:

```python
result = calculate_total(10, 5)
```

prints:

```text
50
```

but `result` contains:

```python
None
```

The function displayed a value but did not return one.

Correct:

```python
def calculate_total(price, quantity):
    return price * quantity
```

Now:

```python
result = calculate_total(10, 5)
```

stores:

```text
50
```

in `result`.

### Mental Model

`print()` means:

```text
Show something to the user.
```

`return` means:

```text
Give something back to the code that called me.
```

A returned value can then be:

* Stored
* Compared
* Printed
* Passed to another function
* Added to a collection
* Used in another calculation

### Returning Boolean Values

Avoid unnecessary code like:

```python
def is_valid_score(score):
    if 0 <= score <= 100:
        return True
    else:
        return False
```

Prefer:

```python
def is_valid_score(score):
    return 0 <= score <= 100
```

Both are correct, but the second expresses the idea more directly.

### Returning Collections

Functions can return lists:

```python
def get_invalid_values(values):
    invalid_values = []

    for value in values:
        if value < 0:
            invalid_values.append(value)

    return invalid_values
```

Functions can return dictionaries:

```python
def create_summary(total, errors):
    return {
        "total_records": total,
        "error_count": errors,
    }
```

### Multiple Return Values

Python can return multiple values:

```python
def get_minimum_and_maximum(values):
    minimum = min(values)
    maximum = max(values)

    return minimum, maximum
```

Call:

```python
minimum, maximum = get_minimum_and_maximum(values)
```

Students should recognize the connection to tuples from Day 3.

Conceptually, Python is returning:

```python
(minimum, maximum)
```

### Early Returns

A function can return before reaching its end.

```python
def calculate_percentage(completed, total):

    if total <= 0:
        return None

    return completed / total * 100
```

This prevents invalid division.

Another example:

```python
def validate_record_id(record_id):

    record_id = record_id.strip()

    if record_id == "":
        return False

    if not record_id.startswith("EQ-"):
        return False

    return True
```

This pattern can make validation functions easier to understand.

### Default Arguments

```python
def calculate_processing_time(
    record_count,
    rate=250
):
    return record_count / rate
```

Call using default:

```python
time = calculate_processing_time(10000)
```

Or provide another value:

```python
time = calculate_processing_time(10000, 500)
```

### Keyword Arguments

```python
time = calculate_processing_time(
    record_count=10000,
    rate=500
)
```

Keyword arguments can improve readability when several values are involved.

### Guided Exercise: 30 Minutes

#### Exercise 1: `print()` or `return`?

Students receive several functions and determine whether they should print or return their result.

#### Exercise 2: Validation Function

Create:

```python
def validate_completion(completion):
```

Rules:

* Must be at least 0
* Must be no greater than 100

Return a Boolean.

#### Exercise 3: Classification Function

Create:

```python
def classify_error_count(error_count):
```

Return:

* `"valid"` for 0
* `"warning"` for 1–5
* `"rejected"` for greater than 5

#### Exercise 4: Create a Summary Dictionary

Create:

```python
def create_record_summary(
    record_id,
    status,
    error_count
):
```

Return:

```python
{
    "record_id": ...,
    "status": ...,
    "error_count": ...
}
```

#### Exercise 5: Multiple Results

Create:

```python
def calculate_statistics(values):
```

Return:

* Minimum
* Maximum
* Average

Students unpack the returned values.

### Block 2 Applied Challenge

Students create:

```python
def validate_record(record):
```

The function receives a dictionary representing one record.

It returns two values:

```python
status, message
```

Example:

```python
status, message = validate_record(record)
```

Possible results:

```text
"ready", "Record passed validation"

"warning", "Record contains minor errors"

"rejected", "Record ID is missing"
```

Students then use the function with several dictionaries from Day 3.

---

## Block 3: Scope, Side Effects, and Function Design

### Instruction: 30 Minutes

#### Topics

* Variable scope
* Local variables
* Global variables
* Parameter scope
* Variable lifetime
* Functions modifying collections
* Side effects
* Pure functions
* Single responsibility
* Function size
* Naming functions
* Avoiding hidden dependencies
* Separating calculations from display

### Local Variables

Variables created inside a function normally exist only inside that function.

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total
```

`total` is local to the function.

Trying:

```python
print(total)
```

outside the function produces an error.

### Parameters Are Local Names

```python
def double_value(number):
    result = number * 2
    return result
```

`number` exists as a local name while the function executes.

### Global Variables

A variable created outside a function is generally called a global variable.

```python
tax_rate = 0.07
```

A function can read it:

```python
def calculate_tax(price):
    return price * tax_rate
```

But this introduces a hidden dependency.

The function appears to need only:

```python
price
```

but it secretly also depends on:

```python
tax_rate
```

A clearer design is:

```python
def calculate_tax(price, tax_rate):
    return price * tax_rate
```

Now all required information is explicit.

### Why Excessive Globals Cause Problems

Global state can make programs:

* Harder to understand
* Harder to test
* Harder to reuse
* More sensitive to execution order
* Easier to accidentally modify

Students do not need to treat global variables as universally forbidden.

The practical rule is:

> Prefer passing required information into functions rather than making functions depend on unrelated variables elsewhere in the program.

### Side Effects

Consider:

```python
def normalize_record(record):
    record["status"] = record["status"].strip().lower()
```

This modifies the original dictionary.

That is a side effect.

Sometimes this is intentional.

But students should recognize the difference between:

```python
def normalize_status(status):
    return status.strip().lower()
```

and a function that modifies an external object.

### Pure Functions

A simplified beginner definition:

> A pure function calculates its result from its inputs without changing unrelated program state.

Example:

```python
def calculate_percentage(completed, total):
    return completed / total * 100
```

Given the same inputs, it produces the same result.

These functions are usually easier to:

* Understand
* Reuse
* Test
* Debug

### Single Responsibility

Poor function:

```python
def process_everything(record):
```

This might:

* Validate the record
* Normalize strings
* Calculate percentages
* Print messages
* Save results
* Update counters

Instead, separate responsibilities:

```python
normalize_record(...)
validate_record(...)
calculate_metrics(...)
classify_record(...)
format_record_summary(...)
```

### Function Names

Prefer verbs describing the action:

```python
calculate_percentage()
normalize_status()
validate_record()
classify_record()
create_summary()
```

Avoid vague names:

```python
do_it()
handle_data()
process_stuff()
thing()
```

### Separating Calculation from Display

Less reusable:

```python
def calculate_percentage(completed, total):
    percentage = completed / total * 100
    print(f"{percentage:.1f}%")
```

More reusable:

```python
def calculate_percentage(completed, total):
    return completed / total * 100
```

Then:

```python
percentage = calculate_percentage(18, 24)

print(f"{percentage:.1f}%")
```

Now the calculation can be used without requiring output.

### Guided Exercise: 30 Minutes

Students receive a deliberately poorly organized program.

Example:

```python
tax_rate = 0.07

price = 50
quantity = 4

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(total)

price = 25
quantity = 7

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(total)
```

Students refactor it into:

```python
def calculate_subtotal(price, quantity):
    return price * quantity


def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate


def calculate_total(subtotal, tax):
    return subtotal + tax
```

Students then apply the same approach to record-processing logic.

### Block 3 Applied Challenge

Students receive a Day 3-style loop containing:

* Normalization
* Validation
* Classification
* Calculations
* Output formatting

all inside one large loop.

They identify pieces that could become functions.

Target structure:

```python
for record in records:

    cleaned_record = normalize_record(record)

    status, message = validate_record(cleaned_record)

    metrics = calculate_metrics(cleaned_record)

    print_record_summary(
        cleaned_record,
        status,
        message,
        metrics
    )
```

Students do not necessarily need to implement every function yet.

The important exercise is learning to identify responsibilities.

---

## Block 4: Documentation, Type Hints, and Composing Functions

### Instruction: 30 Minutes

#### Topics

* Function contracts
* Inputs
* Outputs
* Preconditions
* Docstrings
* Type hints
* Reading function signatures
* Function composition
* Calling one function from another
* Building processing stages
* Main-program structure

### Function Contracts

A useful function should have an understandable contract.

For example:

```python
def calculate_percentage(completed, total):
```

The contract might be:

```text
Input:
    completed: number of completed records
    total: total number of records

Requirement:
    total must be greater than zero

Output:
    completion percentage as a float
```

Students should begin asking:

* What does this function expect?
* What does it return?
* What values are invalid?
* Does it modify anything?

### Docstrings

```python
def calculate_percentage(completed, total):
    """Calculate the percentage of completed items."""
    return completed / total * 100
```

A more informative docstring:

```python
def calculate_percentage(completed, total):
    """
    Calculate completion percentage.

    The total value must be greater than zero.
    """
    return completed / total * 100
```

Students do not need to memorize a particular documentation standard yet.

The objective is simply:

> Important functions should explain their purpose and assumptions.

### Type Hints

```python
def calculate_percentage(
    completed: int,
    total: int
) -> float:

    return completed / total * 100
```

Students should understand:

```text
completed: int
```

means the function expects an integer.

```text
-> float
```

means the function is expected to return a floating-point value.

Type hints do not automatically prevent Python from receiving another type.

They communicate intent to:

* Developers
* Editors
* Static analysis tools
* Documentation systems

### Boolean Function

```python
def is_supported_file(file_name: str) -> bool:
    """Return True when the file type is supported."""

    normalized_name = file_name.strip().lower()

    return (
        normalized_name.endswith(".csv")
        or normalized_name.endswith(".json")
    )
```

### Calling Functions from Functions

```python
def normalize_status(status: str) -> str:
    return status.strip().lower()


def is_active(status: str) -> bool:
    normalized_status = normalize_status(status)

    return normalized_status == "active"
```

One function can build on another.

This creates layers of abstraction.

### Function Composition

Conceptually:

```text
Raw value
   ↓
normalize_status()
   ↓
Normalized value
   ↓
is_active()
   ↓
Boolean result
```

For record processing:

```text
Raw record
    ↓
normalize_record()
    ↓
validate_record()
    ↓
calculate_metrics()
    ↓
classify_record()
    ↓
create_output_record()
```

This begins resembling a data transformation pipeline.

### Main Program

Students should begin separating function definitions from the main execution logic.

Example:

```python
def normalize_status(status: str) -> str:
    return status.strip().lower()


def is_valid_status(status: str) -> bool:
    allowed_statuses = {
        "active",
        "inactive",
        "retired",
    }

    return status in allowed_statuses


status = " ACTIVE "

clean_status = normalize_status(status)
valid_status = is_valid_status(clean_status)

print(clean_status)
print(valid_status)
```

The top portion defines capabilities.

The bottom portion uses them.

### Guided Exercise: 30 Minutes

Students add docstrings and type hints to functions created earlier.

Functions include:

```python
normalize_record_id()
normalize_status()
calculate_percentage()
is_supported_file()
classify_error_count()
```

Students then create:

```python
def process_record(record: dict) -> dict:
```

which calls several smaller functions.

Example structure:

```python
def process_record(record: dict) -> dict:

    record_id = normalize_record_id(
        record["record_id"]
    )

    status = normalize_status(
        record["status"]
    )

    processing_status = classify_error_count(
        record["error_count"]
    )

    return {
        "record_id": record_id,
        "status": status,
        "processing_status": processing_status,
    }
```

### Morning Applied Challenge: Refactor the Day 3 Processor

Students take the Day 3 multi-record processor and reorganize it using functions.

Minimum required functions:

```python
normalize_record()
validate_record()
classify_record()
process_record()
```

Main processing loop:

```python
processed_records = []

for record in records:

    processed_record = process_record(record)

    processed_records.append(processed_record)
```

By lunch, students should have transformed a long procedural program into a collection of smaller reusable components.

---

# Afternoon Session: Debugging, Exceptions, and Testing

## Afternoon Learning Objectives

By the end of the afternoon session, students will be able to:

1. Distinguish syntax errors, runtime errors, and logic errors.
2. Read a Python traceback.
3. Identify the exception type and failing line.
4. Use systematic debugging techniques.
5. Inspect intermediate values.
6. Create small reproducible tests.
7. Handle expected errors with `try` and `except`.
8. Explain why broad exception handling can be dangerous.
9. Raise exceptions intentionally.
10. Use assertions.
11. Write simple automated tests.
12. Test normal, boundary, and invalid cases.
13. Refactor code to make it easier to test.

---

## Block 1: Understanding Errors and Debugging

### Instruction: 30 Minutes

#### Topics

* Bugs
* Syntax errors
* Runtime errors
* Exceptions
* Logic errors
* Tracebacks
* Exception types
* Line numbers
* Reading error messages
* Debugging versus guessing
* Inspecting values
* Isolating problems
* Reproducing failures

### Three Major Error Categories

#### Syntax Error

Python cannot understand the program structure.

Example:

```python
if score >= 70
    print("Pass")
```

Python reports a syntax error because the colon is missing.

#### Runtime Error

The program is valid Python but fails while executing.

Example:

```python
total = 10 / 0
```

This produces:

```text
ZeroDivisionError
```

Another:

```python
record = {
    "record_id": "EQ-1001"
}

print(record["status"])
```

This produces:

```text
KeyError
```

#### Logic Error

The program runs but produces the wrong result.

Example:

```python
length = 10
width = 5

area = length + width
```

Python does exactly what it was told.

The problem is that the programmer wrote the wrong operation.

Logic errors are often harder to find because there may be no traceback.

### Reading a Traceback

Students should not treat a traceback as a wall of incomprehensible text.

Initially, teach them to find:

1. Exception type
2. Error message
3. Relevant file
4. Relevant line number
5. Code on that line

Example:

```text
Traceback (most recent call last):
  File "processor.py", line 18, in <module>
    percentage = completed / total
ZeroDivisionError: division by zero
```

Read from the bottom:

```text
ZeroDivisionError
```

What happened?

```text
division by zero
```

Where?

```text
line 18
```

Which operation?

```python
percentage = completed / total
```

Then inspect:

```python
print(completed)
print(total)
```

### Debugging as a Process

Students should use:

```text
Observe the failure
       ↓
Read the error
       ↓
Locate the failing line
       ↓
Inspect relevant values
       ↓
Form a hypothesis
       ↓
Make one change
       ↓
Run again
```

Avoid:

```text
Change random things
       ↓
Run
       ↓
Change more things
       ↓
Run
       ↓
Hope
```

### Print Debugging

Simple inspection is valuable:

```python
print(f"DEBUG completed={completed}")
print(f"DEBUG total={total}")
```

Students will learn proper logging later, but `print()` is sufficient for learning the debugging process.

### Isolate the Problem

If a 100-line program fails during:

```python
calculate_percentage(10, 0)
```

students should test the function independently:

```python
print(calculate_percentage(10, 0))
```

This reduces the problem.

### Guided Exercise: 30 Minutes

Students receive intentionally broken programs containing:

* Missing colon
* Incorrect indentation
* Misspelled variable
* Invalid dictionary key
* Division by zero
* String/integer mismatch
* Incorrect comparison
* Incorrect calculation
* Incorrect `elif` order

For each problem students record:

```text
Error category:
Observed behavior:
Relevant line:
Cause:
Correction:
```

### Block 1 Applied Challenge

Students receive a broken record-processing program containing at least six defects.

Some produce exceptions.

Others produce incorrect results.

Students must find and correct every problem.

---

## Block 2: Exception Handling

### Instruction: 30 Minutes

#### Topics

* Exceptions
* Expected versus unexpected failures
* `try`
* `except`
* Specific exception types
* `else`
* `finally`
* Converting input safely
* Raising exceptions
* Avoiding bare `except`
* When errors should propagate

### Expected Failure

Consider:

```python
record_count = int(input("Record count: "))
```

The user enters:

```text
twelve
```

Python raises:

```text
ValueError
```

A program may reasonably expect users to occasionally enter invalid input.

### `try` and `except`

```python
try:
    record_count = int(
        input("Record count: ")
    )
except ValueError:
    print("Record count must be a whole number.")
```

### Mental Model

```text
Try operation
     ↓
Success? ─── Yes ──→ Continue
     ↓
     No
     ↓
Matching exception handler
     ↓
Recovery behavior
```

### Catch Specific Exceptions

Prefer:

```python
except ValueError:
```

over:

```python
except:
```

A bare `except` can hide unexpected problems.

Example:

```python
try:
    result = calculate_something()
except:
    print("Something went wrong")
```

This may conceal:

* Programming bugs
* Misspelled variables
* Unexpected system problems

Students should learn:

> Handle errors you expect and understand. Do not automatically hide every possible failure.

### Multiple Exception Types

```python
try:
    percentage = completed / total
except ZeroDivisionError:
    print("Total cannot be zero")
except TypeError:
    print("Values must be numeric")
```

### `else`

```python
try:
    record_count = int(user_input)
except ValueError:
    print("Invalid record count")
else:
    print(f"Record count: {record_count}")
```

The `else` block runs when no exception occurs.

### `finally`

```python
try:
    print("Attempting operation")
except ValueError:
    print("Invalid value")
finally:
    print("Operation finished")
```

`finally` runs whether the operation succeeds or fails.

Students only need the conceptual purpose at this point. File cleanup will make `finally` more meaningful later.

### Raising an Exception

Functions can intentionally reject invalid input.

```python
def calculate_percentage(
    completed: int,
    total: int
) -> float:

    if total <= 0:
        raise ValueError(
            "total must be greater than zero"
        )

    return completed / total * 100
```

This communicates:

> The function cannot meaningfully perform its job with this input.

### Validation Versus Exceptions

Students should begin distinguishing:

```text
Expected business condition
```

from:

```text
Impossible or invalid function input
```

For example:

```text
Record contains 3 errors
```

may simply result in a warning classification.

But:

```text
total = -10
```

may violate a function's assumptions and justify an exception.

### Guided Exercise: 30 Minutes

#### Exercise 1: Safe Integer Conversion

Students repeatedly test:

```python
try:
    value = int(user_input)
except ValueError:
    ...
```

with:

```text
100
-5
12.5
hello
```

#### Exercise 2: Safe Division

Students create:

```python
def calculate_average(total, count):
```

and decide how zero should be handled.

#### Exercise 3: Dictionary Access

Students compare:

```python
record["status"]
```

with:

```python
record.get("status")
```

and discuss when a missing value is expected versus unexpected.

#### Exercise 4: Raise an Exception

Students modify:

```python
calculate_percentage()
```

so invalid totals raise `ValueError`.

#### Exercise 5: Catch the Error

Students call the function inside a `try` block and produce a readable message.

### Block 2 Applied Challenge

Students improve their record-processing functions so malformed input does not crash the entire dataset processing operation.

For each record:

```python
for record in records:
    try:
        processed_record = process_record(record)
    except ValueError as error:
        print(
            f"Rejected record: {error}"
        )
        continue

    processed_records.append(
        processed_record
    )
```

Students should recognize a major real-world idea:

> One bad record does not necessarily need to terminate processing of every other record.

---

## Block 3: Assertions and Testing Functions

### Instruction: 30 Minutes

#### Topics

* Why testing exists
* Expected versus actual behavior
* Test cases
* Assertions
* Normal cases
* Boundary cases
* Invalid cases
* Regression testing
* Testing functions independently
* Arrange-Act-Assert pattern

### Why Test?

A programmer may manually run:

```python
calculate_percentage(50, 100)
```

and observe:

```text
50
```

But what about:

```python
calculate_percentage(0, 100)
calculate_percentage(100, 100)
calculate_percentage(1, 3)
calculate_percentage(50, 0)
```

Software often fails at unusual values rather than typical ones.

Testing asks:

> Given a known input, does the program produce the expected behavior?

### Assertions

```python
result = calculate_percentage(50, 100)

assert result == 50
```

If the condition is true, execution continues.

If false, Python raises:

```text
AssertionError
```

### Simple Test

```python
def test_calculate_percentage():
    result = calculate_percentage(50, 100)

    assert result == 50
```

### Arrange, Act, Assert

A useful structure:

```text
Arrange
    Prepare input

Act
    Run the code

Assert
    Verify the result
```

Example:

```python
def test_normalize_status():

    # Arrange
    raw_status = " ACTIVE "

    # Act
    result = normalize_status(raw_status)

    # Assert
    assert result == "active"
```

### Normal Cases

Typical values:

```python
assert calculate_percentage(50, 100) == 50
```

### Boundary Cases

Values at important boundaries:

```python
assert calculate_percentage(0, 100) == 0
assert calculate_percentage(100, 100) == 100
```

For validation:

```python
assert is_valid_percentage(0) is True
assert is_valid_percentage(100) is True
```

Then:

```python
assert is_valid_percentage(-1) is False
assert is_valid_percentage(101) is False
```

### Testing Boolean Functions

```python
def test_supported_csv():
    assert is_supported_file(
        "records.csv"
    ) is True
```

```python
def test_unsupported_txt():
    assert is_supported_file(
        "records.txt"
    ) is False
```

### Testing Normalization

```python
def test_normalize_status():
    assert normalize_status(
        " ACTIVE "
    ) == "active"
```

### Regression Tests

Suppose a bug occurs because:

```text
" REPORT.CSV "
```

is incorrectly rejected.

After fixing the bug, create a test:

```python
def test_csv_with_spaces_and_capitals():
    assert is_supported_file(
        " REPORT.CSV "
    ) is True
```

Now if a future change accidentally reintroduces the bug, the test catches it.

This introduces the idea of regression testing.

### Guided Exercise: 30 Minutes

Students write assertions for functions developed during the morning.

Minimum tests:

#### `normalize_status()`

Test:

* Lowercase
* Uppercase
* Leading whitespace
* Trailing whitespace

#### `is_supported_file()`

Test:

* CSV
* JSON
* TXT
* Uppercase extension
* Extra whitespace

#### `calculate_percentage()`

Test:

* 0%
* 50%
* 100%

#### `classify_error_count()`

Test:

* 0
* 1
* 5
* 6

This intentionally tests classification boundaries.

### Block 3 Applied Challenge

Students create a test table before writing code.

Example:

| Input       | Expected  |
| ----------- | --------- |
| `0` errors  | valid     |
| `1` error   | warning   |
| `5` errors  | warning   |
| `6` errors  | rejected  |
| `-1` errors | exception |

They then implement the function and assertions.

This reinforces an important practice:

> Decide what correct behavior means before trying to prove the implementation is correct.

---

## Block 4: Automated Tests and Refactoring for Testability

### Instruction: 30 Minutes

#### Topics

* Automated testing
* Test functions
* Test discovery concept
* `pytest`
* Test files
* Naming conventions
* Running tests
* Passing and failing tests
* Testing exceptions
* Keeping functions small
* Why testable code is often better-designed code
* Separating input/output from processing
* Refactoring the record pipeline

### Introducing `pytest`

Students should understand that manually running dozens of assertions becomes inconvenient.

A testing framework can automatically:

1. Find tests.
2. Execute them.
3. Report which passed.
4. Report which failed.

Example test file:

```text
test_processing.py
```

Example:

```python
def test_normalize_status():
    result = normalize_status(" ACTIVE ")

    assert result == "active"
```

Run:

```text
pytest
```

The instructor demonstrates output showing passing tests.

### Multiple Tests

```python
def test_active_status():
    assert normalize_status(
        " ACTIVE "
    ) == "active"


def test_inactive_status():
    assert normalize_status(
        " Inactive "
    ) == "inactive"


def test_supported_csv():
    assert is_supported_file(
        "records.csv"
    ) is True


def test_unsupported_txt():
    assert is_supported_file(
        "records.txt"
    ) is False
```

### Testing Exceptions

Using `pytest`:

```python
import pytest


def test_percentage_rejects_zero_total():

    with pytest.raises(ValueError):
        calculate_percentage(10, 0)
```

Students do not need to deeply understand context managers yet.

The instructor can explain:

> This test says that raising `ValueError` is the expected behavior.

### Why Input Functions Are Harder to Test

Consider:

```python
def calculate_percentage():
    completed = int(
        input("Completed: ")
    )

    total = int(
        input("Total: ")
    )

    result = completed / total * 100

    print(result)
```

This function:

* Reads input
* Performs calculation
* Prints output

Testing the calculation becomes unnecessarily difficult.

Better:

```python
def calculate_percentage(
    completed,
    total
):
    return completed / total * 100
```

Then separately:

```python
completed = int(
    input("Completed: ")
)

total = int(
    input("Total: ")
)

result = calculate_percentage(
    completed,
    total
)

print(result)
```

The calculation is now independently testable.

### Separation of Concerns

Students should begin thinking in three layers:

```text
Input
  ↓
Processing
  ↓
Output
```

Avoid mixing all three inside every function.

Example architecture:

```text
Get raw data
      ↓
normalize_record()
      ↓
validate_record()
      ↓
calculate_metrics()
      ↓
classify_record()
      ↓
Create output
```

Each middle stage can be tested without requiring interactive input.

### Guided Exercise: 30 Minutes

Students take a function that:

* Reads user input
* Cleans it
* Validates it
* Calculates something
* Prints the result

and refactor it into:

```python
normalize_input()
validate_input()
calculate_result()
format_result()
```

They then write tests for the processing functions.

### Block 4 Applied Challenge: Test the Record Processor

Students write tests for their refactored Day 3 record processor.

Minimum tests:

1. Valid record becomes `ready`.
2. Missing ID becomes `rejected`.
3. Unsupported file type becomes `rejected`.
4. Minor errors produce `warning`.
5. Too many errors produce `rejected`.
6. Uppercase file extensions are accepted.
7. Extra whitespace is normalized.
8. Completion of `0` is valid.
9. Completion of `100` is valid.
10. Completion above `100` is rejected.

---

# Day 4 End-of-Day Integrated Challenge

## Refactor and Test the Multi-Record Intake Processor

Students return to the Day 3 integrated challenge.

The original program may resemble:

```text
Input records
      ↓
Large loop
      ↓
Lots of conditions
      ↓
Normalization
      ↓
Validation
      ↓
Classification
      ↓
Output
```

The goal is to restructure it into reusable components.

## Required Functions

Students should create functions similar to:

```python
normalize_record_id()
normalize_source()
is_supported_file()
validate_record()
classify_record()
process_record()
create_summary()
```

Exact function names may vary.

---

## Suggested Structure

### Normalize Identifier

```python
def normalize_record_id(
    record_id: str
) -> str:
    """Normalize a record identifier."""

    return record_id.strip().upper()
```

### Normalize Source

```python
def normalize_source(
    source: str
) -> str:
    """Normalize a source-system name."""

    return source.strip().lower()
```

### Validate File

```python
def is_supported_file(
    file_name: str
) -> bool:
    """Return whether the file type is supported."""

    file_name = file_name.strip().lower()

    return (
        file_name.endswith(".csv")
        or file_name.endswith(".json")
    )
```

### Validate Record

```python
def validate_record(
    record: dict
) -> tuple:

    if record["record_id"] == "":
        return "rejected", "Missing record ID"

    if record["record_count"] <= 0:
        return "rejected", "Invalid record count"

    if not 0 <= record["completion"] <= 100:
        return "rejected", "Invalid completion value"

    if record["error_count"] < 0:
        return "rejected", "Invalid error count"

    if record["error_count"] > 5:
        return "rejected", "Too many errors"

    if record["error_count"] > 0:
        return "warning", "Minor errors detected"

    if record["completion"] < 100:
        return "warning", "Processing incomplete"

    return "ready", "Record passed validation"
```

### Process Record

```python
def process_record(
    record: dict
) -> dict:

    cleaned_record = {
        "record_id": normalize_record_id(
            record["record_id"]
        ),
        "source": normalize_source(
            record["source"]
        ),
        "file_name": record["file_name"].strip().lower(),
        "record_count": record["record_count"],
        "completion": record["completion"],
        "error_count": record["error_count"],
    }

    status, message = validate_record(
        cleaned_record
    )

    cleaned_record["processing_status"] = status
    cleaned_record["message"] = message

    return cleaned_record
```

---

## Main Processing Loop

The final main loop should become much easier to read:

```python
processed_records = []

for record in records:

    processed_record = process_record(
        record
    )

    processed_records.append(
        processed_record
    )
```

Students should compare this with their original Day 3 program.

The goal is for them to recognize that functions allow the main program to describe **what is happening** without exposing every implementation detail at once.

---

# Required Automated Tests

Students must create at least ten automated tests.

Suggested tests:

```text
normalize_record_id
    lowercase input
    whitespace

normalize_source
    uppercase input
    whitespace

is_supported_file
    CSV
    JSON
    uppercase CSV
    unsupported TXT

validate_record
    valid record
    missing ID
    invalid count
    completion > 100
    negative error count
    minor errors
    excessive errors
```

Students run the entire test suite.

The goal is:

```text
All tests pass
```

before declaring the program complete.

---

# Day 4 Common Errors to Address

## Defining a Function but Never Calling It

```python
def say_hello():
    print("Hello")
```

This only defines the function.

Students must call:

```python
say_hello()
```

---

## Forgetting `return`

Incorrect:

```python
def calculate_total(price, quantity):
    total = price * quantity
```

Then:

```python
result = calculate_total(10, 5)
```

produces:

```python
None
```

Correct:

```python
def calculate_total(price, quantity):
    return price * quantity
```

---

## Confusing `print()` and `return`

Students should repeatedly reinforce:

```text
print()
    ↓
Communicates with the human

return
    ↓
Communicates with the calling code
```

---

## Code After `return`

```python
def example():

    return 5

    print("Finished")
```

The `print()` statement never executes.

Once a function returns, execution leaves the function.

---

## Incorrect Scope Assumptions

```python
def calculate():
    result = 100

calculate()

print(result)
```

`result` is local and unavailable outside the function.

Correct:

```python
def calculate():
    return 100

result = calculate()

print(result)
```

---

## Accidentally Depending on Globals

Instead of:

```python
maximum_errors = 5

def is_valid(error_count):
    return error_count <= maximum_errors
```

students should generally prefer:

```python
def is_valid(
    error_count,
    maximum_errors
):
    return error_count <= maximum_errors
```

when the value is part of the function's configurable behavior.

---

## Catching Every Exception

Avoid:

```python
try:
    result = process_record(record)
except:
    print("Error")
```

Prefer handling known problems:

```python
try:
    result = process_record(record)
except ValueError as error:
    print(error)
```

---

## Using Exception Handling to Hide Bugs

Students should not write:

```python
try:
    lots_of_code()
except Exception:
    pass
```

This can make failures invisible.

The goal of exception handling is not:

```text
Make errors disappear
```

It is:

```text
Handle known failure conditions intentionally.
```

---

## Testing Only the Happy Path

A function should not only be tested with:

```text
normal input
```

Students should think about:

```text
Normal
Boundary
Invalid
```

For a percentage:

```text
50       normal
0        boundary
100      boundary
-1       invalid
101      invalid
```

---

## Changing Code Until a Test Passes Without Understanding Why

A failed test is evidence.

Students should:

1. Read the failure.
2. Compare expected and actual values.
3. Identify the relevant function.
4. Inspect the inputs.
5. Understand the cause.
6. Correct the implementation or the test.

---

# Day 4 Instructor Demonstration Strategy

The central instructional theme should be **controlling complexity**.

Begin with a program students already understand:

```python
records = [...]

ready_records = []
warning_records = []
rejected_records = []

for record in records:
    # 30–40 lines of processing
```

Ask:

> Does this work?

Probably.

Then ask:

> How quickly can you understand it?

> Where would you look if normalization is wrong?

> How would you reuse only the validation logic?

> How would you prove the validation logic works?

Gradually transform:

```text
One large program
```

into:

```text
normalize_record()
      ↓
validate_record()
      ↓
classify_record()
      ↓
process_record()
```

Then demonstrate that each piece can be independently exercised:

```python
normalize_record(test_record)
```

and independently tested:

```python
def test_normalize_record():
    ...
```

The important conceptual progression is:

```text
Working code
    ↓
Reusable code
    ↓
Understandable code
    ↓
Testable code
    ↓
Reliable code
```

---

# Day 4 Knowledge Check

Students should be able to answer or demonstrate:

1. What problem do functions solve?
2. What is the difference between defining and calling a function?
3. What is a parameter?
4. What is an argument?
5. What does `return` do?
6. How is `return` different from `print()`?
7. Can a function return a list or dictionary?
8. What happens after a function executes `return`?
9. What is a local variable?
10. Why can excessive use of global variables cause problems?
11. What is a side effect?
12. What is meant by a function having a single responsibility?
13. What does a type hint communicate?
14. What is a docstring?
15. What is a syntax error?
16. What is a runtime error?
17. What is a logic error?
18. What information should you find in a traceback?
19. What does `try` do?
20. What does `except` do?
21. Why should specific exceptions generally be caught?
22. What does `raise` do?
23. What does an assertion verify?
24. What is a boundary test?
25. What is a regression test?
26. Why are small functions generally easier to test?
27. Why should processing logic generally be separated from interactive input and display?

---

# Day 4 End-of-Day Outcomes

By the end of Day 4, students should no longer think of a Python program as simply a long sequence of statements.

They should understand that larger programs can be decomposed into reusable components:

```text
Main Program
     ↓
process_record()
     ↓
 ┌───────────────┐
 │               │
 ↓               ↓
normalize()   validate()
 │               │
 └───────┬───────┘
         ↓
     classify()
         ↓
    Output Record
```

Students should be comfortable with:

* Defining functions
* Calling functions
* Parameters
* Arguments
* Return values
* Boolean-returning functions
* Collection-returning functions
* Multiple return values
* Default arguments
* Keyword arguments
* Local scope
* Basic side effects
* Function composition
* Docstrings
* Type hints
* Reading tracebacks
* Systematic debugging
* `try` and `except`
* Raising exceptions
* Assertions
* Basic `pytest` tests
* Normal cases
* Boundary cases
* Invalid cases
* Refactoring for testability

Most importantly, their mental model should evolve from:

```text
"I wrote the code and it ran."
```

to:

```text
"I divided the problem into small pieces,
each piece has a clear responsibility,
and I can demonstrate that those pieces
behave correctly."
```

This prepares students for Day 5, where those programs begin interacting with the outside world through files and structured data. Students will read and write text, CSV, and JSON data and begin organizing their Python code across multiple modules rather than keeping an entire project in a single file.
