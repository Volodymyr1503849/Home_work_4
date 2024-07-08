from pathlib import Path
def total_selery (way_to_file):
    try:
        way_to_file = Path(way_to_file)
        total_selery=0  
        with open (way_to_file,"r") as ph:
            list_of_users = ph.readlines()
            for users in list_of_users:
                total_selery += int(users.split(",")[1])
            average_selery = total_selery / len(list_of_users)
            return (total_selery,average_selery)
    except FileNotFoundError:
            return ()
