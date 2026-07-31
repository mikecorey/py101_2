import sqlite3
import pandas as pd

connection = sqlite3.connect("../sample_data/chinook.db")

query = """
SELECT
    c.FirstName || ' ' || c.LastName AS customer_name,
    c.Country,
    ar.Name AS artist_name,
    al.Title AS album_title,
    t.Name AS track_name,
    ii.Quantity,
    ii.UnitPrice,
    ii.Quantity * ii.UnitPrice AS line_total,
    i.InvoiceDate
FROM customers AS c
JOIN invoices AS i
    ON c.CustomerId = i.CustomerId
JOIN invoice_items AS ii
    ON i.InvoiceId = ii.InvoiceId
JOIN tracks AS t
    ON ii.TrackId = t.TrackId
JOIN albums AS al
    ON t.AlbumId = al.AlbumId
JOIN artists AS ar
    ON al.ArtistId = ar.ArtistId;
"""

sales = pd.read_sql_query(query, connection)
print(sales)