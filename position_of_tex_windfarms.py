FS =10
AW = 0.1
i=0
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2],fontsize =FS,
            xytext=(x-0, y-50000),arrowprops=dict(facecolor='black', shrink=0.05, width=AW, headlength=4, headwidth=7),
            horizontalalignment='center', verticalalignment='bottom',)
i=2
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
            xytext=(x, y+10000),
            horizontalalignment='center', verticalalignment='bottom',)

i=3
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS-1,
            xytext=(x+10000, y+5000),
            horizontalalignment='center', verticalalignment='bottom',)

i=4 # Bul 1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
            xytext=(x - 5000, y+5000),
            horizontalalignment='center', verticalalignment='bottom',)

i=5 # Bul 2
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
            xytext=(x - 5000, y+5000),
            horizontalalignment='center', verticalalignment='bottom',)

i=6 #CR1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS-1,
            xytext=(x-12000, y-13000),
            horizontalalignment='center', verticalalignment='bottom',)

i=7 #CRE3
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x-2500,y+1000), fontsize =FS-1,
            xytext=(x-90000, y+10000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='right', verticalalignment='bottom',)

i=8
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS-1,
            xytext=(x-8000, y+40000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='bottom',)

i=9 #GWW1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x-2000,y-2000), fontsize =FS-1,
            xytext=(x-40000, y-100000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=10 #HAL1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
            xytext=(x, y+6000),#arrowprops=dict(facecolor='black', shrink=0, width=AW-0.1, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='bottom',)

i=11 #IEW1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y+2500), fontsize =FS,
            xytext=(x, y+60000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='bottom',)

i=12 #IEW2
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x+2000,y+2500), fontsize =FS,
            xytext=(x+7000, y+40000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='bottom',)

i=13 #KHW
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x-2000,y), fontsize =FS-1,
            xytext=(x-90000, y+500),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=14 #NEP
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y+2500), fontsize =FS-1,
            xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=15 #OWF1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
            xytext=(x-60000, y-100000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=16 #SCR2
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
            xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=17 #SCR3
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y+2500), fontsize =FS-1,
            xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=18 #SCR4
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
            xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

i=19 #TAB1
x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
            xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

