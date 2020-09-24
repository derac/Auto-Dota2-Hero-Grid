Install requests with pip:

```> python3 -m pip install requests```

Run the program with the correct path to hero_grid_config.json (replace STEAM_INSTALL and USER_ID with the correct values):

```> python3 update-hero-grid.py -path "STEAM_INSTALL/userdata/USER_ID/570/remote/cfg/hero_grid_config.json"```

For example:

```> python3 .\update-hero-grid.py -path "C:\Program Files (x86)\Steam\userdata\XXXXXXXXX\570\remote\cfg\hero_grid_config.json"```

The tier lists will be saved with a S! prefix. Anything with an S! prefix will get deleted when this is run to allow for quick updating.

![image](https://user-images.githubusercontent.com/6697473/94150156-6b4f2d80-fe3e-11ea-9226-9ac26a25ea7e.png)