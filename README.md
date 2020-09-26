Install requests with pip:

```> python3 -m pip install requests```

If you're using Windows you should be able to just enter this and it will grab the steam install location from the registry and cycle through all users on the system.

```> python3 update-hero-grid.py```

Otherwise, you can specify:

```>python3 update-hero-grid.py -steam_install_path '/bin/steam/whatever/' -user_id '123456789'```

The tier lists will be saved with a S! prefix. Anything with an S! prefix will get deleted when this is run to allow for quick updating.

![image](https://user-images.githubusercontent.com/6697473/94332368-41ab1900-ff9a-11ea-92f5-427414b20049.png)
