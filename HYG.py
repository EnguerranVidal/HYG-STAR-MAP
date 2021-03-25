# PROJECT DECEMBRE 2019
# PROJECT STAR MAP / HYG
# By Enguerran VIDAL

# This file contains the main class of this project.

###############################################################
#                           IMPORTS                           #
###############################################################

#-----------------MODULES
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#-----------------PYTHON FILES
from database import*

###############################################################
#                         HYG CLASS                           #
###############################################################

class HYG_Map():
    ''' StarMap created from the HYG stellar database.'''
    def __init__(self):
        try:
            txt_file='hygdatav3.txt'
            print(" Loading HYG Database ... ")
            labels,data=import_database(txt_file)
            print(" Database loaded. ")
            self.data=data
            self.labels=labels
            self.n_variables=len(labels)
            self.n_stars=len(data)
        except FileNotFoundError:
            print("'"+txt_file+"' cannot be found in the main directory !")
            raise
        self.id=self.find_label('id')
        self.hip=self.find_label('hip')
        self.hd=self.find_label('hd')
        self.hr=self.find_label('hr')
        self.gl=self.find_label('gl')
        self.bf=self.find_label('bf')
        self.proper=self.find_label('proper')

    def find_label(self,label):
        ''' Finds a possible label in the different columns of the HYG database'''
        try:
            for i in range(self.n_variables):
                if label==self.labels[i]:
                    return i
            raise NameError("The '"+str(label)+"' column cannot be found in the HYG database.")
        except NameError:
            raise

    def get_name(self,i):
        ''' Finds an useful name for a star of given index in the database.'''
        proper=self.data[i][self.proper] # Proper
        if proper!='N':
            return proper
        bf=self.data[i][self.bf] #Bayer-Flamsteed
        if bf!='N':
            return "BF "+bf
        hr=self.data[i][self.hr] # Bright Star
        if hr!='N':
            return "HR "+hr
        hd=self.data[i][self.hd] # Henry Draper
        if hd!='N':
            return "HD "+hd
        hip=self.data[i][self.hip] # Hipparcos
        if hd!='N':
            return "HIP "+hip
        else:
            return "ID "+self.data[i][self.id]
                    
    def Hertzprung_Russell(self,n,radius=True):
        ''' Plots n stars in the standard Hertzsprung-Russell.
            n --> number of stars'''
        am=self.find_label('absmag')
        ci=self.find_label('ci')
        lum=self.find_label('lum')
        abs_mag=[]
        color_index=[]
        luminosity=[]
        for i in range(self.n_stars):
            if self.data[i][am]!='N' and self.data[i][ci]!='N':
                abs_mag.append(float(self.data[i][am]))
                color_index.append(float(self.data[i][ci]))
        m=len(color_index)
        multiple=int(m/n)+1
        cis=[]
        mags=[]
        names=[]
        for i in range(m):
            if i%multiple==0:
                cis.append(color_index[i])
                mags.append(abs_mag[i])
                luminosity.append(float(self.data[i][lum]))
                names.append(self.get_name(i))
        if radius==True:
            color_index=np.array(cis)
            abs_mag=np.array(mags)
            color_index=np.array(color_index)
            luminosity=np.array(luminosity)
            temp=4600*(1/(0.92*color_index+1.7)+1/(0.92*color_index+0.62))/5778
            radius=np.sqrt(luminosity)/temp**2
            Markers=dict(color=color_index,colorscale=star_colorscale(),line_width=0,
                         cmax=2.0,cmin=-0.4,size=np.cbrt(radius*0.5))
        else:
            Markers=dict(color=color_index,colorscale=star_colorscale(),
                         line_width=0,cmax=2.0,cmin=-0.4)
        fig = go.Figure(data=go.Scatter(x=color_index,y=abs_mag,mode='markers',marker=Markers,text=names),)
        fig.update_layout(title='Hertzsprung-Russell Diagram',plot_bgcolor='rgba(0,0,0,255)',)
        fig['layout']['yaxis']['autorange'] = "reversed"
        print("Plotting Hertzsprung-Russell Diagram...")
        fig.write_html('HR_diagram.html', auto_open=True)

    def space_bubble(self,distance):
        ''' Plots the stars around the Sun contained in a "bubble" of a given radius.
            distance --> radius of the bubble'''
        am=self.find_label('absmag')
        ci=self.find_label('ci')
        x=self.find_label('x')
        y=self.find_label('y')
        z=self.find_label('z')
        d=self.find_label('dist')
        lum=self.find_label('lum')
        X=[]
        Y=[]
        Z=[]
        distances=[]
        color_index=[]
        luminosity=[]
        abs_mag=[]
        names=[]
        for i in range(self.n_stars):
            if self.data[i][x]!='N' and self.data[i][y]!='N' and self.data[i][z]!='N' and self.data[i][ci]!='N':
                if float(self.data[i][d])*3.26156<distance:
                    X.append(float(self.data[i][x])*3.26156)
                    Y.append(float(self.data[i][y])*3.26156)
                    Z.append(float(self.data[i][z])*3.26156)
                    distances.append(float(self.data[i][d])*3.26156)
                    color_index.append(float(self.data[i][ci]))
                    luminosity.append(float(self.data[i][lum]))
                    abs_mag.append(float(self.data[i][am]))
                    names.append(self.get_name(i))
        color_index=np.array(color_index)
        luminosity=np.array(luminosity)
        temp=4600*(1/(0.92*color_index+1.7)+1/(0.92*color_index+0.62))/5778
        radius=np.sqrt(luminosity)/temp**2
        Markers=dict(color=color_index,colorscale=star_colorscale(),line_width=0,
                     cmax=2.0,cmin=-0.4,size=np.sqrt(radius)+2)
        fig = go.Figure(data=go.Scatter3d(x=X,y=Y,z=Z,mode='markers',marker=Markers,text=names))
        fig.update_layout(scene = dict(xaxis = dict(nticks=6, range=[-distance,distance],backgroundcolor="rgb(0,0,0)"),
                                       yaxis = dict(nticks=6, range=[-distance,distance],backgroundcolor="rgb(0,0,0)"),
                                       zaxis = dict(nticks=6, range=[-distance,distance],backgroundcolor="rgb(0,0,0)"),),
                          width=700,margin=dict(r=20, l=10, b=10, t=10),)
        print("Plotting Space Bubble...")
        print(str(len(names))+" stars have been plotted.")
        fig.write_html('space_bubble.html', auto_open=True)
                

###############################################################
#                        FUNCTIONS                            #
###############################################################

def star_colorscale():
    ''' Returns a custom Colorscale for stars color from their color indices.'''
    C=[[0.0,'rgb(155,178,255)'],[0.0208333333333333,'rgb(158,181,255)'],[0.0416666666666666,'rgb(163,184,255)'],
       [0.0624999999999999,'rgb(170,191,255)'],[0.0833333333333332,'rgb(178,197,255)'],[0.1041666666666665,'rgb(187,204,255)'],
       [0.1249999999999998,'rgb(196,210,255)'],[0.1458333333333331,'rgb(204,216,255)'],[0.1666666666666664,'rgb(211,221,255)'],
       [0.1874999999999997,'rgb(218,226,255)'],[0.208333333333333,'rgb(223,229,255)'],[0.2291666666666663,'rgb(228,266,255)'],
       [0.2499999999999996,'rgb(233,236,255)'],[0.2708333333333329,'rgb(238,239,255)'],[0.2916666666666662,'rgb(243,242,255)'],
       [0.3124999999999995,'rgb(248,246,255)'],[0.3333333333333328,'rgb(254,249,255)'],[0.3541666666666661,'rgb(255,249,251)'],
       [0.3749999999999994,'rgb(255,247,245)'],[0.3958333333333327,'rgb(255,245,239)'],[0.416666666666666,'rgb(255,243,234)'],
       [0.4374999999999993,'rgb(255,241,229)'],[0.4583333333333326,'rgb(255,239,224)'],[0.4791666666666659,'rgb(255,237,219)'],
       [0.4999999999999992,'rgb(255,235,214)'],[0.5208333333333325,'rgb(255,233,210)'],[0.5416666666666658,'rgb(255,232,206)'],
       [0.5624999999999991,'rgb(255,230,202)'],[0.5833333333333324,'rgb(255,229,198)'],[0.6041666666666657,'rgb(255,227,195)'],
       [0.624999999999999,'rgb(255,226,191)'],[0.6458333333333323,'rgb(255,224,187)'],[0.6666666666666656,'rgb(255,223,184)'],
       [0.6874999999999989,'rgb(255,221,180)'],[0.7083333333333322,'rgb(255,219,176)'],[0.7291666666666655,'rgb(255,218,173)'],
       [0.7499999999999988,'rgb(255,216,169)'],[0.7708333333333321,'rgb(255,214,165)'],[0.7916666666666654,'rgb(255,213,161)'],
       [0.8124999999999987,'rgb(255,210,156)'],[0.833333333333332,'rgb(255,208,150)'],[0.8541666666666653,'rgb(255,205,143)'],
       [0.8749999999999986,'rgb(255,200,133)'],[0.8958333333333319,'rgb(255,193,120)'],[0.9166666666666652,'rgb(255,183,101)'],
       [0.9374999999999985,'rgb(255,168,75)'],[0.9583333333333318,'rgb(255,149,35)'],[0.9791666666666651,'rgb(255,123,0)'],
       [1.0,'rgb(255,82,0)']]
    return C



###############################################################
#                       MAIN PROGRAM                          #
###############################################################

x=HYG_Map()
x.Hertzprung_Russell(20000)
x.space_bubble(1000)
