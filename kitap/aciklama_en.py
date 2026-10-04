# English line-by-line explanations for solution code (English edition of the book).
# The Turkish data carries pre-generated notes (explain.lines); for the English edition they are produced here
# from the translated code with the same rules, so the notes always match the code that is printed.
import ast

METHODS = {
    "append": "Adds a new item to the end of the list.",
    "insert": "Inserts an item at the given position.",
    "remove": "Removes the given item from the list (or set).",
    "pop": "Removes an item and gives it back.",
    "add": "Adds a new item to the set.",
    "discard": "Removes the item from the set; no error if it isn't there.",
    "update": "Adds new key-value pairs to the dictionary or changes existing ones.",
    "write": "Writes text to the file.",
    "dump": "Writes the data to the file as JSON.",
    "sort": "Sorts the list in place.",
    "reverse": "Reverses the list in place.",
    "extend": "Adds all items of another list to the end.",
    "clear": "Empties the collection.",
    "feed": "",
}
TYPES = {int: "(integer)", float: "(decimal number)", str: "(text, str)", bool: "(boolean: True/False)"}


def _kind(node):
    if isinstance(node, ast.Constant):
        return TYPES.get(type(node.value), "")
    return {ast.List: "(list)", ast.Dict: "(dictionary: key → value)", ast.Set: "(set: no duplicates)",
            ast.Tuple: "(tuple: a group that can't be changed)", ast.ListComp: "(list built with a comprehension)",
            ast.JoinedStr: "(text built with an f-string)", ast.DictComp: "(dictionary built with a comprehension)"}.get(type(node), "")


def explain(code):
    """[{"n": line_no, "code": line, "notes": [...]}, ...]"""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
    src = code.splitlines()
    seg = lambda n: ast.get_source_segment(code, n) or ""
    short = lambda s, k=60: s if len(s) <= k else s[:k - 3] + "..."
    funcs = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    classes = {n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)}
    notes = {}
    seen_vars = set()

    def add(line, text):
        notes.setdefault(line, [])
        if text not in notes[line]:
            notes[line].append(text)

    def call_note(c, line):
        f = c.func
        if isinstance(f, ast.Name):
            if f.id == "print":
                add(line, f"`{short(seg(c))}`: prints the value in the parentheses.")
            elif f.id in funcs:
                add(line, f"`{f.id}(...)`: calls the function you defined.")
            elif f.id in classes:
                add(line, f"`{f.id}(...)`: creates a new object from the `{f.id}` class.")
        elif isinstance(f, ast.Attribute):
            obj = seg(f.value)
            extra = METHODS.get(f.attr, "")
            add(line, f"`{short(seg(c))}`: runs the `{f.attr}` method on `{short(obj, 30)}`." + (f" {extra}" if extra else ""))

    def args_text(fn):
        a = [x.arg for x in fn.args.args if x.arg != "self"]
        return ", ".join(f"`{x}`" for x in a)

    def visit(body, cls=None):
        for st in body:
            ln = st.lineno
            if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call):
                call_note(st.value, ln)
            elif isinstance(st, ast.Assign):
                t = st.targets[0]
                if isinstance(t, ast.Name):
                    if isinstance(st.value, ast.Call) and isinstance(st.value.func, ast.Name) and st.value.func.id in classes:
                        call_note(st.value, ln)
                    if t.id in seen_vars:
                        add(ln, f"`{t.id}` gets a new value: `{short(seg(st.value))}`.")
                    else:
                        k = _kind(st.value)
                        add(ln, f"Creates a variable named `{t.id}` and stores `{short(seg(st.value))}`{' ' + k if k else ''} in it.")
                        seen_vars.add(t.id)
                elif isinstance(t, ast.Tuple):
                    add(ln, f"`{seg(t)}`: the values on the right are unpacked into these variables in order.")
                    seen_vars.update(e.id for e in t.elts if isinstance(e, ast.Name))
                elif isinstance(t, ast.Subscript):
                    add(ln, f"The value at `{seg(t.value)}[...]` is replaced with `{short(seg(st.value))}`.")
                elif isinstance(t, ast.Attribute):
                    add(ln, f"The object's `{seg(t)}` attribute is set to `{short(seg(st.value))}`.")
            elif isinstance(st, ast.AugAssign):
                add(ln, f"`{seg(st)}`: updates the value of `{seg(st.target)}`.")
            elif isinstance(st, ast.Return):
                add(ln, f"The function returns `{short(seg(st.value))}` and stops here." if st.value else "The function stops here.")
            elif isinstance(st, ast.If):
                if src[ln - 1].lstrip().startswith("elif"):
                    add(ln, f"`elif`: if the conditions above were false, `{short(seg(st.test))}` is checked.")
                else:
                    add(ln, f"Condition: if `{short(seg(st.test))}` is true, the indented lines below run.")
                visit(st.body, cls)
                if st.orelse:
                    if len(st.orelse) == 1 and isinstance(st.orelse[0], ast.If) and src[st.orelse[0].lineno - 1].lstrip().startswith("elif"):
                        visit(st.orelse, cls)
                    else:
                        for i in range(st.body[-1].end_lineno, st.orelse[0].lineno):
                            if src[i - 1].strip().startswith("else"):
                                add(i, "`else`: runs if none of the conditions above were true.")
                                break
                        visit(st.orelse, cls)
            elif isinstance(st, ast.For):
                add(ln, f"Loop: each item in `{short(seg(st.iter))}` is put into `{seg(st.target)}` in turn, and the indented lines run each time.")
                visit(st.body, cls)
            elif isinstance(st, ast.While):
                add(ln, f"Loop: the indented lines repeat as long as `{short(seg(st.test))}` is true.")
                visit(st.body, cls)
            elif isinstance(st, ast.FunctionDef):
                a = args_text(st)
                if cls and st.name == "__init__":
                    add(ln, f"`__init__`: the setup method that runs automatically when a `{cls}` object is created." + (f" Parameters: {a}." if a else ""))
                elif cls:
                    add(ln, f"Defines a method (a function that belongs to the class) named `{st.name}`." + (f" Parameters: {a}." if a else ""))
                else:
                    add(ln, f"Defines a function named `{st.name}`. " + (f"Its parameters: {a}. " if a else "It takes no parameters. ")
                        + "The lines inside run only when the function is called.")
                visit(st.body, cls)
            elif isinstance(st, ast.ClassDef):
                b = [seg(x) for x in st.bases]
                add(ln, f"Defines a class (a blueprint for objects) named `{st.name}`." + (f" It inherits from the `{b[0]}` class." if b else ""))
                visit(st.body, st.name)
            elif isinstance(st, ast.Import):
                for a in st.names:
                    add(ln, f"Adds the `{a.name}` module to the program.")
            elif isinstance(st, ast.ImportFrom):
                add(ln, f"Takes {', '.join(f'`{a.name}`' for a in st.names)} from the `{st.module}` module.")
            elif isinstance(st, ast.With):
                head = src[ln - 1].strip().rstrip(":")
                add(ln, f"`{short(head)}`: opens the file; it is closed automatically when the block ends." if "open(" in head else f"`{short(head)}`: starts a block.")
                visit(st.body, cls)
            elif isinstance(st, ast.Try):
                add(ln, "`try`: the code below is attempted; if an error occurs, the program doesn't crash and the `except` part runs.")
                visit(st.body, cls)
                for h in st.handlers:
                    add(h.lineno, f"`{src[h.lineno - 1].strip().rstrip(':')}`: these lines run if this error happens.")
                    visit(h.body, cls)
                visit(st.orelse, cls); visit(st.finalbody, cls)
            elif isinstance(st, ast.Break):
                add(ln, "`break`: leaves the loop immediately.")
            elif isinstance(st, ast.Continue):
                add(ln, "`continue`: skips the rest of this round and moves to the next one.")
            elif isinstance(st, ast.Raise):
                add(ln, f"`{short(seg(st))}`: raises an error on purpose.")

    visit(tree.body)
    return [{"n": n, "code": src[n - 1], "notes": notes[n]} for n in sorted(notes)]


if __name__ == "__main__":
    import sys
    for x in explain(open(sys.argv[1]).read()):
        print(x)
