def write_html(clustering,filename):

    def display_images(ids):
        import image_utils
        paths=image_utils.image_ids_to_paths(ids)
        for i in paths:
            file.write('<img src="' + i + '" height="100">')
           
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
    The content of the document......
    """
    )

    display_clusters(clustering)

    file.write(
    """</body>
    </html>""")
    
    file.close()
  
def total_clustering (clusterings):
    for k,v in clusterings.items():
        write_html(v,'display_'+str(k)+'_clusters.html')       
