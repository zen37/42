
def union(*args) -> set:
    result = set()
    for arg in args:
        result.update(arg)
    return result

def intersect(*args) -> set:
    if not args:
        return set()
    
    result = set(args[0])
    for arg in args[1:]:
        result.intersection_update(arg)  # Modify result in place by intersecting with each subsequent set
    return result

if __name__ == "__main__":
    x = union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
    print(x)
    y = intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
    print(y)

from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    result = selector(data)
    for func in filters:
        result = func(result)
    return result



def select(*columns: str) -> ModifierFunc:
    """
    Return function that selects only specific columns from dataset

    :param columns: column names to select
    :return: function that selects columns
    """
    def selector(data: DataType) -> DataType:
        """
        Select columns from dataset

        :param data: List of dictionaries with columns and values
        :return: List of dictionaries with selected columns
        """
        return [{column: row[column] for column in columns} for row in data]

    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return function that filters specific column to be one of `values`

    :param column: column name to filter
    :param values: allowed values for the column
    :return: function that filters dataset
    """
    def filter_func(data: DataType) -> DataType:
        """
        Filter dataset based on column and values

        :param data: List of dictionaries with columns and values
        :return: Filtered list of dictionaries
        """
        return [row for row in data if row.get(column) in values]

    return filter_func


def test_query():
    friends = [
        {'name': 'John', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Jane', 'gender': 'female', 'sport': 'Cricket'}
    ]
    
    value = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', *('Basketball', 'Cricket')),
        field_filter('gender', *('male',)),
    )
    assert [{'gender': 'male', 'name': 'John', 'sport': 'Basketball'}] == value
    

if __name__ == "__main__":
    test_query()