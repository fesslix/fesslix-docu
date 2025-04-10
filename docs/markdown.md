# Markdown Files

Whether you write your book's content in Jupyter Notebooks (`.ipynb`) or
in regular markdown files (`.md`), you'll write in the same flavor of markdown
called **MyST Markdown**.
This is a simple file to help you get started and show off some syntax.

## What is MyST?

MyST stands for "Markedly Structured Text". It
is a slight variation on a flavor of markdown called "CommonMark" markdown,
with small syntax extensions to allow you to write **roles** and **directives**
in the Sphinx ecosystem.

For more about MyST, see [the MyST Markdown Overview](https://jupyterbook.org/content/myst.html).

[cross referencing in MyST](https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#reference-roles)

## Source code

(https://www.sphinx-doc.org/en/master/usage/domains/python.html#info-field-lists)

## Sample Roles and Directives

Roles and directives are two of the most powerful tools in Jupyter Book. They
are kind of like functions, but written in a markup language. They both
serve a similar purpose, but **roles are written in one line**, whereas
**directives span many lines**. They both accept different kinds of inputs,
and what they do with those inputs depends on the specific role or directive
that is being called.

https://myst-parser.readthedocs.io/en/latest/

Here is a "note" directive:

```{note}
Here is a note
```

```{todo}
Here is a todo
```

```{warning}
Here is a warning
```

```{attention}
Here is an attention
```

```{caution}
Here is a caution
```

```{error}
Here is an error
```

```{tip}
Here is a tip
```

```{hint}
Here is a hint
```

```{important}
Here is a important
```

:::{admonition} Some title
:class: tip
Here is a admonition with a user-specific title.
:::

```{danger}
Here is a danger
```

```{seealso}
Here is a seealso
```

```python
from a import b
c = "string"
```

```{code-block} python
:caption: This is a caption
:emphasize-lines: 2,3
:lineno-start: 1

a = 1
b = 2
c = 3
```

```bash
pip install package-name
```

It will be rendered in a special box when you build your book.

Here is an inline directive to refer to a document: {doc}`markdown-notebooks`.


## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

```{bibliography}
```

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).
