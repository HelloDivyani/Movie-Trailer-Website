import media
import  fresh_tomatoes
toy_story = media.Movie("Toy Story","A story of a boy and his toys coming to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=JcpWXaA2qeg")
#toy_story = media.Movie()
#print(toy_story.storyLine)
avatar=media.Movie("Avatar","A marine alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyLine)
#avatar.show_trailer()
dashavatar = media.Movie("Dashavatara","The story of 10 avatars of Lord Vishnu on Earth","https://upload.wikimedia.org/wikipedia/commons/a/a0/Avatars.jpg","https://www.youtube.com/watch?v=jT22axesGn8")
hanuman=media.Movie("Hanuman","The story of God Hanuman avatar of Lord Shiva on Earth","https://upload.wikimedia.org/wikipedia/en/3/30/Hanumanfilm.jpg","https://www.youtube.com/watch?v=uHz2ng84hFE&list=RDMMuHz2ng84hFE")
ram=media.Movie("Legend of Prince Ram","The story of avatar of Lord Vishnu as Prince Ram in Ayodhya","https://upload.wikimedia.org/wikipedia/en/7/7c/Ramayana%2C_The_Legend_of_Prince_Rama.jpg","https://www.youtube.com/watch?v=0PCNGP4LbEk")
bali=media.Movie("Chotta Bheem and Throne of Bali","choota bheem and Prince Arjun fights with witch langda and saves Bali","https://upload.wikimedia.org/wikipedia/en/d/d2/Chhota_Bheem_and_the_throne_of_Bali_2013_poster.jpg","https://www.youtube.com/watch?v=H7Ht-m2QMDY")
movies = [toy_story,avatar,dashavatar,hanuman,ram,bali]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
