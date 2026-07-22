# Day 2: Expressions, Comparisons, and Program Decisions

## Day 2 Purpose

Day 1 introduced students to the layers beneath a computer and showed them how to write simple Python statements.

Day 2 moves from merely storing and displaying values to making programs evaluate information and make decisions.

Students will learn how to:

* Construct more complex expressions
* Manipulate text data
* Compare values
* Combine multiple conditions
* Accept and convert input
* Control which code runs
* Translate written business rules into Python
* Validate records and classify data

These skills form the foundation for nearly every later programming activity. Data cleaning, filtering, validation, transformation, access control, workflow logic, and error detection all depend on expressions and conditional logic.

The primary mental model for Day 2 is:

```text
Receive a value
      ↓
Interpret the value
      ↓
Evaluate one or more conditions
      ↓
Choose an action
      ↓
Produce a result
```

---

# Morning Session: Values, Expressions, and Comparisons

## Morning Learning Objectives

By the end of the morning session, students will be able to:

1. Construct arithmetic expressions using multiple operators.
2. Predict the result of an expression using operator precedence.
3. Explain the difference between integer and floating-point calculations.
4. Use common string operations and methods.
5. Normalize inconsistent text values.
6. Compare numbers and strings.
7. Create Boolean expressions.
8. Combine conditions using `and`, `or`, and `not`.
9. Convert values between common Python data types.
10. Explain why values received from users or files may require conversion.

---

## Block 1: Numeric Expressions and Calculations

### Instruction: 30 Minutes

#### Topics

* Reviewing integers and floating-point numbers
* Numeric literals
* Using underscores in large numbers
* Arithmetic operators
* Operator precedence
* Parentheses
* Division behavior
* Integer division
* Remainders
* Exponents
* Assignment and reassignment
* Calculation results as new values
* Basic rounding
* Floating-point limitations at a conceptual level
* Writing calculations that communicate intent

#### Arithmetic Operators

| Operator | Meaning                   | Example  |
| -------- | ------------------------- | -------- |
| `+`      | Addition                  | `5 + 3`  |
| `-`      | Subtraction               | `5 - 3`  |
| `*`      | Multiplication            | `5 * 3`  |
| `/`      | Division                  | `5 / 3`  |
| `//`     | Integer or floor division | `5 // 3` |
| `%`      | Remainder                 | `5 % 3`  |
| `**`     | Exponent                  | `5 ** 3` |

#### Example

```python
unit_price = 24.95
quantity = 12
shipping_cost = 18.00

subtotal = unit_price * quantity
total_cost = subtotal + shipping_cost

print(f"Subtotal: ${subtotal:.2f}")
print(f"Shipping: ${shipping_cost:.2f}")
print(f"Total: ${total_cost:.2f}")
```

#### Operator Precedence

Python generally evaluates arithmetic expressions in the following order:

1. Parentheses
2. Exponents
3. Multiplication and division
4. Addition and subtraction

For example:

```python
result = 10 + 4 * 2
```

produces `18`, because multiplication happens before addition.

The following expression produces `28`:

```python
result = (10 + 4) * 2
```

#### Division, Integer Division, and Remainders

```python
total_minutes = 135

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"{hours} hours and {remaining_minutes} minutes")
```

This introduces an important programming pattern:

* Integer division determines how many complete groups exist.
* The remainder determines what is left over.

This pattern can be used for:

* Minutes and hours
* Seconds and minutes
* Items and boxes
* Records and batches
* Bytes and storage units
* Work items and processing groups

#### Floating-Point Values

Students should understand that decimal values are represented internally using binary approximations.

For example:

```python
print(0.1 + 0.2)
```

may not display exactly `0.3`.

The instructor should explain that this is not a Python mistake. It is a consequence of how many decimal fractions are represented in binary.

At this point, students only need to know:

* Floating-point values are usually appropriate for measurements and general calculations.
* Display formatting can control visible decimal places.
* Financial and precision-sensitive calculations sometimes require specialized approaches introduced later.

### Guided Exercise: 30 Minutes

Students complete a calculation worksheet in Python.

#### Exercise 1: Storage Conversion

```python
file_size_bytes = 8_750_000

file_size_kb = file_size_bytes / 1_000
file_size_mb = file_size_bytes / 1_000_000
```

Students print all three values using formatted output.

#### Exercise 2: Task Completion

```python
completed_tasks = 37
total_tasks = 48
```

Students calculate:

* Remaining tasks
* Percentage completed
* Percentage remaining

#### Exercise 3: Batch Processing

```python
total_records = 10_250
batch_size = 1_000
```

Students calculate:

* Number of complete batches
* Number of records left over
* Total batches required when a partial batch is included

#### Exercise 4: Cost Estimate

Students calculate the total cost of a project using:

* Labor hours
* Hourly rate
* Equipment cost
* Travel cost
* Contingency percentage

#### Exercise 5: Predict Before Running

Students predict the results of expressions such as:

```python
print(4 + 3 * 2)
print((4 + 3) * 2)
print(17 // 5)
print(17 % 5)
print(2 ** 4)
```

They then run the code and compare their predictions with the results.

### Block 1 Applied Challenge

Students create a processing-time estimator.

The program should store:

* Total number of records
* Number of records processed per minute
* Number of available processors
* Estimated setup time

The program should calculate and display:

* Processing time on one processor
* Approximate processing time using all available processors
* Total estimated time including setup
* Whole hours and remaining minutes

The instructor should note that real parallel processing is more complicated, but the exercise reinforces numeric expressions and the idea of decomposing a problem into intermediate calculations.

---

## Block 2: Working with Strings as Data

### Instruction: 30 Minutes

#### Topics

* Strings as sequences of characters
* String length
* Index positions
* Zero-based indexing
* Negative indexing
* Slicing
* String methods
* Whitespace
* Case normalization
* Replacing text
* Searching within strings
* String immutability
* Formatted output
* Text data as structured information

#### Strings as Sequences

A string is not simply one indivisible object. It can be treated as an ordered sequence of characters.

```python
project_code = "ALPHA-204"
```

Conceptually, Python numbers the characters beginning at zero:

```text
Character:  A  L  P  H  A  -  2  0  4
Index:      0  1  2  3  4  5  6  7  8
```

Examples:

```python
print(project_code[0])
print(project_code[6])
print(project_code[-1])
```

#### Slicing

A slice selects a range of characters.

```python
project_name = project_code[0:5]
project_number = project_code[6:9]

print(project_name)
print(project_number)
```

The ending position is not included.

Students should recognize the basic pattern:

```python
text[start:end]
```

#### Common String Methods

```python
name = "  jordan smith  "

clean_name = name.strip()
uppercase_name = clean_name.upper()
display_name = clean_name.title()
```

Important methods include:

| Method          | Purpose                                |
| --------------- | -------------------------------------- |
| `.strip()`      | Remove leading and trailing whitespace |
| `.lower()`      | Convert to lowercase                   |
| `.upper()`      | Convert to uppercase                   |
| `.title()`      | Capitalize words for display           |
| `.replace()`    | Replace part of a string               |
| `.startswith()` | Check the beginning of a string        |
| `.endswith()`   | Check the ending of a string           |
| `.find()`       | Find the position of text              |
| `.count()`      | Count occurrences                      |
| `.isdigit()`    | Check whether characters are digits    |
| `.isalpha()`    | Check whether characters are letters   |

#### String Immutability

Strings cannot be changed character by character in place.

A method such as:

```python
clean_name = name.strip()
```

creates or returns a new string value. It does not rewrite the original string automatically.

```python
name = "  jordan smith  "
name.strip()

print(name)
```

The original whitespace still exists because the returned value was not assigned.

The corrected version is:

```python
name = name.strip()
```

#### Normalizing Text

Data frequently contains inconsistent capitalization or extra spaces.

These values appear different to a computer:

```text
ACTIVE
Active
active
 active
active 
```

A common normalization process is:

```python
status = " Active "
normalized_status = status.strip().lower()

print(normalized_status)
```

The result is:

```text
active
```

This concept will later be used extensively when cleaning datasets.

### Guided Exercise: 30 Minutes

Students receive several inconsistent text values.

```python
employee_name = "  aLEX joHNSON "
department = "engineering "
status = " ACTIVE"
employee_id = "emp-00427"
file_name = "Quarterly_Report.CSV"
```

Students create normalized versions:

```python
clean_employee_name = employee_name.strip().title()
clean_department = department.strip().lower()
clean_status = status.strip().lower()
clean_employee_id = employee_id.strip().upper()
clean_file_name = file_name.strip().lower()
```

Students then:

1. Display the original and cleaned values.
2. Print the length of each value before and after cleaning.
3. Extract the employee number from the employee ID.
4. Determine whether the file name ends in `.csv`.
5. Extract the file extension.
6. Replace underscores in the file name with spaces.
7. Create a formatted summary.

#### Example

```python
employee_id = "emp-00427"

prefix = employee_id[0:3]
employee_number = employee_id[4:]

print(f"Prefix: {prefix}")
print(f"Employee number: {employee_number}")
```

### Block 2 Applied Challenge

Students create a filename analysis program.

The program should store a file name such as:

```python
file_name = "  FY2026_Equipment_Status_FINAL.CSV  "
```

It should then:

* Remove extra whitespace
* Convert the value to lowercase
* Determine the total number of characters
* Determine whether it is a CSV file
* Extract the extension
* Replace underscores with spaces
* Create a human-readable display name
* Print the original and normalized versions

Example output:

```text
Original:   FY2026_Equipment_Status_FINAL.CSV
Normalized: fy2026_equipment_status_final.csv
Extension: csv
CSV file: True
Display name: Fy2026 Equipment Status Final
```

---

## Block 3: Comparisons and Boolean Logic

### Instruction: 30 Minutes

#### Topics

* Boolean values
* Expressions that produce Boolean results
* Equality and inequality
* Numeric comparisons
* String comparisons
* Membership testing
* Combining conditions
* Truth tables
* Operator precedence
* Chained comparisons
* Naming Boolean variables clearly

#### Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `<=`     | Less than or equal to    |
| `>`      | Greater than             |
| `>=`     | Greater than or equal to |

#### Equality Versus Assignment

Students must clearly distinguish:

```python
status = "active"
```

from:

```python
status == "active"
```

The single equal sign assigns a value.

The double equal sign compares two values and produces either `True` or `False`.

#### Examples

```python
record_count = 1_250
minimum_required = 1_000

has_enough_records = record_count >= minimum_required

print(has_enough_records)
```

```python
status = "active"

is_active = status == "active"
is_inactive = status == "inactive"
is_not_closed = status != "closed"
```

#### String Comparisons

String comparisons are case-sensitive:

```python
print("Active" == "active")
```

This produces `False`.

That is why normalization is commonly performed before comparison:

```python
status = " Active "
normalized_status = status.strip().lower()

is_active = normalized_status == "active"
```

#### Membership Testing

The `in` operator checks whether a value appears within another value.

```python
file_name = "equipment_status.csv"

contains_status = "status" in file_name
is_csv = ".csv" in file_name
```

At this stage, students use membership testing primarily with strings. Membership testing with collections will be covered more fully on Day 3.

#### Combining Conditions with `and`

Both conditions must be true.

```python
age = 35
has_badge = True

can_enter = age >= 18 and has_badge
```

#### Combining Conditions with `or`

At least one condition must be true.

```python
is_manager = False
is_administrator = True

has_elevated_access = is_manager or is_administrator
```

#### Negating a Condition with `not`

```python
system_locked = False

system_available = not system_locked
```

#### Basic Truth Table

| A     | B     | `A and B` | `A or B` |
| ----- | ----- | --------- | -------- |
| False | False | False     | False    |
| False | True  | False     | True     |
| True  | False | False     | True     |
| True  | True  | True      | True     |

#### Chained Comparisons

Python allows readable range checks:

```python
temperature = 72

is_normal = 60 <= temperature <= 80
```

This is equivalent to:

```python
is_normal = temperature >= 60 and temperature <= 80
```

#### Clear Boolean Variable Names

Students should prefer names that sound like yes-or-no questions:

```python
is_active = True
has_required_fields = False
can_process_record = True
is_valid_temperature = False
```

These names make later conditional statements easier to read.

### Guided Exercise: 30 Minutes

Students create Boolean expressions for a fictional equipment record.

```python
equipment_id = "EQ-1045"
status = "active"
operating_hours = 820
maximum_hours = 1_000
inspection_complete = True
temperature = 74.5
```

Students create variables such as:

```python
has_equipment_prefix = equipment_id.startswith("EQ-")
is_active = status == "active"
is_within_hour_limit = operating_hours <= maximum_hours
has_completed_inspection = inspection_complete
is_temperature_normal = 60 <= temperature <= 80
```

They then combine them:

```python
is_ready = (
    has_equipment_prefix
    and is_active
    and is_within_hour_limit
    and has_completed_inspection
    and is_temperature_normal
)
```

Students should print every intermediate condition rather than immediately writing one long expression.

Example:

```python
print(f"Correct identifier: {has_equipment_prefix}")
print(f"Active status: {is_active}")
print(f"Within hour limit: {is_within_hour_limit}")
print(f"Inspection complete: {has_completed_inspection}")
print(f"Temperature normal: {is_temperature_normal}")
print(f"Ready for use: {is_ready}")
```

#### Additional Exercises

Students write expressions answering questions such as:

* Is a score between 70 and 100?
* Is a file a CSV or JSON file?
* Is a user both active and authorized?
* Is a record missing a required prefix?
* Is a quantity below the reorder level?
* Is a project complete or canceled?
* Does a file name contain the word `final`?
* Is a year divisible by four?

### Block 3 Applied Challenge

Students create a record readiness evaluator using only variables, calculations, comparisons, and Boolean expressions.

The record should include:

* Record identifier
* Status
* Completion percentage
* Error count
* Approval status
* Security classification
* File extension

The final Boolean value should be `True` only when:

* The identifier begins with the correct prefix.
* The status is active.
* Completion is at least 95%.
* The error count is zero.
* Approval has been received.
* The security classification is acceptable.
* The file is a supported type.

Students must print every individual check and the final result.

---

## Block 4: Input, Type Conversion, and Interpreting Raw Values

### Instruction: 30 Minutes

#### Topics

* Programs receiving values
* Hard-coded values compared with user input
* The `input()` function
* Input values as strings
* Explicit type conversion
* `int()`
* `float()`
* `str()`
* Conversion failures
* Converting before calculating
* Normalizing before comparing
* Raw values versus interpreted values
* Why data from files and networks may arrive as text
* Basic data-parsing workflow

#### Reading Input

```python
employee_name = input("Enter employee name: ")
```

The value returned by `input()` is a string.

Even if the user enters:

```text
42
```

Python initially receives:

```python
"42"
```

The quotation marks are not typed by the user, but they represent the fact that Python is treating the input as text.

#### Numeric Conversion

```python
quantity_text = input("Enter quantity: ")
quantity = int(quantity_text)
```

A shorter version is:

```python
quantity = int(input("Enter quantity: "))
```

For beginner instruction, the longer version is often clearer because it shows the two steps:

1. Receive text.
2. Convert the text.

#### Why Conversion Matters

This code joins strings:

```python
first_value = input("Enter a number: ")
second_value = input("Enter another number: ")

result = first_value + second_value
```

Entering `10` and `5` produces:

```text
105
```

The corrected version is:

```python
first_value = int(input("Enter a number: "))
second_value = int(input("Enter another number: "))

result = first_value + second_value
```

This produces:

```text
15
```

#### Common Conversion Functions

```python
record_count = int("1250")
temperature = float("72.5")
message = str(404)
```

#### Conversion Failures

This fails:

```python
record_count = int("twelve")
```

Students do not yet need full exception handling. That will be introduced later.

For now, they should understand:

* Conversion requires compatible text.
* Numeric conversion is an assumption about the input.
* Programs should eventually verify that the assumption is safe.
* Error handling and validation will become increasingly important.

#### Raw-to-Useful Data Workflow

```text
Raw value
    ↓
Remove unnecessary whitespace
    ↓
Normalize capitalization
    ↓
Convert to the intended type
    ↓
Compare or calculate
    ↓
Produce a result
```

Example:

```python
status_input = input("Enter status: ")
status = status_input.strip().lower()

is_active = status == "active"

print(f"Active record: {is_active}")
```

### Guided Exercise: 30 Minutes

Students build a simple interactive project calculator.

The program asks for:

* Project name
* Number of completed tasks
* Total number of tasks
* Budget
* Amount spent
* Whether approval has been received

Example:

```python
project_name = input("Project name: ").strip()
completed_tasks = int(input("Completed tasks: "))
total_tasks = int(input("Total tasks: "))
budget = float(input("Budget: "))
amount_spent = float(input("Amount spent: "))
approval_text = input("Approved? yes/no: ").strip().lower()
```

Students calculate:

```python
completion_percentage = completed_tasks / total_tasks * 100
remaining_budget = budget - amount_spent
is_approved = approval_text == "yes"
```

They print a formatted project summary.

#### Exercise Discussion

Students identify:

* Which values began as text
* Which values were converted to integers
* Which values were converted to floating-point numbers
* Which value was converted into a Boolean expression
* What would happen if the user entered an unexpected value

### Morning Applied Challenge: Interactive File Processing Estimate

Students create a program that asks the user for:

* File name
* File size in megabytes
* Number of records
* Processing rate per second
* Whether the file has been approved

The program should:

1. Normalize the file name.
2. Determine whether the file has a supported extension.
3. Convert numeric values to appropriate types.
4. Calculate estimated processing time.
5. Calculate complete minutes and remaining seconds.
6. Determine whether the file is approved.
7. Print a formatted summary.
8. Print Boolean values indicating whether the file appears ready.

No `if` statements are required yet. The program should calculate and display Boolean results.

### Morning Knowledge Check

Students should be able to explain:

* The difference between `/`, `//`, and `%`
* Why parentheses can change a calculation
* Why `"Active"` and `"active"` are not equal
* What `.strip()` does
* What `.lower()` does
* The difference between `=` and `==`
* When to use `and`
* When to use `or`
* What `not` does
* Why `input()` produces a string
* Why type conversion may be necessary

---

# Afternoon Session: Conditional Logic and Program Flow

## Afternoon Learning Objectives

By the end of the afternoon session, students will be able to:

1. Use `if` statements to conditionally execute code.
2. Use `if` and `else` to choose between two paths.
3. Use `elif` to classify values into multiple categories.
4. Explain why the order of conditions matters.
5. Use range checks correctly.
6. Combine multiple business rules.
7. Decide when to use nested conditions.
8. Identify gaps and overlaps in decision logic.
9. Validate required values.
10. Assign records a valid, warning, or rejected status.
11. Trace the execution path of a conditional program.

---

## Block 1: Making Decisions with `if` and `else`

### Instruction: 30 Minutes

#### Topics

* Sequential execution
* Conditional execution
* `if` statements
* Code blocks
* Colons
* Indentation
* Conditions as Boolean expressions
* Two-way decisions with `else`
* Execution paths
* Tracing code manually
* Common syntax and indentation errors

#### Sequential Execution

Until this point, most student programs execute from top to bottom:

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

Every statement runs.

A conditional statement allows some code to run only when a condition is true.

#### Basic `if` Statement

```python
temperature = 85

if temperature > 80:
    print("Temperature warning")
```

The indented line runs only if the condition is `True`.

#### Structure

```python
if condition:
    code_that_runs_when_true
```

Important syntax elements include:

* The `if` keyword
* A Boolean expression
* A colon
* An indented block

#### `if` and `else`

```python
inspection_complete = True

if inspection_complete:
    print("Equipment may continue to readiness review.")
else:
    print("Inspection is required.")
```

Exactly one of the two blocks runs.

#### Execution Paths

Students should begin thinking of the program as having branches:

```text
                 Is inspection complete?
                       /          \
                    Yes            No
                    /               \
           Continue review      Require inspection
```

The processor still executes instructions one at a time, but the condition determines which instruction sequence is followed.

#### Conditions Can Be Stored or Written Directly

Stored Boolean:

```python
is_within_limit = operating_hours <= maximum_hours

if is_within_limit:
    print("Within operating limit")
```

Direct comparison:

```python
if operating_hours <= maximum_hours:
    print("Within operating limit")
```

For beginners, storing important conditions in named Boolean variables can improve readability.

#### Indentation

This is valid:

```python
if temperature > 80:
    print("Warning")
    print("Check cooling system")
```

This is not part of the condition:

```python
if temperature > 80:
    print("Warning")

print("Program complete")
```

The final line runs regardless of the temperature.

### Guided Exercise: 30 Minutes

Students write short programs using `if` and `else`.

#### Exercise 1: Pass or Fail

```python
score = 78

if score >= 70:
    print("Pass")
else:
    print("Fail")
```

#### Exercise 2: Inventory Status

```python
quantity_on_hand = 14
reorder_level = 20

if quantity_on_hand <= reorder_level:
    print("Reorder required")
else:
    print("Inventory level acceptable")
```

#### Exercise 3: File Type

```python
file_name = "equipment.csv"

if file_name.lower().endswith(".csv"):
    print("Supported file type")
else:
    print("Unsupported file type")
```

#### Exercise 4: Approval

```python
approval_status = " approved "
approval_status = approval_status.strip().lower()

if approval_status == "approved":
    print("Processing authorized")
else:
    print("Processing not authorized")
```

#### Exercise 5: Predict the Path

Students review several programs without running them and identify:

* Which condition is evaluated
* Whether the condition is `True` or `False`
* Which statements run
* Which statements are skipped
* What output appears

### Block 1 Applied Challenge

Students build a simple access decision program.

The program stores:

* Whether the user has an account
* Whether the account is active
* Whether the user has completed required training
* Whether the system is locked

The first version uses one combined condition:

```python
can_access = (
    has_account
    and account_active
    and training_complete
    and not system_locked
)

if can_access:
    print("Access granted")
else:
    print("Access denied")
```

Students then print each individual condition so that the result can be explained.

---

## Block 2: Multiple Outcomes with `elif`

### Instruction: 30 Minutes

#### Topics

* More than two possible outcomes
* The `elif` keyword
* Mutually exclusive categories
* First matching branch
* Condition order
* Range classification
* Inclusive and exclusive boundaries
* Avoiding gaps
* Avoiding overlaps
* Default behavior with `else`

#### Basic `elif` Structure

```python
if condition_one:
    action_one
elif condition_two:
    action_two
elif condition_three:
    action_three
else:
    default_action
```

Python evaluates the conditions from top to bottom.

Once one condition is true:

* Its block runs.
* The remaining branches are skipped.

#### Example: Score Classification

```python
score = 86

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)
```

#### Why Order Matters

This version is incorrect:

```python
score = 95

if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 80:
    grade = "B"
elif score >= 90:
    grade = "A"
```

The first condition is already true, so the grade becomes `D`.

The instructor should emphasize:

> In an `if`/`elif` chain, Python selects the first true branch, not the most specific or most accurate branch.

#### Range Boundaries

```python
temperature = 82

if temperature < 32:
    category = "freezing"
elif temperature < 60:
    category = "cold"
elif temperature <= 80:
    category = "normal"
else:
    category = "hot"
```

Students should test boundary values such as:

* 31
* 32
* 59
* 60
* 80
* 81

#### Gaps in Logic

```python
if score > 90:
    result = "excellent"
elif score < 70:
    result = "needs improvement"
```

What happens to a score of `80`?

Unless another branch or `else` is provided, no category is assigned.

#### Overlapping Conditions

```python
if temperature >= 70:
    category = "warm"
elif temperature >= 80:
    category = "hot"
```

The second branch can never run because all values greater than or equal to `80` already satisfy the first branch.

### Guided Exercise: 30 Minutes

Students create several classification programs.

#### Exercise 1: Processing Status

Classify completion percentage:

* `100`: Complete
* `90–99.99`: Final review
* `50–89.99`: In progress
* `1–49.99`: Started
* `0`: Not started

#### Exercise 2: Storage Size

Classify a file as:

* Empty
* Small
* Medium
* Large
* Very large

The instructor provides the thresholds.

#### Exercise 3: Error Severity

Based on an error count:

* `0`: Clean
* `1–5`: Warning
* `6–20`: Review required
* More than `20`: Rejected

#### Exercise 4: Age of Data

Based on days since update:

* Current
* Recent
* Stale
* Expired

#### Exercise 5: Boundary Testing

Students create a table showing expected results for values immediately below, equal to, and immediately above each threshold.

### Block 2 Applied Challenge

Students create a record-quality classification program.

Inputs include:

* Completeness percentage
* Error count
* Days since last update
* Approval status

The program assigns an overall status:

* `ready`
* `review`
* `incomplete`
* `rejected`

Students must:

1. Write the classification rules in plain language.
2. Convert those rules into an ordered `if`/`elif`/`else` chain.
3. Test at least six records.
4. Include at least two boundary cases.
5. Explain why the conditions are ordered as written.

---

## Block 3: Compound and Nested Conditions

### Instruction: 30 Minutes

#### Topics

* Combining multiple requirements
* `and`, `or`, and `not` inside conditions
* Parentheses for readability
* Nested `if` statements
* Flat conditions versus nested conditions
* Dependent decisions
* Independent decisions
* Short-circuit evaluation at a basic level
* Decision tables
* Translating policy language into code
* Avoiding overly complex expressions

#### Compound Condition

```python
if status == "active" and error_count == 0:
    print("Record may proceed")
```

#### Multiple Acceptable Values

```python
if file_extension == "csv" or file_extension == "json":
    print("Supported format")
```

#### Negation

```python
if not system_locked:
    print("System available")
```

#### Parentheses for Readability

```python
if (
    status == "active"
    and completion_percentage >= 95
    and error_count == 0
    and is_approved
):
    print("Ready for publication")
```

Parentheses make a long condition easier to read and allow it to span multiple lines.

#### Nested Conditions

A nested condition is an `if` statement inside another conditional block.

```python
if account_active:
    if training_complete:
        print("Access granted")
    else:
        print("Training required")
else:
    print("Account inactive")
```

Nested conditions are useful when the second decision only matters if the first decision succeeds.

#### Flat Alternative

```python
if account_active and training_complete:
    print("Access granted")
elif account_active:
    print("Training required")
else:
    print("Account inactive")
```

Both approaches can work. Students should choose the version that most clearly reflects the decision process.

#### Independent Conditions

Multiple separate `if` statements may all run:

```python
if error_count > 0:
    print("Errors detected")

if missing_fields > 0:
    print("Missing fields detected")

if duplicate_count > 0:
    print("Duplicates detected")
```

This differs from an `if`/`elif` chain, where only one branch runs.

The distinction is important:

* Use separate `if` statements when multiple conditions may require action.
* Use `if`/`elif` when selecting one outcome from a set of alternatives.

#### Decision Table

Before writing a complex condition, students can use a table.

| Active | Approved |      Errors | Result            |
| ------ | -------- | ----------: | ----------------- |
| Yes    | Yes      |           0 | Ready             |
| Yes    | No       |           0 | Awaiting approval |
| Yes    | Yes      | More than 0 | Review            |
| No     | Any      |         Any | Inactive          |

The table can then be translated into Python.

#### Basic Short-Circuit Explanation

In an `and` expression, Python can stop evaluating as soon as one condition is false.

In an `or` expression, Python can stop evaluating as soon as one condition is true.

Students do not need to exploit this behavior yet, but they should understand that conditions are evaluated from left to right.

### Guided Exercise: 30 Minutes

Students translate written rules into Python.

#### Rule Set 1: File Acceptance

A file is accepted when:

* The file is a CSV or JSON file.
* The file size is greater than zero.
* The file size is below the maximum.
* Approval has been received.
* The file is not encrypted with an unsupported method.

#### Rule Set 2: Equipment Readiness

Equipment is ready when:

* The equipment is active.
* Inspection is complete.
* Operating hours are below the limit.
* No critical fault is present.
* Temperature is within the acceptable range.

#### Rule Set 3: User Access

A user is granted access when:

* The user has an active account.
* The user has completed training.
* The user possesses the required role or is an administrator.
* The system is not in maintenance mode.

Students first create named Boolean variables:

```python
has_supported_type = (
    file_extension == "csv"
    or file_extension == "json"
)

has_valid_size = file_size > 0 and file_size <= maximum_size
can_process = has_supported_type and has_valid_size and is_approved
```

They then use those variables in a conditional statement.

### Block 3 Applied Challenge

Students create a decision table and Python program for a data-publication workflow.

The workflow uses:

* Dataset status
* Data owner approval
* Security review completion
* Error count
* Missing-value percentage
* Whether the dataset contains restricted fields
* Whether the user has a publishing role

Possible outcomes include:

* Publish
* Awaiting approval
* Security review required
* Data-quality review required
* Access denied
* Dataset inactive

Students must decide:

* Which conditions are independent
* Which conditions are mutually exclusive
* Which conditions should be evaluated first
* Whether nesting makes the logic easier to understand

---

## Block 4: Validation and Defensive Decision Logic

### Instruction: 30 Minutes

#### Topics

* What validation means
* Raw data versus trusted data
* Required values
* Type expectations
* Range validation
* Allowed-value validation
* Format validation
* Cross-field validation
* Valid, warning, and rejected records
* Validation order
* Avoiding calculations with invalid values
* Communicating why a record failed
* Fail-fast versus collecting multiple problems
* Designing readable validation logic

#### What Validation Means

Validation asks whether data meets the rules required for safe and meaningful processing.

Examples include:

* Is a required value present?
* Is a number within an acceptable range?
* Is a status one of the allowed values?
* Does an identifier follow the required format?
* Does an end date occur after a start date?
* Is a file type supported?
* Is a percentage between 0 and 100?

#### Types of Validation

##### Required-Value Validation

```python
record_id = "EQ-1024"

if record_id == "":
    print("Record ID is required")
```

A stronger version normalizes whitespace first:

```python
record_id = record_id.strip()

if record_id == "":
    print("Record ID is required")
```

##### Range Validation

```python
completion_percentage = 105

if 0 <= completion_percentage <= 100:
    print("Percentage is valid")
else:
    print("Percentage must be between 0 and 100")
```

##### Allowed-Value Validation

Before lists and sets are introduced on Day 3, students can use explicit comparisons:

```python
status = "active"

if status == "active" or status == "inactive" or status == "retired":
    print("Status is valid")
else:
    print("Unsupported status")
```

The instructor can mention that Day 3 will introduce a cleaner way to represent collections of allowed values.

##### Format Validation

```python
equipment_id = "EQ-1045"

has_correct_prefix = equipment_id.startswith("EQ-")
has_expected_length = len(equipment_id) == 7

if has_correct_prefix and has_expected_length:
    print("Identifier format appears valid")
else:
    print("Invalid identifier format")
```

##### Cross-Field Validation

Some values are only valid in relation to other values.

```python
completed_tasks = 12
total_tasks = 10

if completed_tasks <= total_tasks:
    print("Task counts are consistent")
else:
    print("Completed tasks cannot exceed total tasks")
```

#### Validation Order

Students should generally check basic validity before performing dependent calculations.

Risky order:

```python
completion_percentage = completed_tasks / total_tasks * 100

if total_tasks > 0:
    print(completion_percentage)
```

Safer order:

```python
if total_tasks > 0:
    completion_percentage = completed_tasks / total_tasks * 100
    print(completion_percentage)
else:
    print("Total tasks must be greater than zero")
```

This is an early introduction to defensive programming.

#### Record Statuses

A useful pattern is to classify records into three broad categories:

* Valid: processing may continue.
* Warning: processing may continue, but attention is required.
* Rejected: processing should stop for that record.

Example:

```python
if error_count > 10:
    record_status = "rejected"
elif error_count > 0:
    record_status = "warning"
else:
    record_status = "valid"
```

#### Reporting the Reason

A program should ideally explain why a value was rejected.

```python
if record_id.strip() == "":
    validation_message = "Record ID is missing"
elif not record_id.startswith("EQ-"):
    validation_message = "Record ID must begin with EQ-"
else:
    validation_message = "Record ID is valid"

print(validation_message)
```

Students should understand that a simple `True` or `False` result may be enough for a computer, but humans often need an explanatory message.

### Guided Exercise: 30 Minutes

Students validate a fictional maintenance record.

```python
record_id = "EQ-1045"
status = "active"
operating_hours = 850
maximum_hours = 1_000
inspection_complete = True
error_count = 2
temperature = 82
```

The rules are:

* Record ID is required.
* Record ID must begin with `EQ-`.
* Status must be active or inactive.
* Operating hours cannot be negative.
* Maximum hours must be greater than zero.
* Operating hours should not exceed maximum hours.
* Inspection must be complete for an active record.
* Temperature should be between 60 and 80.
* More than five errors causes rejection.
* One to five errors causes a warning.

Students create separate Boolean checks:

```python
has_record_id = record_id.strip() != ""
has_correct_prefix = record_id.startswith("EQ-")
has_valid_status = status == "active" or status == "inactive"
has_valid_hours = operating_hours >= 0 and maximum_hours > 0
is_within_hour_limit = operating_hours <= maximum_hours
has_valid_temperature = 60 <= temperature <= 80
```

Students then assign an overall status.

Example:

```python
if not has_record_id:
    record_status = "rejected"
    status_message = "Record ID is missing"
elif not has_correct_prefix:
    record_status = "rejected"
    status_message = "Record ID format is invalid"
elif not has_valid_status:
    record_status = "rejected"
    status_message = "Status value is invalid"
elif not has_valid_hours:
    record_status = "rejected"
    status_message = "Operating-hour values are invalid"
elif error_count > 5:
    record_status = "rejected"
    status_message = "Too many errors"
elif not inspection_complete:
    record_status = "warning"
    status_message = "Inspection is incomplete"
elif not is_within_hour_limit:
    record_status = "warning"
    status_message = "Operating-hour limit exceeded"
elif not has_valid_temperature:
    record_status = "warning"
    status_message = "Temperature outside preferred range"
elif error_count > 0:
    record_status = "warning"
    status_message = "Minor errors require review"
else:
    record_status = "valid"
    status_message = "Record passed validation"
```

Students test the program by changing one value at a time.

### Block 4 Applied Challenge: Data Intake Validator

Students build a complete validator for one fictional incoming data record.

The record contains:

* Record ID
* Source system
* File name
* File size
* Record count
* Completion percentage
* Error count
* Approval status
* Security review status
* Processing status

#### Required Validation Rules

The program must check:

1. Record ID is not blank.
2. Record ID uses the correct prefix.
3. Source system is recognized.
4. File extension is supported.
5. File size is greater than zero.
6. Record count is greater than zero.
7. Completion percentage is between 0 and 100.
8. Error count is not negative.
9. Approval has been received.
10. Security review is complete.
11. Processing status is active.

#### Required Outcomes

The program assigns one of the following:

* `ready`
* `warning`
* `rejected`

It must also produce a human-readable explanation.

Example output:

```text
Record ID: INGEST-2048
Source: maintenance_system
File: equipment_status.csv
Status: WARNING
Reason: File contains three noncritical errors.
Ready for processing: False
```

#### Required Testing

Students should test at least eight scenarios:

1. Completely valid record
2. Blank record ID
3. Unsupported file type
4. Zero-byte file
5. Completion percentage over 100
6. Negative error count
7. Missing approval
8. Valid record with a small number of noncritical errors

Students should record the expected and actual result for each scenario.

---

# Day 2 End-of-Day Integrated Challenge

Students create a small interactive record-intake program.

## Program Requirements

The program asks the user for:

* Record identifier
* File name
* File size in megabytes
* Record count
* Completion percentage
* Error count
* Approval status
* Security review status

The program must:

1. Remove unnecessary whitespace.
2. Normalize capitalization.
3. Convert numeric values.
4. Determine the file extension.
5. Validate required fields.
6. Validate numeric ranges.
7. Validate approval and security status.
8. Assign an overall classification.
9. Produce a formatted summary.
10. Explain why the record is ready, requires review, or is rejected.

## Sample Input

```text
Record ID: INGEST-2401
File name: equipment_readiness.csv
File size: 18.5
Record count: 12450
Completion percentage: 98
Error count: 2
Approved: yes
Security review complete: yes
```

## Sample Output

```text
Record Intake Summary
---------------------
Record ID: INGEST-2401
File: equipment_readiness.csv
File size: 18.50 MB
Records: 12,450
Completion: 98.0%
Errors: 2
Approved: True
Security review complete: True

Classification: WARNING
Reason: The record passed required validation but contains minor errors.
Ready for automatic processing: False
```

## Optional Extension

Students add an estimated processing time based on a fixed rate of records per second.

```python
processing_rate = 250
estimated_seconds = record_count / processing_rate
```

They display the result as minutes and remaining seconds.

---

# Day 2 Common Errors to Address

The instructor should intentionally demonstrate and correct common mistakes.

## Assignment Instead of Comparison

Incorrect:

```python
if status = "active":
    print("Active")
```

Correct:

```python
if status == "active":
    print("Active")
```

## Missing Colon

Incorrect:

```python
if score >= 70
    print("Pass")
```

Correct:

```python
if score >= 70:
    print("Pass")
```

## Incorrect Indentation

Incorrect:

```python
if score >= 70:
print("Pass")
```

Correct:

```python
if score >= 70:
    print("Pass")
```

## Comparing a String with a Number

```python
record_count = input("Record count: ")

if record_count > 1000:
    print("Large dataset")
```

This fails because `record_count` is a string.

Correct:

```python
record_count = int(input("Record count: "))

if record_count > 1000:
    print("Large dataset")
```

## Using `and` Incorrectly

Incorrect:

```python
if status == "active" and "approved":
    print("Ready")
```

The second part does not perform the intended comparison.

Correct:

```python
if status == "active" and approval_status == "approved":
    print("Ready")
```

## Incorrect Range Logic

Incorrect:

```python
if score >= 70 or score <= 100:
    print("Valid passing score")
```

Almost every number satisfies at least one side.

Correct:

```python
if score >= 70 and score <= 100:
    print("Valid passing score")
```

Or:

```python
if 70 <= score <= 100:
    print("Valid passing score")
```

## Incorrect `elif` Order

Incorrect:

```python
if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 80:
    grade = "B"
```

Correct:

```python
if score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
```

## Forgetting to Normalize Text

```python
status = " Active "

if status == "active":
    print("Active record")
```

Correct:

```python
status = status.strip().lower()

if status == "active":
    print("Active record")
```

---

# Day 2 Instructor Demonstration Strategy

The instructor should use the following progression throughout the day:

1. State the rule in plain language.
2. Identify the values needed.
3. Create individual Boolean checks.
4. Print and verify each Boolean result.
5. Combine the checks.
6. Add conditional behavior.
7. Test normal cases.
8. Test boundary cases.
9. Test intentionally invalid cases.

For example:

```text
Plain-language rule:
A file is ready when it is approved, has no errors, and is a CSV file.
```

Convert the rule into separate checks:

```python
is_approved = approval_status == "approved"
has_no_errors = error_count == 0
is_csv = file_name.lower().endswith(".csv")
```

Combine the checks:

```python
is_ready = is_approved and has_no_errors and is_csv
```

Use the result:

```python
if is_ready:
    print("File is ready")
else:
    print("File is not ready")
```

This approach helps students see that complex business rules are normally built from several small, understandable expressions.

---

# Day 2 Knowledge Check

Students should be able to answer or demonstrate the following:

1. What is the difference between `=` and `==`?
2. What type of value does a comparison produce?
3. When should `and` be used?
4. When should `or` be used?
5. What does `not` do?
6. Why might text be normalized before comparison?
7. Why does the order of `elif` statements matter?
8. What happens after the first true branch in an `if`/`elif` chain?
9. When should separate `if` statements be used instead of `elif`?
10. Why should input be validated before calculation?
11. What is a boundary value?
12. What is the difference between a warning and a rejected record?
13. Why is a human-readable validation message useful?
14. Why should complex conditions be divided into named Boolean variables?
15. How can a written business rule be translated into Python?

---

# Day 2 End-of-Day Outcomes

By the end of Day 2, students should be able to write programs that:

* Receive values
* Normalize text
* Convert data types
* Perform calculations
* Compare values
* Combine Boolean conditions
* Select among multiple execution paths
* Validate basic records
* Assign classifications
* Explain why a decision was made

The students' programming model should now expand from simple sequential execution:

```text
Statement
    ↓
Statement
    ↓
Statement
```

to decision-based execution:

```text
Receive data
     ↓
Normalize and convert
     ↓
Evaluate conditions
     ↓
Choose an execution path
     ↓
Produce a result and explanation
```

This prepares students for Day 3, where they will begin working with collections of values and processing multiple records rather than evaluating only one record at a time.
