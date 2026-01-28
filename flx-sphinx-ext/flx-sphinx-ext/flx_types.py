from docutils import nodes
from sphinx.domains import ObjType
from sphinx.domains.python import PyClasslike, PyXRefRole
from sphinx.locale import _


class PyTypeLike(PyClasslike):
    """Behaves like py:class but renders as 'type'."""

    def get_signature_prefix(self, sig):
        return [nodes.Text("type ")]

    def get_index_text(self, modname, name_cls):
        return _("type %s") % name_cls[0]


def setup(app):
    domain = app.registry.domains["py"]

    # Directive: .. py:type::
    domain.directives["type"] = PyTypeLike

    # Object type → separate index category
    domain.object_types["type"] = ObjType(
        _("type"),   # index label
        "type",      # role name
    )

    # IMPORTANT: register role *inside* Python domain
    domain.roles["type"] = PyXRefRole()

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
