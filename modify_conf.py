conf_file = 'docs/conf.py'

# Read the existing content of conf.py
with open(conf_file, 'r') as file:
    conf_content = file.readlines()

# Define the new content to append
latex_documents = """
latex_documents = [
    ('intro', 'fesslix.tex', 'My Project Name Documentation', 'Your Name or Organization', 'manual'),
]
"""

# Check if latex_documents is already defined to avoid duplication
if 'latex_documents' not in ''.join(conf_content):
    with open(conf_file, 'a') as file:
        file.write("\n" + latex_documents)
    print("latex_documents appended to conf.py")
else:
    print("latex_documents already present in conf.py")
