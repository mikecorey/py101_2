fn = input("Enter a filename: ")

valid_extension = (
    fn.endswith('.csv') or
    fn.endswith('.md') or
    fn.endswith('.txt') or
    fn.endswith('.json')
)

extension = fn.split('.')[-1]

is_sales_data = 'sales' in fn
is_draft = fn.lower().startswith('draft')

if valid_extension:
    if is_sales_data:
        if not is_draft:
            print(f"we will process valid final sales {extension}")
        else:
            print("This sales data is just draft data.  We will not process it.")
    else:
        print("This doesn't seem to be sales data. We will not process it.")
else:
    print(f"I don't know how to handle {extension}")