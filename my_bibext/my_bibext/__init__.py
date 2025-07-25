from .my_bibext import MyStyle

def setup(app):
    import pybtex.plugin
    pybtex.plugin.register_plugin('pybtex.style.formatting', 'mystyle', MyStyle)
    return {"version": "0.1"}
    
    
