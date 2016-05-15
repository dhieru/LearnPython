import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#toy_story.show_trailer();

ddlj_movie = media.Movie("Dilwale Dulhania Le Jayenge",
                         "Raj and Simran, two young non-resident Indians, who fall in love during a vacation through Europe with their friends",
                         "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",
                         "https://www.youtube.com/watch?v=c25GKl5VNeY")

three_idiots_movie = media.Movie("3 Idiots",
                            "The film is distinctive for featuring real inventions by little-known people in India's backyards",
                            "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                            "https://www.youtube.com/watch?v=xvszmNXdM4w")

rdb_movie = media.Movie("Rang de Basanti",
                        "The story is about a British documentary filmmaker who is determined to make a film on Indian freedom fighters based on diary entries by her grandfather, a former officer of the British Indian Army",
                        "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg",
                        "https://www.youtube.com/watch?v=Dms-mPxc1SU")

andaz_apna_apna = media.Movie("Andaz Apna Apna",
                              "Two slackers competing for the affections of an heiress, inadvertently become her protectors from an evil criminal.",
                              "https://upload.wikimedia.org/wikipedia/en/1/15/Andaz_Apna_Apna.jpg",
                              "https://www.youtube.com/watch?v=fd_w7Qw8biU")

the_darkknight = media.Movie("The Dark Knight",
                               "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham",
                               "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                               "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [toy_story,ddlj_movie,three_idiots_movie,rdb_movie,andaz_apna_apna,the_darkknight]
fresh_tomatoes.open_movies_page(movies)
