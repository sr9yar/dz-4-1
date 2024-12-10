import json



def get_data() -> dict:
  purchases = {}
  with open("purchase_log.txt", "r") as file:
    for line in file:
      purchase = json.loads(line)
      purchases[purchase["user_id"]] = purchase["category"]
  return purchases



def main() -> None:
  purchases = get_data()
  for key in purchases.keys():
    print(f"{key} '{purchases[key]}'")



main()
