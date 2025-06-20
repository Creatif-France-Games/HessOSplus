import importlib.util
import os

def load_apps():
    apps = []
    for filename in os.listdir("apps"):
        if filename.endswith(".py"):
            name = filename[:-3]
            spec = importlib.util.spec_from_file_location(name, f"apps/{filename}")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            app_class = getattr(module, "App")
            icon = getattr(module, "get_icon")()
            apps.append({
                "name": name,
                "class": app_class,
                "icon": icon
            })
    return apps
