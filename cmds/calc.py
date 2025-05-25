def run(args):
    if not args:
        print("Usage: calc <expression>")
        return
    try:
        expression = " ".join(args)
        result = eval(expression, {"__builtins__": {}})
        print("Result:", result)
    except Exception as e:
        print(f"Error: {e}")
