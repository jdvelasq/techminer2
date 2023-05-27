from ._items2counters import items2counters


def add_counters(
    column,
    name,
    directory,
    database,
    table,
    start_year,
    end_year,
    **filters,
):
    new_column_names = items2counters(
        column=column,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    table[name] = table[name].map(new_column_names)
    return table
