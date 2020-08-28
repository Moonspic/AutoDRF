# AutoDRF
Quick Api Makers for Django DRF

This mini script will create API folder inside all app folders that has "models.py" in it.
the script will look into all folders that are in the same of directory of (AutoDRF.py and apply.py) and create standard api folders that has:
1-permissions.py
2-serializers.py
3-views.py
4-urls.py
and get the import from each other with the right names. The names will match the models inside "models.py".
The current version does consider the name of app as of the folder it contains the model. 
The future versions will process "config.py" for faster procesing.

The benefits of this AutoDRF:
1- it standarize the names of classes of the API.
2- It genenrate the files automatically at no time. 

to process the apps:
1-places the app folders inside the folder that has "apply.py" and "AutoDRF.py"
2- run "python3 apply.py"
3-Get the api files inside each app's folder. 
4- Enjoy! 

You can do whatever customization you wish on the generated files. 


or You can uncomment the main function in AutoDRF and run "AutoDRF.py" 
The script is provided without any kind of direct or indirect warranty, liability or responsibility of any kind whatsoever. 
