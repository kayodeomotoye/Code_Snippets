import textwrap

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ))


INDENTS = 4
shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

def print_hanging_indents(poem):
    dedented_txt = textwrap.dedent(poem).strip()
    dedented_text = dedented_txt.splitlines()
    print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * INDENTS,
                    width=40,
                    ))


print_hanging_indents(shakespeare_unformatted)