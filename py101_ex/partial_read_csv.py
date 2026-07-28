contacts = []
with open('../sample_data/fake_address_book.csv') as f:
    f.readline()
    for line in f:
        line = line.strip()
