import csv
import os
import sqlite3
from typing import Dict


def create_db_from_csv_file(
    csv_file: str,
    sqlite_file: str,
    schema: Dict[str, str],
    skip_first_line: bool = False,
) -> None:
    """
    Create a sqlite3 database and fill it with the given CSV file.

    Example of valid schema:
    {
        'name': varchar(255),
        'address': varchar(255),
    }
    """
    # Create DB
    if os.path.isfile(sqlite_file):
        os.remove(sqlite_file)
    con = sqlite3.Connection(sqlite_file)
    cur = con.cursor()

    # Create table
    columns_array = [('"' + k + '" ' + v) for k, v in schema.items()]
    cur.execute('CREATE TABLE "scuole" (' + ", ".join(columns_array) + ");")

    # Import CSV
    f = open(csv_file)
    csv_reader = csv.reader(f, delimiter=",")
    if skip_first_line:
        next(csv_reader, None)
    cur.executemany(
        "INSERT INTO scuole VALUES (" + ",".join(["?"] * len(schema.keys())) + ")",
        csv_reader,
    )

    # Clean up
    cur.close()
    con.commit()
    con.close()
    f.close()
