Run the following commands:

```> python3 -m pip install requests```

Replace STEAM_INSTALL and USER_ID with the appropriate values and run:

```> python3 update-herogrid.py -path STEAM_INSTALL/userdata/USER_ID/570/remote/cfg/hero_grid_config.json```

The tier lists will be saved with a S! prefix. Anything with an S! prefix will get deleted when this is run to allow for quick updating.

```
usage: update-herogrid.py [-h] -path PATH

optional arguments:
  -h, --help           show this help message and exit
  -path PATH, -p PATH  Required. STEAM_INSTALL/userdata/USER_ID/570/remote/cfg/hero_grid_config.json
```

![image](https://user-images.githubusercontent.com/6697473/94150156-6b4f2d80-fe3e-11ea-9226-9ac26a25ea7e.png)