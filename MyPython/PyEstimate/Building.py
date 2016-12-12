import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig3 = plt.figure()
fig3.suptitle('COMMUNITY CENTRE AT TALIPADA BAUNSUNI',fontsize = 14,fontweight = "bold")
ax3 = fig3.add_subplot(111, aspect='equal')
fig3.subplots_adjust(top= 0.9)

ax3.set_title('window sill level plan')
ax3.set_xlabel('\n\nJunior Engineer\tAssistant Engineer\tBlock Development Officer',fontsize = 10)
for p in [
    patches.Rectangle(
        (0.2233, 0.05), 6.1/15,.38/15,
        hatch='//',
        fill = False
    ),
    patches.Rectangle(
        (0.2233, 0.05+(3.65-0.38)/15), 6.1/15,.38/15,
        hatch='//',
        fill = False
    ),
    
    patches.Rectangle(
        (0.05, 0.05), 2.6/15, 3.65/15,
        
        fill=False
    ),
    patches.Rectangle(
        (0.05, 0.05), 0.25/15, 0.25/15,
        
        facecolor = "black"
    ),
    patches.Rectangle(
        (0.05, 0.05+(3.65-.25)/15), 0.25/15, 0.25/15,
        
        facecolor = "black"
    ),
    patches.Rectangle(
        (0.05+10.78/15, 0.05), 0.25/15, 0.25/15,
        
        facecolor = "black"
    ),
    patches.Rectangle(
        (0.05+10.78/15, 0.05+(3.65-.25)/15), 0.25/15, 0.25/15,
        
        facecolor = "black"
    ),
    patches.Rectangle(
        (0.2233, 0.05), 0.38/15, 1.225/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (8.32/15+.05, 0.05), 0.38/15, 1.225/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (0.2233, 2.425/15+0.05), 0.38/15, 1.225/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (8.32/15+.05, 2.425/15+0.05), 0.38/15, 1.225/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (8.32/15+.05+.38/15, 0.46/15+0.05), 2.33/15, 0.25/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (8.32/15+.05+.38/15, 3.2/15-0.25/15+.05), 2.33/15, 0.25/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (10.78/15+.05, 0.46/15+0.05),  0.25/15,2.74/15,
        hatch='//',
        fill=False
        ),
    patches.Rectangle(
        (.05, 0.4),  11.03/15,0.6/15,
        
        fill=False
        ),
    patches.Rectangle(
        (.05, 0.4+(2.7/15)),  2.6/15,(3.15-2.1)/15,
        
        fill=False
        ),
    patches.Rectangle(
        (.05, 0.4+(3.15+0.6)/15),  11.03/15,0.25/15,
        hatch ='-',
        fill=False
        ),
    patches.Rectangle(
        (.05+2.6/15, 0.4+.6/15),  8.43/15,3.15/15,
        
        fill=False
        ),
    patches.Rectangle(
        (0.05, 0.4), 0.25/15, 2.7/15,
        
        facecolor = "black"
    ),
    patches.Rectangle(
        (0.05+10.78/15, 0.4), 0.25/15, (3.15+0.6)/15,
        
        facecolor = "black"
    ),
    patches.Rectangle(
        (.05+(2.6+2.65)/15, .05),  1.2/15,0.38/15,
        hatch ='--',
        facecolor = "white"
        ),
    patches.Rectangle(
        (.05+(2.6+2.65)/15, .05+(3.65-.38)/15),  1.2/15,0.38/15,
        hatch ='--',
        facecolor = "white"
        ),
    #window in elevation
    patches.Rectangle(
        (.05+(2.6+2.65)/15, .4+(.6+1.2)/15),  1.2/15,1.2/15,
        
        facecolor = "white"
        ),
    
    
    
]:
    ax3.add_patch(p)
    ax3.axis([0,0.85,0,0.7])
fig3.savefig('rect3.png', dpi=90, bbox_inches='tight')







