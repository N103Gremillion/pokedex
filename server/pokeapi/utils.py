def print_pretty_json(data) -> None:
  import json
  print(json.dumps(data, indent=4))