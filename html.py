def write_html(clustering):

    def display_images(ids):
        import image_utils
        paths = dict(zip(ids, image_utils.image_ids_to_paths(ids)))
        for id,path in paths.items():
            file.write('<a href="' + path + '"><img src="' + path + '" alt="Image ' + str(id) + '" height="100"></a>\n')

    def display_clusters(clusters):
        for k,v in clusters.items():
            file.write('<h1>'+ str(k) + '</h1>')

            display_images(v)

    file =open('display.html', 'w')

    file.write(
    """<!DOCTYPE html>
    <html>
    <head>
    <title>Title of the document</title>
    </head>

    <body>
    The content of the document......
    """
    )

    display_clusters(clustering)

    file.write(
    """</body>
    </html>""")

    file.close()
