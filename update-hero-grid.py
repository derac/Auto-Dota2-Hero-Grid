import argparse, requests, json, os, datetime

parser = argparse.ArgumentParser()
parser.add_argument('-path','-p',type=str,required=True,
                    help="located at c:\\{STEAM_INSTALL_LOCATION}\\userdata\\{STEAM_USER_ID}\\570\\remote\\cfg\\hero_grid_config.json")
parser.add_argument('-verbose','-v',action="store_true",help="show debug info")
args = parser.parse_args(); parser.print_help(); print();
date_str = datetime.date.today().strftime(" %d-%m-%Y")
spec_url = 'https://stats.spectral.gg/lrg2/api/?league=imm_ranked_meta_last_7&mod=heroes-positions-position_'
spec_pos = {"Core Safelane":"1.1","Core Midlane":"1.2","Core Offlane":"1.3","Support":"0.0"}

if os.path.isfile(args.path): # open grid config and delete existing if desired
    try:
        with open(args.path) as f: grid_conf = json.load(f); print("Grid config loaded.")
        grid_conf["configs"] = [c for c in grid_conf["configs"] if "S!" != c["config_name"][:2]]
    except Exception as e: raise e
else: grid_conf = {"version":3,"configs":[]}; print("Creating new Grid Config file.")

for pos_name,pos_endpoint in spec_pos.items(): # update the grid config
    try: hero_data = json.loads(requests.get(spec_url+pos_endpoint).content)["result"][pos_endpoint]
    except Exception as e: raise e
    hero_ranks = sorted([(data["rank"],hero_id) for hero_id,data in hero_data.items()], key=lambda x:-x[0])
    pos_conf = {"config_name": 'S! ' + pos_name + date_str,
                "categories": [{"category_name":chr(65+i)+" tier - rank %s+"%(100-5*i-5),
                                "x_position":i//5*400, "y_position":(i%5)*120,"width":400,"height":100,
                                "hero_ids":[id for rank,id in hero_ranks if (100-5*i) >= rank > (100-5*i-5)]}
                               for i in range(15)]}
    grid_conf["configs"].append(pos_conf); print("Processed",pos_name+'.');
    if args.verbose: print(pos_conf)

try: # write grid conf
    with open(args.path, "w") as f: print(json.dumps(grid_conf, indent=4), file=f)
    print("Grid Config has been written.")
except Exception as e: raise e