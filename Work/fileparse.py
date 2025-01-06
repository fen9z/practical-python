# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None):
    """Parse a csv file into a list of records"""
    with open(filename) as f:
        rows = csv.reader(f)

        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            record = dict(zip(headers, row))
            records.append(record)

    return records
