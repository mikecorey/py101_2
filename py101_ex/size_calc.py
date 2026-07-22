file_size_str = input("enter file size (in KB): ")
file_size = int(file_size_str)

total_space_str = input("enter total space (in KB): ")
total_space = int(total_space_str)

remaining_space = total_space - file_size
remaining_space_bytes = remaining_space * 1000
remaining_space_kibibytes = remaining_space_bytes / 1024
if remaining_space > 0:
    print(f"Great! You have {remaining_space} KB left over.")
    print(f"  oh by the way, that's {remaining_space_kibibytes} KiB")
else:
    print(f"Oh no! You're out of space.  You needed {remaining_space * -1} KB")
    print(f"  and that's {remaining_space_kibibytes * -1} Kib")
