import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
fig.suptitle('CONSTRUCTION OF CEMENT CONCRETE ROAD FROM SANKARA TO KHAIRAPADA',fontsize = 14,fontweight = "bold")
ax3 = fig.add_subplot(111, aspect='equal')
fig.subplots_adjust(top= 1.2)

ax3.set_title('Estimated Cost:-Rs. 2,00,000.00         Head of Account:-Biju K.B.K.(2016-17)')
ax3.set_xlabel('\n\nJunior Engineer\tAssistant Engineer\tBlock Development Officer',fontsize = 10)
for p in [
    patches.Rectangle(
        (0.675, 0.6), 3.65,0.1,
        
        fill = False
    ),
    patches.Rectangle(
        (0.675+.2, 0.5), 3.65-.4,0.1,
        
        fill = False
    ),
    patches.Rectangle(
        (0.675, 0.3), 0.2,0.3,
        
        fill = False
    ),
    patches.Rectangle(
        (0.675+3.65-.2, 0.3), 0.2,0.3,
        
        fill = False
    ),
    patches.Rectangle(
        (0.675+.2, 0.45), 3.65-.4,0.05,
        
        fill = False
    ),
    patches.Rectangle(
        (0.675+3.65, 0.45), .675,0.25,
        
        fill = False
    ),
    patches.Rectangle(
        (0, 0.45), 0.675,0.25,
        
        fill = False
    ),
 ]:
    ax3.add_patch(p)
    ax3.axis([0,5.0,0,1.0])
    ax3.text(0.1,0.5,'Earth Work',fontsize = 8)
    ax3.text(.675+3.65+.1,0.5,'Earth Work',fontsize = 8)
    ax3.text(.675+1,0.62,'C.C. (1:2:4) using 12mm size c.b.g. chips',fontsize = 6)
    ax3.text(.675+1,0.52,'C.C. (1:3:6) using 40mm size c.b.g. metal',fontsize = 6)
    ax3.text (0.695,.3,'cut-off',verticalalignment='bottom',fontsize = 8)
fig.savefig('ccroadss.png', dpi=90, bbox_inches='tight')




