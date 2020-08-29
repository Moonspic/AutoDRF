# AutoDRF v0.1
Quick Api Makers for Django DRF

This mini script will create an API folder inside all te app folders that have a "models.py" in them.
the script will look into all folders that are in the same of directory of (AutoDRF.py and apply.py) and it will create standard api folders that each of which has:
1-permissions.py
2-serializers.py
3-views.py
4-urls.py
Each of those folder will import the necessary classes from each other with the right names. The names will match the created classes inside "models.py".
The current version does consider the name of app as of the folder it contains the model.
The future versions will process "config.py" for faster procesing.

The benefits of AutoDRF script:
1- it standarizes the names of classes of each of those API files.
2- It genenrates  the files automatically at no time. 

to process the apps and generate the API files:
1-places the app folders inside the folder that has "apply.py" and "AutoDRF.py"
2- run "python3 apply.py"
3-Get the api files inside each app's folder. 
4- Enjoy! 

You can do whatever customization you wish on the generated files then after. 


Also, You can uncomment the main function in AutoDRF file and run "python3 AutoDRF.py" instead.
The script is provided without any kind of direct or indirect warranty, liability or responsibility of any kind whatsoever. 
