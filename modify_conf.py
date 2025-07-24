conf_file = 'docs/conf.py'

# Read the existing content of conf.py
with open(conf_file, 'r') as file:
    conf_content = file.readlines()

## Define the new content to append
#latex_documents = """
#latex_documents = [
#    ('intro', 'fesslix.tex', 'Fesslix – Stochastic Analysis', 'Dr.-Ing. Wolfgang Betz', 'manual'),
#]
#"""

## Check if latex_documents is already defined to avoid duplication
#if 'latex_documents' not in ''.join(conf_content):
#    with open(conf_file, 'a') as file:
#        file.write("\n" + latex_documents)
#    print("latex_documents appended to conf.py")
#else:
#    print("latex_documents already present in conf.py")
    
######################################################################
## Create custon bib style
######################################################################

# Define the new content to append
bibstyle_documents = """
import pybtex.plugin
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.template import toplevel, sentence, field, words, href, tag
from pybtex.style.names import last_first
from pybtex.plugin import register_plugin

class ManuscriptLinkStyle(UnsrtStyle):
    def format_title(self, e):
        # If there's a 'file' field (pointing to your manuscript), make the title a link
        if 'file' in e.fields:
            return href[e.fields['file']][field('title')]
        elif 'url' in e.fields:
            return href[e.fields['url']][field('title')]
        else:
            return tag('em')[field('title')]

    def format_entry(self, entry):
        # Customize the entry format
        template = toplevel [
            self.format_names('author'),
            self.format_title(entry),
            sentence [ self.format_journal_or_booktitle(entry) ],
            sentence [ self.format_volume_and_pages(entry) ],
            self.format_year(entry),
        ]
        return template.format_data(entry)

# Register the custom style under name 'mystyle'
register_plugin('pybtex.style.formatting', 'mystyle', ManuscriptLinkStyle)
"""

# Check if latex_documents is already defined to avoid duplication
if 'ManuscriptLinkStyle' not in ''.join(conf_content):
    with open(conf_file, 'a') as file:
        file.write("\n" + bibstyle_documents)
    print("bibstyle_documents appended to conf.py")
else:
    print("bibstyle_documents already present in conf.py")
    

