def is_table_empty(query, table):
    if query == None:
        print(f"Populating {table}...")
        return True
    else:
        print(f"{table} is populated!")
        return False