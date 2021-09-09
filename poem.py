INDENTS = 4


def print_hanging_indents(poem):
    """You can use textwrap's fill but this worked better for us"""
    for part in poem.split("\n\n"):
        lines = [line.strip() for line in part.splitlines()
                 if line.strip()]
        print(lines[0])
        for line in lines[1:]:
            print(' ' * INDENTS + line)