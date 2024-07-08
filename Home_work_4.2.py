from pathlib import Path
def get_cats_info(way_to_file):
    try:
       list_of_cats = []
       way_to_file = Path(way_to_file)
       with  open (way_to_file,"r") as ph:
           for i in ph.readlines():
                list_of_cats.append({"id":i.split(",")[0],"name":i.split(",")[1],"age":i.split(",")[2][0]})
       return list_of_cats
    except FileNotFoundError:
            return []
