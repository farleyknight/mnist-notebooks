
def my_function(args):
  return f"Hello, {args['name']}"

def verify_my_function(args, output):
  return output == f"Hello, {args['name']}"