import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[640, 640],color = -0.6, units="pix",fullscr=False
)
#The window on which the stimulus will appear

n = 200 #total number of tiles

tile2_xys = []  #for StimA
tile_xys = [] #for StimB

alternate = -1

#stimA- first checkerboard/chessboard

for i in range(0,20):
    for j in range(0,10):
        if(alternate == -1):
            tile_x = -760 + 80*i
            tile_y = -680 + 160*j
        else:
            tile_x = -760 + 80*i
            tile_y = -760 + 160*j
        tile2_xys.append([tile_x, tile_y]) 
    alternate*=(-1)


stimA = psychopy.visual.ElementArrayStim(
    win=win,units="pix",nElements=n,elementTex=None,elementMask=None,xys=tile2_xys,sizes = 80
)


#stimB- second checkerboard/chessboard

for i in range(0,20):
    for j in range(0,10):
        if(alternate == -1):
            tile_x = -760 + 80*i
            tile_y = -760 + 160*j
        else:
            tile_x = -760 + 80*i
            tile_y = -680 + 160*j
        tile_xys.append([tile_x, tile_y]) 
    alternate*=(-1)


stimB = psychopy.visual.ElementArrayStim(
    win=win,units="pix",nElements=n,elementTex=None,elementMask=None,xys=tile_xys,sizes = 80
)


frequency =10
#will only work for factors of 60 (1,2,3,4,5,6,10,12,15,20,30,(NOT 60)) - monitor rate is 60Hz


fre = int(60/frequency)
fre2 = int(fre/2)
#to flip between stimA and stimB
while not psychopy.event.getKeys():
    for frameN in range(1,61):
        if ((frameN%fre <fre2) ==1):
            stimA.draw()
            win.flip()
        else:
            stimB.draw()
            win.flip()

win.close()
