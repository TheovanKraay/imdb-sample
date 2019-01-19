from imdbpie import Imdb
imdb = Imdb()
#imdb = Imdb(anonymize=True)
import json
import pandas as pd
import numpy

#read movie data (movies.dat must be in the local directory)
moviesDF = pd.read_table('movies.dat', sep='::', comment='#', header=None)

#create a list to store the movie ratings
list = []

print("Getting movie certifications...")
#iterate over movies list
for index, row in moviesDF.iterrows():

    #substring to year
    year = row[0][-5:-1]

    #substring to film
    film = row[0][:-6]

    #search for the film
    movies = imdb.search_for_title(film)

    #iterate over items that match the title search
    for movie in movies:
        #match on the specified year
        if movie['year'] == year:
            id = movie['imdb_id']

            #break out of the loop when year matches
            break

    #get the exact title from IMDB by ID        
    title = imdb.get_title_auxiliary(id)

    #get the movie certificate
    cert = title['certificate'] 
    cert = cert['certificate'] 
    
    print (film)
    print (cert)
    #append the certificaton to the list
    list.append(cert)

#add the ratings list as column to the dataframe
moviesDF[2] = list

#add to file    
print("Adding to file...")
moviesDF.to_csv(r'movies_output.txt', header=None, index=None, sep='=', mode='a')

print("Complete!")

    


