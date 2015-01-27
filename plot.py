from matplotlib import pyplot

def consensus_quality_bar_chart(consensus_quality, original_data_quality):
    pyplot.bar(left = [0] + list(range(1,1+len(original_data_quality))),
               height = [consensus_quality] + original_data_quality,
               width = 0.6,
               color = ['red'] + ['blue']*len(original_data_quality))
    pyplot.show()

def bar_chart(left,height):
    pyplot.bar(left=left,height=height)
    pyplot.show()
