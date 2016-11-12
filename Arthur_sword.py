import matplotlib.pyplot as plt
fig =plt.figure()
fig.suptitle('Arthur and the Sword',fontsize =14,fontweight='bold')
ax =fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Hard words & their meaning')
ax.text(.05,.8,'apparently:(adverb), as far as one knows or can see.',style = 'italic',
        bbox = {'facecolor':'red','alpha':0.9,'pad':5})
ax.text(.05,.6,'''knight:(noun):A knight is a person granted an honorary title of
knighthood by a monarch''',style = 'italic',
        bbox = {'facecolor':'blue','alpha':0.5,'pad':5})
ax.text(.05,.72,'rage:(noun)= a violent uncontrollable anger..',style = 'italic',
        bbox = {'facecolor':'green','alpha':0.7,'pad':5})

ax.text(.05,.5,'''resolve:(verb) =settle or find a solution to (a problem or
contentious matter).''',style = 'italic',
        bbox = {'facecolor':'yellow','alpha':0.7,'pad':5})
ax.text(.05,.4,'''Archbishop:(noun) =In Christianity, an archbishop
 is a bishop of higher rank or office..''',style = 'italic',
        bbox = {'facecolor':'grey','alpha':0.7,'pad':5})
ax.text(.05,.3,'''Cathedral:(noun) =A cathedral, is a Christian church
which contains the seat of a bishop,''',style = 'italic',
        bbox = {'facecolor':'pink','alpha':0.9,'pad':5})
ax.text(.05,.2,'''solemn:(adjective) =formal and dignified.
characterized by deep sincerity''',style = 'italic',
        bbox = {'facecolor':'violet','alpha':0.9,'pad':5})
ax.text(.05,0.1,'''anvil:(noun)=an iron block on which pieces of metal
    are hammered into shape''',style = 'italic',
        bbox = {'facecolor':'orange','alpha':0.9,'pad':5})




ax.axis([0,1,0,1])
plt.show()
