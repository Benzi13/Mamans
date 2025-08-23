import ast
import importlib.util
import inspect
import sys
from types import FunctionType, MethodType

def load_module_from_path(path: str):
    spec = importlib.util.spec_from_file_location("dynamic_mod", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["dynamic_mod"] = mod
    spec.loader.exec_module(mod)
    return mod

def first_class_name_in_file(path: str) -> str | None:
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=path)
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            return node.name
    return None

def wrap_method_with_code(cls, method_name: str, code_line: str):
    original = getattr(cls, method_name)

    if isinstance(original, (FunctionType, MethodType)):
        def wrapper(self, *args, **kwargs):
            exec(code_line, globals(), locals())
            return original(self, *args, **kwargs)
        setattr(cls, method_name, wrapper)
        return

    if isinstance(original, classmethod):
        func = original.__func__
        def wrapper(cls_, *args, **kwargs):
            exec(code_line, globals(), locals())
            return func(cls_, *args, **kwargs)
        setattr(cls, method_name, classmethod(wrapper))
        return

    if isinstance(original, staticmethod):
        func = original.__func__
        def wrapper(*args, **kwargs):
            exec(code_line, globals(), locals())
            return func(*args, **kwargs)
        setattr(cls, method_name, staticmethod(wrapper))
        return

def main():
    file_name = input("Enter python file name: ").strip()
    code_line = input("Enter a python code: ").strip()

    mod = load_module_from_path(file_name)

    cls_name = first_class_name_in_file(file_name)
    if not cls_name or not hasattr(mod, cls_name):
        print("No class found in file.")
        return

    cls = getattr(mod, cls_name)

    for name, member in inspect.getmembers(cls):
        if callable(member) and not (name.startswith("__") and name.endswith("__")):
            wrap_method_with_code(cls, name, code_line)

    try:
        try:
            instance = cls()
        except TypeError:
            instance = None

        ran_any = False
        for name, member in inspect.getmembers(cls):
            if name.startswith("__") and name.endswith("__"):
                continue
            # instance method
            if instance is not None and hasattr(instance, name) and callable(getattr(instance, name)):
                try:
                    getattr(instance, name)()
                    ran_any = True
                except TypeError:
                    pass
            else:
                # classmethod / staticmethod
                attr = getattr(cls, name, None)
                if callable(attr):
                    try:
                        attr()
                        ran_any = True
                    except TypeError:
                        pass

        if not ran_any:
            print("No zero-arg methods to run for demonstration.")
    except Exception as e:
        print("Demo run failed:", e)

if __name__ == "__main__":
    main()
