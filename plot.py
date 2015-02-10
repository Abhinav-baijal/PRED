from matplotlib import pyplot
#script to do statical analysis of the quality of output v/s input.
def consensus_quality_bar_chart(consensus_quality, original_data_quality):
    pyplot.bar(left = [0] + list(range(1,1+len(original_data_quality))),
               height = [consensus_quality] + original_data_quality,
               width = 0.6,
               color = ['red'] + ['blue']*len(original_data_quality))
    pyplot.show()
#plots a bar chart. 
def bar_chart(left,height):
    pyplot.bar(left=left,height=height)
    pyplot.show()
