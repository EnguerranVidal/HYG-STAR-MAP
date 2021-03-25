# HYG STAR MAP

<img src="https://user-images.githubusercontent.com/80796115/112481174-05a11700-8d77-11eb-8a1b-f5fc7d1f8d03.PNG" width="500" height="500">

 This project's goal is to create a 3D Star map from HYG ( Hypparcos satellite star survey ) data as well as eventually create a HR diagramm and other pretty plots.
 The code currently supports a Hertzsprung-Russell diagram plot as well as a 3D "bubble" function able to plot the stars around the Sun situated under a certain distance from it. This code works with CSV, NUMPY, PLOTLY and MATPLOTLIB.PYPLOT. Please try getting a working environment with these libraries implemented before attempting to run it. The following code and content is copyrighted under the MIT License ( for further details see [License.md](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/License.md) ).
 
 ## CONTENTS :
 
 The code contains the following files :
 
 - **[HYG.py](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/HYG.py)** : contains the **HYG_Map** class which handles the import of the HYG v3 database and the plotting which uses **Plotly**.
 
 - **[database.py](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/database.py)** : contains the functions used to convert the **hygdatav3.csv** file into the hygdatav3.txt file and to import the data contained in the **hygdata.txt file**.
 
 - **[hygdata_v3.csv ( Compressed version )](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/hygdata_v3.csv.gz)** : Original compressed HYG database
 
 - **[hygdatav3.csv](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/hygdatav3.csv)** : csv file of the HYG database
 
 - **[hygdatav3.txt](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/hygdatav3.txt)** : txt file of the HYG database
 
 - **[space_bubble.html](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/space_bubble.html)** : HTML file hosting the space bubble feature plotted by Plotly usage in **HYG.py**
 
 - **[HR_diagram.html](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/HR_diagram.html)** : HTML file hosting the HR diagram feature plotted by Plotly usage in **HYG.py**

## HYG DATA FORMAT :

If we look at the **[hygdatav3.txt](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/hygdatav3.txt)**, these are the labels :

**id,hip,hd,hr,gl,bf,proper,ra,dec,dist,pmra,pmdec,rv,mag,absmag,spect,ci,x,y,z,vx,vy,vz,rarad,decrad,pmrarad,pmdecrad,bayer,flam,con,comp,comp_primary,base,lum,var,var_min,var_max**

Among the labels, we mainly use "id", "hip", "hd", "hr", "gl", "bf" and "proper" to name the stars in each plots but also "x", "y", "z", "distance", "ci", "absmag" and "lum" in the HR diagram and space bu
bubble layouts.

# MAJOR UPDATES :

## UPDATE 1 : Better Looking Plots Overall

### **Changes** :
- We changed the HTML output files names so both the HR and space bubble plost can be open at the same time. 

- In  **[database.py](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/database.py)**, we added the "dat2csv" function allowing us to convert any dat file into a csv file. This will be of use if we try to use the Gaia Star survey to double our star count.

- In **[HYG.py](https://github.com/EnguerranVidal/HYG-STAR-MAP/blob/main/HYG.py)**, we changed the layouts of the HR diagram and Space Bubbleplots in order to change the hovertemplates of the labels, making them display names of the pointed stars. We also changed the background to a deep black to aid better visualisation, but we also added a size scale to the Scatter markers which displays radii values. However there seemsto be a few problems with this markers size scaleat the minutes.

### **New Issues** :

- In the space bubble feature, the size of the markers are fixed and do not interact with the overall zoom of Plotly, we would have guessed that the markers would appear bigger as we close in but they remain constant :

<img src="https://user-images.githubusercontent.com/80796115/112481136-ff129f80-8d76-11eb-84ad-86049601229b.PNG" width="500" height="500">

<img src="https://user-images.githubusercontent.com/80796115/112481153-02a62680-8d77-11eb-9698-845a827294f1.PNG" width="500" height="500">

- From the image up above, we can notice the labels show up the stars' names, however the x, y and z coordinates are still displayed which is not optimal, the spectral type or distance to the Sun would be better info to show for the user.

- In the HR diagram feature, stars with small radii show up in the red-giants section where you would usually find bigger star than in the main sequence as seen in the image below. This indicates that the radii must have been wrongly calculated. this will need to be checked.

<img src="https://user-images.githubusercontent.com/80796115/112481105-f752fb00-8d76-11eb-9aec-9dc376c06ab1.PNG" width="500" height="500">

