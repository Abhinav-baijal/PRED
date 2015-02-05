def write_html(clustering,filename='display'):

    def display_images(ids):
        import image_utils
        paths = dict(zip(ids, image_utils.image_ids_to_paths(ids)))
        for id,path in paths.items():
            file.write('<a href="' + path + '"><img src="' + path + '" alt="Image ' + str(id) + '" height="100"></a>\n')

    def display_clusters(clusters):
        for k,v in clusters.items():
            file.write('<h1>'+ str(k) + '</h1>')

            display_images(v)



    file =open(filename, 'w')

    file.write(
    """<!DOCTYPE html>
    <html>
    <head>
    <title>Title of the document</title>
    </head>

    <body>
    """
    )

    display_clusters(clustering)

    file.write(
    """</body>
    </html>""")

    file.close()

def total_clustering (clusterings, prefix='display'):
    for k,v in clusterings.items():
        write_html(v,prefix+str(k)+'_clusters.html')
