# HYG STAR MAP
 This project's goal is to create a 3D Star map from HYG ( Hypparcos satellite star survey ) data as well as eventually create a HR diagramm and other pretty plots.
 The code currently supports a Hertzsprung-Russell diagram plot as well as a 3D "bubble" function able to plot the stars around the Sun situated under a certain distance from it.
 
 The code contains the following files :
 
 - **HYG.py** : contains the **HYG_Map** class which handles the import of the HYG v3 database and the plotting which uses **Plotly**.
 
 - **database.py** : contains the functions used to convert the **hygdatav3.csv** file into the hygdatav3.txt file and to import the data contained in the **hygdata.txt file**.
 
 - **hygdata_v3.csv** ( RAR version ) : Original Winrar compressed HYG database
 
 - **hygdatav3.csv** : csv file of the HYG database
 
 - **hygdatav3.txt** : txt file of the HYG database
 
 - **first_figure.html** : HTML file hosting the figure plotted by Plotly usage in **HYG.py**


# HYG DATA FORMAT :

If we look at the **hygdatav3.txt**, these are the labels :

**id,hip,hd,hr,gl,bf,proper,ra,dec,dist,pmra,pmdec,rv,mag,absmag,spect,ci,x,y,z,vx,vy,vz,rarad,decrad,pmrarad,pmdecrad,bayer,flam,con,comp,comp_primary,base,lum,var,var_min,var_max**

The ones which are interesting for us here are "absmag", "ci", "x", "y" and "z" for our HR diagramm and our space 3D star ap bubble.

# PREREQUISITES :

This code works with csv, Numpy, Plotly and Matplotly. Please try to get a working environment with these libraries put in before running it.
