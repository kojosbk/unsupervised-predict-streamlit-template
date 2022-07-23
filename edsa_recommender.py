"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import base64
from  PIL import Image
from streamlit_option_menu import option_menu

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Changing the background
# import base64

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# set_png_as_page_bg('resources/imgs/newbg.png')
set_bg_hack('resources/imgs/MISSION STATEMENT (4).png')
logo = Image.open('resources\imgs\logosidebar-removebg-preview.png')
st.sidebar.image(logo, use_column_width=True)
# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    st.sidebar.title("Pages")
    page_options = ["Home","Exploratory Data Analysis(EDA)","Recommender System","Solution Overview","Business Pitch","About"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    if page_selection == "Solution Overview":
        title_SO = """
	    <div style="background-color:#eebd8a;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Solution Overview</h1>
        """
        st.markdown(title_SO, unsafe_allow_html=True)
        #st.title("Solution Overview")
        st.image('resources/imgs/Sol.jpeg',use_column_width=True)
        st.write("Describe your winning approach on this page")
        st.write("Our objective was to construct a recommendation algorithm based on the content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed based on their historical preferences. We used a special version of the MovieLens dataset. Below is a description of the dataset we used")
        st.write("genome_scores - a score mapping the strength between movies and tag-related properties")
        st.write("genome_tags - user assigned tags for genome-related scores")
        st.write("imdb_data - Additional movie metadata scraped from IMDB using the links.csv file")
        st.write("links - File providing a mapping between a MovieLens ID and associated IMDB and TMDB IDs")
        st.write("tags - User assigned for the movies within the dataset")
        st.write("test - The test split of the dataset. Contains user and movie IDs with no rating data")
        st.write("train - The training split of the dataset. Contains user and movie IDs with associated rating data")
        st.write("The initial step was the data preprocessing and we looked for missing values. We discovered that there are missing values in three of the eight datasets we have.")
        st.write("After data preprocessing we started building our based model. We built five different collaborative base models, namely SVD, Normal Predictor, CoClustering, KNN Baseline, and lastly NMF. Their performances were compared using a statistical measure known as the root mean square error (RMSE), which determines the average squared difference between the estimated values and the actual value. A low RMSE value indicates a high model accuracy. The best performing base models were SVD and KNN Baseline.\n\nWe performed hyperparameter tuning on SVD and it gave us the best result of Kaggle.")

        imdb = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h3 style="color:black;text-align:left;">Cleaning the imdb_data dataset</h3>
        """
        st.markdown(imdb, unsafe_allow_html=True)
        st.write('We imputed the runtime with the mean runtime\n\nCreated a list plot keywords for each movie.\n\nCreated a list of title casts for each movie.')

        movies = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h3 style="color:black;text-align:left;">Cleaning the movies dataset</h3>
        """
        st.markdown(movies, unsafe_allow_html=True)
        st.write('Created a list of genres in every movie in the movies column\n\nAdded the releasea_year column.')

        st.write('After cleaning the data, we then merged the data')
        st.write('We proceeded to the second step, the EDA. We constructed various plots using our data and gathered insights from our data, these are well documented on our Exploratory Data Analysis(EDA) page.')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # Home
    if page_selection == "Home":
        st.image('resources/imgs/EDSA_logo.png',use_column_width=True)

        html_temp = """
	    <div style="background-color:{};padding:10px;border-radius:10px;margin:10px;border:3px; border-style:solid; border-color:#eebd8a; padding: 1em;">
	    <h1 style="color:{};text-align:center;">UNSUPERVISED PREDICT</h1>
	    </div>
	    """
        
        title_temp = """
	    <div style="background-color:#eebd8a;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Recommender System</h1>
	    <h2 style="color:black;text-align:center;">Team:JM4</h2>
	    <h2 style="color:black;text-align:center;">JM Data Intelligence</h3>
	    </div>
	    """
        st.markdown(html_temp.format('#D2691E00','black'), unsafe_allow_html=True)
        st.markdown(title_temp, unsafe_allow_html=True)
    

    # EDA
    if page_selection == "Exploratory Data Analysis(EDA)":
        with st.sidebar:
            choose = option_menu("EDA", ["Ratings","Movies","Directors",'Genres','Title Cast'],
                                icons=['tropical-storm', 'tree', 'kanban', 'bar-chart-steps','bezier', 'alt','bezier2'],
                                menu_icon="app-indicator", default_index=0,
                                styles={
                "container": {"padding": "5!important", "background-color": "#f1f2f6"},
                "icon": {"color": "#eebd8a", "font-size": "25px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#585858"},		
                    }
                    )
        title_eda = """
	    <div style="background-color:#eebd8a;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Exploratory Data Analysis(EDA)</h1>
        """
        st.markdown(title_eda, unsafe_allow_html=True)
        
    

        if choose == "Ratings":
            st.image('resources/imgs/EDA6.png',use_column_width=True)

            op_ratings = st.radio("Choose an option under ratings",("Top 20 users by number of ratings","Rating distribution","Relationship between the number of ratings a movie has and how highly it is rated"))

            if op_ratings == "Top 20 users by number of ratings":
                #if rating_option == "Top 10 users by number of ratings":
                st.image('resources/imgs/top_20rev.png',use_column_width=True)
                st.write('When we look at the top 20 users by the number of ratings, we can see that user 72315 is an outlier in that he or she has rated a disproportionately high number of films compared to the other users, with a difference of 9272 ratings between user 12952 and user 80974. As a result, our recommendation system "better knows" user 72315 and his or her preferences, making it simple for it to suggest films to them.')
            if op_ratings == "Relationship between the number of ratings a movie has and how highly it is rated":
                #if rating_option == "Top 10 users by number of ratings":
                st.image('resources/imgs/corr_rat_count.png',use_column_width=True)
                st.write('The scatter plot above indicates that the more ratings a film has, the more likely it is to obtain a high rating. This confirms our instinctive notion that films with better ratings tend to get more referrals from viewers. In other words, most people try to steer clear of negative comments.')
            
            # if op_ratings == "Top 10 users by number of ratings(No outlier)":
            # #if rating_option == "Top 10 users by number of ratings(No outlier)":
            #     st.image('resources/imgs/rating_no_outlier.png',use_column_width=True)
            #     st.write("Removing the outlier user 72315 we see that the rest of users have not rated an extreme number of movies comapred to each other.Now that we've looked into the number of ratings for each user, we can now investigate the distribution of ratings")
            #     st.write("Most review sites use a 1 to 5 star rating system, with")
            #     st.write("5 star : Excellent\n\n4.0 – 5.0 stars : Positive Reviews\n\n3.0 - 3.9 stars : Neutral Reviews\n\n1.0 - 2.9 star : Negative Reviews")
            if op_ratings == "Rating distribution":
            #if rating_option == "Rating distribution":
                st.image('resources/imgs/Ratings dist.png',use_column_width=True)
                st.write("When we look at the distribution of ratings, we can see that 4.0 is the most popular rating, making up 27% of all ratings, which suggests that most users have found most films to be good but not excellent—although no film can truly be excellent. The second most popular rating is 3.0, which indicates that many users have found the films they've seen to be neutral.")
                st.write("It's interesting to observe that the ratings are skewed to the left here, with more ratings on the right side of the bar graph. This might be due to the fact that individuals only prefer to review movies they enjoy, since they wouldn't bother to stay to the finish or score one they didn't like.")
                st.write("We can observe that the average movie rating is 3.5, indicating that the skewed distribution indicates that we have more neutral and favorable reviews.")

        if choose == "Movies":
           
            st.image('resources/imgs/predict bg.png',use_column_width=True)
            op_movies = st.radio("Choose an option under movies",("Top 20 most rated movies of all time","First Twenty Years with the Highest Numbers of Movies produced"))

            if op_movies == "Top 20 most rated movies of all time":
                st.image('resources/imgs/Top Twenty Rated Movies.png',use_column_width=True)
                st.write("Unsurprisingly, Shawshank Redemption, a 1994 American drama film written and directed by Frank Darabont, holds the record for highest box office gross. It is based on the 1982 Stephen King novel Rita Hayworth and Shawshank Redemption. Other timeless classics include The Matrix, which not only won 41 awards but also helped to define action filmmaking in the twenty-first century.\n\nHollywood's handling of action sequences was altered by The Matrix, which also helped to popularize the bullet time special effect. This method is used in the film's most famous moment, which leaves us in awe as Neo maneuvers his body to avoid an enemy's bullets while dodging their fire.\n\nIt's fascinating to observe that 21 of the top 25 movies of all time, or 84 percent of them, were published before the year 2000. Might this signify that people no longer rate movies, or could it just be because these films were produced so long ago that their rating counts have accumulated over time?\n\nFinding the highest-rated films of the twenty-first century is motivated by the discovery that 84% of the titles in our 20 most popular films were released before 2000.")
                test = '''<p float="left"><img src="https://www.themoviedb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg" width="200" height = 300/><img src="https://cdn.europosters.eu/image/750/posters/pulp-fiction-group-i1295.jpg" width="200" height = 300/>
                <img src="https://cps-static.rovicorp.com/2/Rights%20Managed/Belgacom/Forrest%20Gump/_derived_jpg_q90_310x470_m0/ForrestGump_EN.jpg" width="200" height = 300/></p>
                \n\n**Top three Most Rated Movies**\n- Shawshank Redemption (1994)<a href="https://www.youtube.com/watch?v=NmzuHjWmXOc&ab_channel=RottenTomatoesClassicTrailers"> Watch trailer</a>
                    \n- Pulp Fiction (1994)<a href="https://www.youtube.com/watch?v=s7EdQ4FqbhY&ab_channel=Movieclips"> Watch trailer</a>
                    \n- Forrest Gump (1994)<a href="https://www.youtube.com/watch?v=bLvqoHBptjg&ab_channel=ParamountMovies"> Watch trailer</a>'''
                st.markdown(test, unsafe_allow_html=True)
            if op_movies == "First Twenty Years with the Highest Numbers of Movies produced":
                st.image('resources/imgs/first_20years.png',use_column_width=True)
                st.write("The year 2015 had the largest number of films created, with over 1700. It was followed by the years 2016 and 2017, which both saw over 1500 films produced.")
                st.write("One thing to note is that a year like 2019 would have been expected to have a lot of movies released, but due to the outbreak of COVID 19, we observe a decline in movie releases in the year 2019.")

        if choose == "Directors":
        #if option_selection == "Directors":
            #st.info("We start off with directors, A film director controls a film's artistic and dramatic aspects and visualizes the screenplay (or script) while guiding the technical crew and actors in the fulfilment of that vision. The director has a key role in choosing the cast members, production design and all the creative aspects of filmmaking\n\n\n\nEven though most people don't into finding our who director what movie to decide whether its going to be a good watch or not, there is a proportion of people that either watch the credits at the end of the movie or do research of each movie before they watch it, for these people director of a movie plays an import role in decided whether or not to watch a movie, for me personally I watch mroe series's than movies and but I know that if a series is directed by Chuck Lorre than I will definately love it.\n\nlet's start by finding our which directors have recieved the most number of ratings for their collective movies")
            
            op_director = st.radio("Choose an option under directors",("Top 3 most rated directors","Top 3 directors with most number of movies","10 highest rated director with over 10000 ratings","10 worst rated directors with over 10000 ratings"))

            if op_director == "Top 3 most rated directors":
                st.image('resources/imgs/Mean Rating Per.png',use_column_width=True)
                dis = '''### Top 3 Directors with High ratings

<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3ie6FvZbpJx2VbSMzbGsFagq2wPgnNXJxSPQVTI6ofqhWv28AZKCUZIt54kEQHr9gfiI&usqp=CAU" alt="Photo of Stephen King" class="GeneratedImage"> <img height = "238" width = 950 src="resources\imgs\king.jpg" alt="Movies of sk" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Stephen_King">Stephen King</a>  The Shawshank Redemption, which debuted at the top of both lists of the Top 25 Most Rated Movies of All Time and the Top 10 Best Rated Movies of All Time, was adapted from a novel by Stephen King, who is also an author of horror, supernatural fiction, suspense, crime, and fantasy novels. Stephen King has directed a total of 23 movies.</a>
</br>
</br>
<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxlTrJvdxqSMBYf90USQe0qXEaMhXdy35FJOpUlEZ5PGl4wIBI" alt="Photo of Quentin Tarantino" class="GeneratedImage">  <img height = "238" width = 950 src="resources\imgs\quent.JPG" alt="Movies of Tom Hanks" class="GeneratedImage"></br>
</br>
<a href="https://en.wikipedia.org/wiki/Quentin_Tarantino"> Quentin Tarantino</a> an American film director, screenwriter, producer, and actor, now sits atop the ranking. His movies include nonlinear plots, aestheticized violence, lengthy discussion sequences, ensemble casts, allusions to pop culture and a wide range of other movies, soundtracks mostly made up of songs and score pieces from the 1960s to the 1980s, alternate histories, and elements of neo-noir film. One of Quentin Tarantino's films with the highest ratings In the top 10 best-rated movies we previously viewed, pulp fiction was prevalent.</a>
</br>
</br>

<img height = "238" width = 178 src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSFu6ohQVsNtOaLKFv6Qv3Xbp2GCIx54HXeTKy0qnVOiZEp4IFT" alt="Photo of John Sayles" class="GeneratedImage">  <img height = "238" width = 950 src="resources\imgs\jon.png" alt="Movies of Tom Hanks" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Stephen_King">John Sayles</a>   is an American independent film director, screenwriter, editor, actor, and novelist. He has twice been nominated for the Academy Award for Best Original Screenplay, for Passion Fish and Lone Star. His film Men with Guns was nominated for the Golden Globe for Best Foreign Language Film.</a>
</br>
</br>

### Key observatios
* From the list above, we can see certain directors who are immediately recognized. Stephen King and Quentin Tarantino are, predictably, at the top of the list.
* It comes as no surprise that the director of the film with the highest rating, Shawshank Redemption, is ranked first.
* The fact that the top 3 directors have an average mean rating of 4.0 further demonstrates how positively moviegoers rank their favorite films.
---
After seeing the total number of ratings each filmmaker has received, it is only logical to question how many films each of these directors has produced. Since this would affect the overall number of ratings they have received, let's find out which directors have produced the most films.

---
                '''  
                st.markdown(dis, unsafe_allow_html=True)
            if op_director == "Top 3 directors with most number of movies":

                direct = '''### Top 3 Directors with most movies released

<img height = "238" width = 178 src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Luc_Besson_by_Gage_Skidmore.jpg/640px-Luc_Besson_by_Gage_Skidmore.jpg" alt="Photo of Luc Besson" class="GeneratedImage">  <img height = "238" width = 950 src="https://i.ibb.co/hL7J390/luc.jpg" alt="Movies of Tom Hanks" class="GeneratedImage">
</br>
<a href="https://en.wikipedia.org/wiki/Luc_Besson">Luc Paul Maurice Besson</a>  is a French filmmaker, writer, and producer of movies. The Big Blue, La Femme Nikita, and Subway were all movies he either directed or produced. </a>
</br>
</br>
<img height = "238" width = 178 src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQXYKDvhxIVt8R_yV3LLLZJ2LemcV860GqEgu9TKCDvGSDnHksM" alt="Photo of woody allen" class="GeneratedImage"> <img height = "238" width = 950 src="resources\imgs\woody.JPG" alt="Movies of Tom Hanks" class="GeneratedImage">
</br>
<a href="https://en.wikipedia.org/wiki/Woody_Allen"> Woody Allen</a> is an American filmmaker, writer, actor, and comedian whose career spans more than six decades including several films that have won Academy Awards. </a>
</br>
</br>

<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3ie6FvZbpJx2VbSMzbGsFagq2wPgnNXJxSPQVTI6ofqhWv28AZKCUZIt54kEQHr9gfiI&usqp=CAU" alt="Photo of Stephen King" class="GeneratedImage"> <img height = "238" width = 950 src="resources\imgs\king.JPG" alt="Movies of Tom Hanks" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Stephen_King">Stephen King</a>  is an American writer of books in the genres of horror, science fiction, fantasy, suspense, and paranormal fiction. </a>
</br>
</br>


---

                '''
                st.markdown(direct, unsafe_allow_html=True)
                st.image('resources/imgs/Number of Movies Per director.png',use_column_width=True)
                st.write("Luc Besson and Woody Allen share the top rank with an equal amount of 26 films apiece. Stephen King is next. Having a total of 23 films, this time at number 2. We also notice some well-known names, including William Shakespeare, an English playwright, poet, and actor who is renowned as the greatest dramatist and writer in the English language. Additionally, Tyler Perry, a well-known producer, director, actor, screenwriter, dramatist, novelist, composer, businessman, and philanthropist, is most known for his Madea film series, which he not only directs but also stars in three roles.\n\n\n\nMost of the movies that were produced by the directors in the above bar plot have the genres Drama and Romance or a mixture of those two gernes popularly known as romantic comedies. Whether or not these two genres are the most succesful generes of highest rated genres is still to be investigated.")
            if op_director == "10 highest and worst rated director with over 10000 ratings":
            #if director_option == "10 highest and worst rated director with over 10000 ratings":
                st.image('resources/imgs/10_highest_rated_D3.png',use_column_width=True)
                st.image('resources/imgs/10_worst_directors_D4.png',use_column_width=True)
                st.write("Toping the chart of the best rated directors is Chuck Palahniuk, the director of Fight Club that recieved an average rating of 4.22 which had Action, Crime, Drama and thriller genres. The second spot is held by Christopher McQuarrie recieving an average rating of 4.19 for three movies he has directed namely Usual suspects, Way of the gun and Edge of Tomorrow with mix of genres Action, Crime and Thriller, this this shares some light on the question we posed earlier of whether people the most succesful genres were a mix of Drama, Romance or Comedy, as we see that our two best rated directors create blockbusters with mix of genres action and thriller. We will investigated these genres thoroughly at a later stage.\n\n\Looking at the worst rated directed we see that the lowest rated director is Jack Bernstein with an average rating of 2.84\n\n\n\nWe now move to the next factor that influences the perfrance of of viewers that is the genre of the movie.\n\n")
        
        
        if choose == "Genres":
        #if option_selection == "Genres":
            op_genre = st.radio("Choose an option under Genres",("Treemap of movie genres","Genre average rating over the years","Word cloud of movie genres"))
            #options_genres = ["Treemap of movie genres","Genre average rating over the years","Word cloud of movie genres"]
            #genre_options = st.selectbox('Choose option', options_genres)
            if op_genre == "Treemap of movie genres":
            #if genre_options == "Treemap of movie genres":
                st.image('resources/imgs/Treemap_G1.png',use_column_width=True)
                st.write("The genre treemap shows that Drama is the most popular genre with a genre count of 25606 followed by comedy with a count of 16870 as we initially suspected, We also see that Thriller and Romance follow suit. IMAX is by far the least popular genres with a count of 195 with Film-Noir following with a count of 353.\n\n\n\nWe have now seen the the most popular and least popular genres, lets now dig a little deeper into the genres and find out if whether the genre preference has changed throughout the years, to investigate this let's created an animated bar plot.")
            if op_genre == "Genre average rating over the years":
            #if genre_options == "Genre average rating over the years":
                st.video('resources/imgs/download.mp4')
                st.write("Right off the bat of the bet, the bar charr race shows us that there has been a change in genre preferences over the years")
                st.write("Stangely Animation was the best rated genre in 1995.\n\n\n\nIn 1996 Animation dropped to the 8th position and the Documentary became the most rated genre\n\n\n\n1997 Animation toped the char again and the following year Documentaty took over, seems between those 4 years the most prefered genres where Animation and Documentary, Strange times indeed...\n\n\n\nIn 1999 Crime movies started being popular and became the highest rated genre that year\n\n\n\nDrame took over the top spot in the year 2000\n\n\n\n2001 We see Fantasy, Crime and Drama taking the 1st. 2nd and 3rd spots respectively and we see these genres taking turns over the next couple of years until 2013 when Romance takes the lead and Documentaries become more popular and toping the chart in 2015.")
            if op_genre == "Word cloud of movie genres":
            #if genre_options == "Word cloud of movie genres":
                st.image('resources/imgs/Wordcloud_G3.png',use_column_width=True)

        if choose == "Title Cast":
           
        #if option_selection == "Title Cast":
            st.image('resources/imgs/Number of Movies Per Actor For Top 10 Actors.png',use_column_width=True)
            act = '''### Top 3 Movie Actors with Highest Number of movies released

<img height = "238" width = 178 src="https://cdn.britannica.com/77/191077-050-63262B99/Samuel-L-Jackson.jpg" alt="Photo of Tom Hanks" class="GeneratedImage">
<img height = "238" width = 950 src="https://i.ibb.co/x3452bJ/sam.jpg" alt="Movies of Tom Hanks" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Tom_Hanks">Samuel Leroy Jackson </a>  is an American actor. One of the most widely recognized actors of his generation, the films in which he has appeared have collectively grossed over $27 billion worldwide, making him the highest-grossing actor of all time. </a>
</br>
</br>
<img height = "238" width = 178 src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSItxlkc_a8e3O3T59cqB6Uw5iPRY5bJlmr8ZUt0KRPLObKcdTd" alt="Photo of Edward Norton" class="GeneratedImage">
<img height = "238" width = 950 src="https://i.ibb.co/qM46cdK/wilss.jpg" alt="Movies of Bruce Willis" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Bruce_Willis">Bruce Willis</a>  is a famous American actor. In the 1970s, his acting career got its start on an off-Broadway theater. He rose to stardom in a starring role on the comedy-drama series Moonlighting (1985–1989), and he went on to feature in more movies, being known as an action hero for his performances as John McClane in the Die Hard trilogy (1988–2013) and other projects.</a>
</br>
</br>

<img height = "238" width = 178 src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRpa6S_5nG_DBliLGNbMMqx_tSAxqmQqDbK26PsKIdZUPxZT017" alt="Photo of Steve Buscemi" class="GeneratedImage">
<img height = "238" width = 950 src="https://i.ibb.co/K7JbtwT/ste.jpg" alt="Movies of Leonardo DiCaprio" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Steve_Buscemi">Steve Buscemi</a> is an American actor and film producer. Known for his work as a leading man in biopics and period films, he is the recipient of numerous accolades, including an Academy Award, a British Academy Film Award, and three Golden Globe Awards.  </a>
</br>
</br>
'''
            st.write("The likes of Samuel L. Jackson ,steve Buscemi ans Keith David are the most popular cast members according to the graph above.")
            st.markdown(act, unsafe_allow_html=True)

    #About
    if page_selection == "About":
        title_about = """
	    <div style="background-color:#eebd8a;padding:10px;border-radius:10px;margin:10px;">
	    <h1 style="color:black;text-align:center;"> - The Team -</h1>
        <h3 style="color:black;text-align:right;">We are a team of data science students from Explore Data Science Academy. This is our project for unsupervised sprint.</h3>
        """
        mission = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h1 style="color:black;text-align:center;"> - Our Mission - </h1>
        <h3 style="color:black;text-align:center;">To keep you entertained by helping you find movies you're most likely to enjoy&#128515</h3>
        """

        contributors = """
        <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h1 style="color:black;text-align:center;"> - Contributors -</h1>
        """
        
        
        st.markdown(title_about, unsafe_allow_html=True)
        st.markdown(mission, unsafe_allow_html=True)
        st.markdown(contributors, unsafe_allow_html=True)
        st.image('resources/imgs/team members.png',use_column_width=True)

    if page_selection == "Business Pitch":
        st.image('resources/imgs/BV_1.jpg',use_column_width=True)
        st.write("Some of the biggest companies in the world invested in streaming entertainment in the 21st century. The investment in streaming entertainment gave us platforms such as Netflix, Apple TV,, Disney Plus, Amazon prime and many more. These platforms are racking up millions of subscribers as the entire world is now streaming more than ever.")
        st.write("You may be wondering why these streaming platforms are attracting millions of subscribers, there are several reasons why people are leaning more towards streaming platforms. Streaming platforms have a lot of diverse content that can be consumed anywhere, anytime, and the subscribers are in total control of the rate at which they consume the content.")
        st.image('resources/imgs/BV_2.jpg',use_column_width=True)
        st.write("Another thing that is a major contributor in the rise and success of streaming platforms is their ability to recommend content that their users are most likely to watch and enjoy. They achieve this through the use of recommender algorithms. These algorithms ensure that each user is exposed to what they like.")
        st.image('resources/imgs/increasing.jpg',use_column_width=True)
        st.write("When doing exploratory data analysis we saw that the number of movies released increases exponentially each year. The exponential increase in the number of movies released means that streaming platforms need an excellent recommender algorithm to ensure that the movies reach the right audience.")
        st.image('resources/imgs/BV_L.jpg',use_column_width=True)
        st.write("This is where our recommender algorithm comes in. Our recommender algorithm will help with user retention by making tailored recommendations for each user. The user retention will ultimately result in a growth of the platform.")




if __name__ == '__main__':
    main()
