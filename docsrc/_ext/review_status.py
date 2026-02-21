import importlib


def setup(app):
    app.connect("autodoc-process-docstring", add_review_status)
    return {"version": "1.0", "parallel_read_safe": True}


def add_review_status(app, what, name, obj, options, lines):
    if what != "module":
        return

    try:
        module = importlib.import_module(name)
        reviewed = getattr(module, "__reviewed__", None)
    except (ImportError, AttributeError):
        reviewed = None

    if reviewed:
        badge = f".. note:: ✓ Reviewed: {reviewed}"
        lines.insert(0, "")
        lines.insert(0, badge)
        lines.insert(0, "")
