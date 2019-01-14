import numpy as np
import matplotlib.patches as patches

def add_cluster_areas(this_ax, windfarms_geoDF, clusters, p, colors):
    alp=0.7
    i = 0
    if i in [p]:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=30000, height=65000,angle=-30, alpha=alp , fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 1
    if i in [p]:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=28000, height=60000,angle=60, alpha=alp, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 2
    if i in [p]:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=72000, height=154000,angle=35, alpha=alp-0.2, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 3
    if i in [p]:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=140000, height=164000,angle=-20, alpha=alp-0.2, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 4
    if i in [p]:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=30000, height=30000,angle=-20, alpha=alp-0.2, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)
    
    return this_ax



def add_names(windfarms_geoDF,this_ax,windfarms,ind):
    #import position_of_tex_windfarms
    FS =10
    AW = 0.1
    i=0 #AKE1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2],fontsize =FS,
                xytext=(x+8000, y-50000),arrowprops=dict(facecolor='black', shrink=0.05, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='bottom',)
    i=2 #ARD1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
                xytext=(x, y+10000),
                horizontalalignment='center', verticalalignment='bottom',)

    i=3
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS-1,
                xytext=(x+10000, y+5000),
                horizontalalignment='center', verticalalignment='bottom',)

    i=4 # Bul 1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
                xytext=(x - 5000, y+5000),
                horizontalalignment='center', verticalalignment='bottom',)

    i=5 # Bul 2
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
                xytext=(x - 15000, y-20000),
                horizontalalignment='center', verticalalignment='bottom',)

    i=6 #CR1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS-1,
                xytext=(x-12000, y-13000),
                horizontalalignment='center', verticalalignment='bottom',)

    i=7 #CRE3
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x-2500,y+1000), fontsize =FS-1,
                xytext=(x-90000, y+10000),arrowprops=dict(facecolor='black',shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='right', verticalalignment='bottom',)

    i=8
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS-1,
                xytext=(x-8000, y+40000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='bottom',)

    i=9 #GWW1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x-2000,y-2000), fontsize =FS-1,
                xytext=(x-30000, y-85000),arrowprops=dict(facecolor='black',shrink=0, width=AW, headlength=3,headwidth=4),
                horizontalalignment='center', verticalalignment='center',)

    i=10 #HAL1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=windfarms_geoDF.iloc[i]['geometry'].bounds[:2], fontsize =FS,
                xytext=(x, y+6000),#arrowprops=dict(facecolor='black', shrink=0, width=AW-0.1, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='bottom',)

    i=11 #IEW1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y+2500), fontsize =FS,
                xytext=(x, y+60000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='bottom',)

    i=12 #IEW2
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x+2000,y+2500), fontsize =FS,
                xytext=(x+7000, y+40000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='bottom',)

    i=13 #KHW
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x-2000,y), fontsize =FS-1,
                xytext=(x-90000, y+500),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='center',)

    i=14 #NEP
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y+2500), fontsize =FS-1,
                xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='center',)

    i=15 #OWF1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
        xytext=(x-55000, y-85000),arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='center',)

    i=16 #SCR2
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
            xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
            horizontalalignment='center', verticalalignment='center',)

    i=17 #SCR3
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y+2500), fontsize =FS-1,
                xytext=(x-5000, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='center',)

    i=18 #SCR4
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
                xytext=(x, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='center',)

    i=19 #TAB1
    if i in ind:
        x = windfarms_geoDF.iloc[i]['geometry'].x; y = windfarms_geoDF.iloc[i]['geometry'].y
        this_ax.annotate(windfarms['Asset ID'][i], xy=(x,y-2500), fontsize =FS-1,
                xytext=(x+5000, y+10000),#arrowprops=dict(facecolor='black', shrink=0, width=AW, headlength=3, headwidth=4),
                horizontalalignment='center', verticalalignment='center',)            
    return this_ax

def add_cluster_areas2(this_ax, windfarms_geoDF, clusters, p, colors):
    alp=0.7
    i = 0
    if i in p:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=30000, height=65000,angle=-30, alpha=alp , fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 1
    if i in p:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=28000, height=60000,angle=60, alpha=alp, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 2
    if i in p:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=72000, height=154000,angle=35, alpha=alp-0.2, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 3
    if i in p:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=140000, height=164000,angle=-20, alpha=alp-0.2, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)

    i = 4
    if i in p:
        cl = colors[i]
        xs = [windfarms_geoDF.iloc[i]['geometry'].x for i in np.where(clusters==i)]
        ys = [windfarms_geoDF.iloc[i]['geometry'].y for i in np.where(clusters==i)]
        x = (np.max(xs) + np.min(xs))/2
        y = (np.max(ys) + np.min(ys))/2
        e = patches.Ellipse(xy=[x,y], width=30000, height=30000,angle=-20, alpha=alp-0.2, fc=cl, ec=cl, lw=1, fill=True)
        this_ax.add_patch(e)
    
    return this_ax