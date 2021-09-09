import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    code_tags = r'<code>.*?</code>'
    pre_tags = r'<pre>.*?</pre>'

    # DOTALL is to match text wrapped over multiple lines
    # https://www.thegeekstuff.com/2014/07/advanced-python-regex/
    preserve_tags = (re.findall(code_tags, org_text) +
                     re.findall(pre_tags, org_text, re.DOTALL))

    restore_trans_code = (re.findall(code_tags, trans_text) +
                          re.findall(pre_tags, trans_text, re.DOTALL))

    for from_, to in zip(restore_trans_code, preserve_tags):
        trans_text = trans_text.replace(from_, to)

    return trans_text

