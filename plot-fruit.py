import matplotlib.pyplot as plt
fig,ax=plt.subplots()
fruits=['xiaoming','xiaohong','xiaozi','xiaoqiang','xiaoluo']
counts=[25,47,80,55,32]
bar_labels=['red','blue','purple','orange','green']
bar_colors=['tab:red','tab:blue','tab:purple','tab:orange','tab:green']

ax.bar(fruits,counts,label=bar_labels,color=bar_colors)
ax.set_xlabel('participator')
ax.set_ylabel('numberofvotes')
ax.set_title('Votingstatus')
ax.legend(title='BallotColor')
plt.show()



