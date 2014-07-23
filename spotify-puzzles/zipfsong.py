#builds the album from stdin
def get_album_list():
        global top_x_songs

        lst = []
        idx = 0
        init_input = raw_input().split()
        album_length = init_input[0] #n, number of songs on the album
        top_x_songs = int(init_input[1])  #m, number of songs to display
	
        for x in range(int(album_length)):
                tup = raw_input().split()
                lst.append([int(tup[0]),tup[1]]) #3rd item used for tie-breaker in sort
                idx +=1

        return lst

def calculateQScore(lst):
        for idx, t in enumerate(lst):
                lst[idx][0] = lst[idx][0] * (idx+1)
        return lst
        

def main():
        album_list = get_album_list() #obtain the album song list from stdin
        q_list = calculateQScore(album_list) #calcualte q-scores of all songs
        sorted_list =  sorted(q_list,key = lambda song:song[0], reverse=True) #use python sorted to sort by Q-score
      	#print selected number
        for x in range(top_x_songs):
                print sorted_list[x][1]


main()
