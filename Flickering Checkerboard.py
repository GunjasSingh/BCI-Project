import psychopy.visual
import psychopy.event
import time

win = psychopy.visual.Window(
    size=[640, 640],color = -1, units="pix",fullscr=False
)
#The window on which the stimulus will appear


n = 200 #total number of tiles

tile_xys = []
tile2_xys = []

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

t=0.2; # time for delay to adjust frequency between stims A and B

#to flip between stimA and stimB
while not psychopy.event.getKeys():
	stimA.draw()
	win.flip()
	time.sleep(t)
	stimB.draw()
	win.flip()
	time.sleep(t)

win.close()
