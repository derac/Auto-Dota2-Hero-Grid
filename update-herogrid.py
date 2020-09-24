import argparse, requests, json, winreg
from datetime import date
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('-overwrite','-o',action="store_true",help="Delete saved hero grids.")
parser.print_help(); print(); args = parser.parse_args()

date_str = date.today().strftime(" %d-%m-%Y")
spec_url = 'https://stats.spectral.gg/lrg2/api/?pretty&league=imm_ranked_meta_last_7&mod=heroes-positions-position_'
spec_positions = {"Core Safelane":"1.1","Core Midlane":"1.2","Core Offlane":"1.3","Support":"0.0"}
rank_cutoffs = [100,97,93,90,85,80]

# get path to the grid config
try:
    steam_path = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\WOW6432Node\Valve\Steam"), "InstallPath")[0]
    grid_conf_path = steam_path + '\\userdata\\62756100\\570\\remote\\cfg\\hero_grid_config.json'
except: print("Couldn't get steam path from the registry to get the hero grid config file path.")

# open grid config and delete existing if desired
try:
    with open(grid_conf_path) as f: grid_conf = json.load(f)
    if args.overwrite: grid_conf["configs"] = []
except: print("Couldn't load the grid config.")

# update the grid config with each position's data from spectral.gg
for pos_name,pos_endpoint in spec_positions.items():
    try: hero_data = json.loads(requests.get(spec_url+pos_endpoint).content)["result"][pos_endpoint]
    except: print("Failed to load data from spectral.gg"); quit()
    hero_ranks = [(data["rank"],hero_id) for hero_id,data in hero_data.items()]
    hero_ranks.sort(key=lambda x:-x[0])
    pos_conf = {"config_name": pos_name + date_str,
                "categories": [{"category_name":"Rank %s+"%rank_cutoffs[i+1],
                                "x_position":0, "y_position":i*120,"width":1000,"height":100,
                                "hero_ids":[id for rank,id in hero_ranks if rank_cutoffs[i] >= rank > rank_cutoffs[i+1]]}
                               for i in range(5)]}
    grid_conf["configs"].append(pos_conf)

# write grid conf
try:
    with open(grid_conf_path, "w") as f: print(json.dumps(grid_conf, indent=4), file=f)
    print("Grid Config has been written.")
except: print("Couldn't print the grid config.")
