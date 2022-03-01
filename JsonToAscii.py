import json
import math

# Will assume that the base fields title, xtitle, ytitle and items are the only ones that are ever present.
# Under items we will assume the observed object structure is consistent i.e. we wont see an object with more than 1
# field
# Also assume all field names are strings and all values are numeric
INPUT_JSON = """
{
    "title": "stock count",
    "xtitle": "asset",
    "ytitle": "count",
    "items": [
        {"chairs": 20},
        {"tables": 5},
        {"stands": 7},
        {"lamps": 8},
        {"cups": 10},
        {"another": 4}
    ]
}
"""

# Functions

def print_title(title, graph_width):
    # Prints the title and underline, it should be centred in the graph

    top_line = ''
    next_line = ''

    if graph_width == len(title):
        # Just print title
        top_line = title
        for i in range(len(title)):
            next_line += '-'

    else:
        # need padding to ensure title is in centre
        for i in range(math.floor((graph_width - len(title)) / 2)):
            top_line = top_line + ' '
        top_line += title

        # Must also underline title
        for i in range(math.floor((graph_width - len(title)) / 2)):
            next_line += ' '

        for i in range(len(title)):
            next_line += '-'

    print(top_line)
    print(next_line)


def print_x_title(x_title):
    # Prints the x axis title, simpler as we don't need to pad anything

    title_line = x_title

    # Underlining
    next_line = ''
    for i in range(len(x_title)):
        next_line += '-'

    print(title_line)
    print(next_line)


def print_col_j_at_row(dotvalue, field_width, row_num):
    # Add the column part of each line of the columns, only needs to know whether to add a dot or not.

    out = ' '
    # Should we print a dot or not
    if dotvalue >= row_num:
        out += '*'
    else:
        out += ' '

    # Pad out each column
    for k in range(field_width - 3):
        out += ' '

    return out


def print_columns_at_line_i(i, dot_values, col_width, initial_padding):
    # Print each text line of our data columns

    line = ''

    for k in range(initial_padding):
        line += ' '

    for j in range(len(dot_values)):
        # will add to the line column by column
        line += print_col_j_at_row(dot_values[j], col_width, i)

    print(line)


def print_col_names(x_title, col_width):
    # print the column names at the bottom

    col_names_line = ''
    # add some padding for x title
    for k in range(len(x_title)):
        col_names_line += ' '

    for col_name in fields:
        col_names_line += f' {col_name}'
        # pad with space if col name shorter than max
        for i in range(col_width - len(col_name) - 2):
            col_names_line += ' '

    print(col_names_line)


def print_y_title(y_title, graph_width):
    # Prints the y axis title

    title_line = ''
    # bit of maths to centre the title
    for i in range(math.floor((graph_width - len(y_title)) / 2)):
        title_line += ' '
    title_line += y_title

    # doing the underline
    next_line = ''
    for i in range(math.floor((graph_width - len(y_title)) / 2)):
        next_line += ' '

    for i in range(len(y_title)):
        next_line = next_line + '-'

    print(title_line)
    print(next_line)


if __name__ == "__main__":
    input_data = json.loads(INPUT_JSON)

    # Insert data into fields
    title = input_data['title']
    x_title = input_data['xtitle']
    y_title = input_data['ytitle']
    items = input_data['items']
    fields = [list(item.keys())[0] for item in items]
    values = [list(item.values())[0] for item in items]

    # will make it so we see no more than 10 dots for largest value
    dot_value = max(values)/10
    dot_values = [math.floor(v/dot_value) for v in values]

    # find column width by finding longest field name and adding 2 spaces
    field_lengths = [len(f) for f in fields]
    col_width = max(field_lengths) + 2

    # Graph width
    # Title could be longer than width of all cols
    graph_width = max([(col_width * len(values)) + len(y_title) + 1, len(title)])

    # Now we build the graph starting from the top
    print_title(title, graph_width)

    print_x_title(x_title)

    # print each line of the columns
    for i in range(10,0,-1):
        print_columns_at_line_i(i, dot_values, col_width, len(x_title))

    print_col_names(x_title, col_width)

    print_y_title(y_title, graph_width)
