Install requests with pip:

```> python3 -m pip install requests```

Run the program with the correct path to hero_grid_config.json (replace STEAM_INSTALL and USER_ID with the correct values):

```> python3 update-hero-grid.py -path "STEAM_INSTALL/userdata/USER_ID/570/remote/cfg/hero_grid_config.json"```

For example in Windows:

```> python3 .\update-hero-grid.py -path "C:\Program Files (x86)\Steam\userdata\XXXXXXXXX\570\remote\cfg\hero_grid_config.json"```

The tier lists will be saved with a S! prefix. Anything with an S! prefix will get deleted when this is run to allow for quick updating.

![image](https://user-images.githubusercontent.com/6697473/94332368-41ab1900-ff9a-11ea-92f5-427414b20049.png)
