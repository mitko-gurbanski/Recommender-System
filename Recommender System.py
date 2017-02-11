from math import sqrt
oceniPoKorisnici={
    'Lisa Rose': {'Catch Me If You Can': 3.0 , 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck      ': 1.5,  'The Night Listener': 3.0,'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5,'Superman Returns': 3.5, 'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck      ': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My Luck      ': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane':4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck      ' : 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5, 'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5, 'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck      ': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
    }

oceniPoFilmovi = {}

def transform(): #Transformacija na Rechnik
    for person in oceniPoKorisnici:
        for film in oceniPoKorisnici[person]:
            if film not in oceniPoFilmovi:
                oceniPoFilmovi[film]={}
            oceniPoFilmovi[film][person]=oceniPoKorisnici[person][film]

def cos_similarity(people,movie1,movie2):
    si={}
    for item in people[movie1]:
        if item in people[movie2]:
            si[item]=1
    if len(si)==0:
        return 0
    sum1=0
    sum21=0
    sum22=0
    for item in si:
        sum1+=(people[movie1][item]*people[movie2][item])
        sum21+=pow(people[movie1][item],2)
        sum22+=pow(people[movie2][item],2)
    if sum21==0 or sum22==0:
        return 0

    return round(sum1/(sqrt(sum21)*sqrt(sum22)),2)

def sim_pearson(people,movie1,movie2):
    si={}
    for item in people[movie1]:
        if item in people[movie2]:
            si[item]=1
    n=len(si)
    if n==0:
        return 0
    sum1=0
    sum2=0
    sum1Sqr=0
    sum2Sqr=0
    psum=0
    for item in si:
        sum1+=people[movie1][item]
        sum2+=people[movie2][item]
        sum1Sqr+=pow(people[movie1][item],2)
        sum2Sqr+=pow(people[movie2][item],2)
        psum+=people[movie1][item]*people[movie2][item]
    broitel=psum-(sum1*sum2/n)
    imenitel=sqrt((sum1Sqr-pow(sum1,2)/n)*(sum2Sqr-pow(sum2,2)/n))

    if broitel==0:
        return 0
    return round(broitel/imenitel,2)


def sim_distance(people,movie1,movie2):
    si={}
    for item in people[movie1]:
        if item in people[movie2]:
            si[item]=1
    total = sum([pow(people[movie1][item] - people[movie2][item], 2) for item in people[movie1] if item in people[movie2]])
    return round(1/(1+sqrt(total)),2)


if __name__ == "__main__":
    transform()
    threshold=0.98
    print(oceniPoFilmovi)
    movies_watched=["You, Me and Dupree","Catch Me If You Can","Snitch"]
    print("------------------------------")
    for movie1 in movies_watched:
        print("|",movie1,"\t","|")
        print("------------------------------")
        for movie2 in sorted(oceniPoFilmovi.keys()):
            if movie1==movie2:
                continue
            if movie1 in movies_watched:
                result=cos_similarity(oceniPoFilmovi, movie1, movie2)
                if result>=threshold:
                    print(movie2 +"\t",cos_similarity(oceniPoFilmovi, movie1, movie2))
                #print(cos_similarity(oceniPoFilmovi, movie1, movie2), sim_pearson(oceniPoFilmovi, movie1, movie2),
                      #sim_distance(oceniPoFilmovi, movie1, movie2))
        print("------------------------------")



