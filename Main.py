import csv 

def Parse_WWindows_Firewall(file_path):
    rules = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rule = {
                "name": row[0],
                "display_name": row[1],
                "enabled": row[2],
                "direction": row[3],
                "action": row[4],
                "profile": row[5],
                "interfaces": row[6],
            }
            rules.append(rule)
    return rules    

rules = Parse_WWindows_Firewall("firewall_rules.csv")
print(rules[0])