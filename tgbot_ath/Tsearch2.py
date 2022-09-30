import codecs
import torrse

#print(torrse.Engines)
#engine = torrse.engine_1337x()

#all of the engines got same parameters

#query = your query
# category = category of torrent --> print(torrse.categories)
#limit = limit of torrents
#magnet = extract magnet for each torrent if True, it may be slow when you use it, also you can extract magnet after search --> torrse.get_magnet(link)

#default parameters
#search(query, category=None, limit=15, magnet=False)
#results = engine.search('dragon nest', 'movie', 30)


    #in some engines magnet links in query page so i also added it in search results (see engine_nyaa)


#also there is a function to make search in all engines

#NOTE: limit parameter for each engine
#exclude_same = exclude torrents that got same magnets
#engines = list of engines that you want to make search, ALL if you do not set parameter

#default parameters
#search(query, category=None, limit=15, magnet=False, exclude_same=True, engines=Engines)
#results = torrse.search('dear esther', 'game', 30)





def get_torrents(query):
        res=''
        results = torrse.search(query,None,  30, torrse.Engines) 

        for i in results:
            res=res+str(i)
            
        arr=res.split('name')
        for i in arr:
            res=res+'\n\n'+i

        print(res)


        text_file = codecs.open('_result.txt',"w", "utf-8")
        text_file.write(res)
        text_file.close()
        
    



        