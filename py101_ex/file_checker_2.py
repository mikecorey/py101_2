fn = input("Enter a filename: ")

valid_extensions = [
    'csv',
    'json',
    'parquet',
    'md',
    'txt',
]

extension = fn.split('.')[-1]

is_valid_extension = extension in valid_extensions
is_sales_data = 'sales' in fn
is_draft = fn.lower().startswith('draft')

error_reasons = []

if not is_valid_extension:
    error_reasons.append('Not a valid file extension.')
if not is_sales_data:
    error_reasons.append('Not sales data.')
if is_draft:
    error_reasons.append('This is still draft data.  Not finalized')

if len(error_reasons) == 0:
    print(f"we will process valid final sales {extension}")
else:
    print("The following Errors exist:")
    for e in error_reasons:
        print(f'\t{e}')
