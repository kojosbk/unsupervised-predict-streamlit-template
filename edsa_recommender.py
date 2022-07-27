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
    page_options = ["Home","Recommender System","Solution Overview","Exploratory Data Analysis(EDA)","Business Pitch","About"]

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
        solu = '''Our goal was to develop a collaborative filtering or content-based recommendation system that can reliably anticipate how a user will evaluate a film they haven't yet seen based on their past preferences. We made advantage of a unique MovieLens dataset. The dataset we utilized is described in <a href="https://markuphero.com/share/7Uz8F3mlG4lO1eUehLe2"> this link.</a>
        '''
        st.markdown(solu, unsafe_allow_html=True)
        st.write("Data preparation was the first phase, during which we searched for missing values. In three of the eight datasets we have, we  found missing values.")
        st.write("Following data preparation, we began constructing our based model. Five distinct collaborative base models were created by our team: SVD, SVDpp, Normal Predictor, CoClustering, KNN Baseline, and NMF. A statistical metric known as the root mean square error (RMSE), which calculates the average squared difference between the estimated values and the actual value, was used to compare their performances. An accurate model is one with a low RMSE value. SVD and KNN Baseline base models had the best performance. The SVD model underwent hyperparameter adjustment, and the outcome was the best on Kaggle.")

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
            
            op_director = st.radio("Choose an option under directors",("Top 3 most rated directors","Top 3 directors with most number of movies","3 worst rated directors"))

            if op_director == "Top 3 most rated directors":
                st.image('resources/imgs/Mean Rating Per.png',use_column_width=True)
                dis = '''### Top 3 Directors with High ratings

<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3ie6FvZbpJx2VbSMzbGsFagq2wPgnNXJxSPQVTI6ofqhWv28AZKCUZIt54kEQHr9gfiI&usqp=CAU" alt="Photo of Stephen King" class="GeneratedImage"> <img height = "238" width = 950 src="https://i.ibb.co/GFtp5H9/king.jpg" alt="Movies of sk" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Stephen_King">Stephen King</a>  The Shawshank Redemption, which debuted at the top of both lists of the Top 25 Most Rated Movies of All Time and the Top 10 Best Rated Movies of All Time, was adapted from a novel by Stephen King, who is also an author of horror, supernatural fiction, suspense, crime, and fantasy novels. Stephen King has directed a total of 23 movies.</a>
</br>
</br>
<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxlTrJvdxqSMBYf90USQe0qXEaMhXdy35FJOpUlEZ5PGl4wIBI" alt="Photo of Quentin Tarantino" class="GeneratedImage">  <img height = "238" width = 950 src="https://i.ibb.co/QNKJg49/quent.jpg" alt="Movies of QT" class="GeneratedImage"></br>
</br>
<a href="https://en.wikipedia.org/wiki/Quentin_Tarantino"> Quentin Tarantino</a> an American film director, screenwriter, producer, and actor, now sits atop the ranking. His movies include nonlinear plots, aestheticized violence, lengthy discussion sequences, ensemble casts, allusions to pop culture and a wide range of other movies, soundtracks mostly made up of songs and score pieces from the 1960s to the 1980s, alternate histories, and elements of neo-noir film. One of Quentin Tarantino's films with the highest ratings In the top 10 best-rated movies we previously viewed, pulp fiction was prevalent.</a>
</br>
</br>

<img height = "238" width = 178 src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSFu6ohQVsNtOaLKFv6Qv3Xbp2GCIx54HXeTKy0qnVOiZEp4IFT" alt="Photo of John Sayles" class="GeneratedImage">  <img height = "238" width = 950 src="https://i.ibb.co/d4rc8Hg/jon.png" class="GeneratedImage"></br>
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
<img height = "238" width = 178 src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQXYKDvhxIVt8R_yV3LLLZJ2LemcV860GqEgu9TKCDvGSDnHksM" alt="Photo of woody allen" class="GeneratedImage"> <img height = "238" width = 950 src="https://i.ibb.co/88Nhr6p/woody.jpg" alt="Movies of Tom Hanks" class="GeneratedImage">
</br>
<a href="https://en.wikipedia.org/wiki/Woody_Allen"> Woody Allen</a> is an American filmmaker, writer, actor, and comedian whose career spans more than six decades including several films that have won Academy Awards. </a>
</br>
</br>

<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3ie6FvZbpJx2VbSMzbGsFagq2wPgnNXJxSPQVTI6ofqhWv28AZKCUZIt54kEQHr9gfiI&usqp=CAU" alt="Photo of Stephen King" class="GeneratedImage"> <img height = "238" width = 950 src="https://i.ibb.co/GFtp5H9/king.jpg" alt="Movies of Tom Hanks" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Stephen_King">Stephen King</a>  is an American writer of books in the genres of horror, science fiction, fantasy, suspense, and paranormal fiction. </a>
</br>
</br>


---
                '''
                st.markdown(direct, unsafe_allow_html=True)
                st.image('resources/imgs/Number of Movies Per director.png',use_column_width=True)
                st.write("Luc Besson and Woody Allen share the top rank with an equal amount of 26 films apiece. Stephen King is next. Having a total of 23 films, this time at number 2. We also notice some well-known names, including William Shakespeare, an English playwright, poet, and actor who is renowned as the greatest dramatist and writer in the English language. Additionally, Tyler Perry, a well-known producer, director, actor, screenwriter, dramatist, novelist, composer, businessman, and philanthropist, is most known for his Madea film series, which he not only directs but also stars in three roles.\n\n\n\nMost of the movies that were produced by the directors in the above bar plot have the genres Drama and Romance or a mixture of those two gernes popularly known as romantic comedies. Whether or not these two genres are the most succesful generes of highest rated genres is still to be investigated.")
            if op_director == "3 worst rated directors":
            #if director_option == "10 highest and worst rated director with over 10000 ratings":
                st.image('resources/imgs/worst.png',use_column_width=True)
                wor = '''
                ### Top 3 Directors with the lowest ratings

<img height = "125" width = 125 src="https://www.thepitchkc.com/content/uploads/2021/11/g/r/charles-band-scaled-e1637002282929.jpg" alt="Photo of Charles Band" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Charles_Band">Charles Band</a> is an American film producer and director, known for his work on horror comedy movies. </a>
</br>
</br>
<img height = "125" width = 125 src="https://upload.wikimedia.org/wikipedia/en/e/e3/John_Hughes_Home_Alone_2.jpg" alt="Photo of John Hughes" class="GeneratedImage"> 
</br>
<a href="https://en.wikipedia.org/wiki/John_Hughes_(filmmaker)"> John Hughes</a> was an American filmmaker. Hughes began his career in 1970 as an author of humorous essays and stories for the National Lampoon magazine. </a>
</br>
</br>

<img height = "125" width = 125 src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQq8v6TWEuFEzwzeUmeVXsHWsR2nTst1wxrbHrSS77qnJMYtqog" alt="Photo of Clive Barker" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Clive_Barker">Clive Barker</a>   is an English playwright, author, film director and visual artist who came to prominence in the mid-1980s with a series of short stories, the Books of Blood, which established him as a leading horror writer. He has since written many novels and other works. </a>
</br>
</br>

### Key observatios
* From the list above, we can notice a few filmmakers that stand out right away. Puppet Master was created by Charles band, which gets very poor reviews.

* The least popular directors have an average mean rating of 2.5, which further exemplifies how poorly viewers evaluate their movies.
---

'''
                st.markdown(wor, unsafe_allow_html=True)
                        
        
        if choose == "Genres":
        
            op_genre = st.radio("Choose an option under Genres",("Mean Rating of movies Per Genre","Genre average rating over the years"))
            
            if op_genre == "Mean Rating of movies Per Genre":
            #if genre_options == "Treemap of movie genres":
                st.image('resources/imgs/Mean Rating Per Genre.png',use_column_width=True)
                #st.write("The genre bar chart shows that Drama is the most popular genre with a genre count of 25606 followed by comedy with a count of 16870 as we initially suspected, We also see that Thriller and Romance follow suit. IMAX is by far the least popular genres with a count of 195 with Film-Noir following with a count of 353.\n\n\n\nWe have now seen the the most popular and least popular genres, lets now dig a little deeper into the genres and find out if whether the genre preference has changed throughout the years, to investigate this let's created an animated bar plot.")
                gendec = '''
                #### Observations
<img height = "210" width = 400 src="https://imgix.bustle.com/fatherly/2019/06/best-nature-documentaries.jpg?w=1200&h=630&fit=crop&crop=faces&fm=jpg" align="center" alt="Photo of Clive Barker" class="GeneratedImage"></br>

- Documentries seams to be the most higly rated releases in the data

- The ratings are almost evenly distributed, with the exception of documentaries, conflict, drama, musicals, and romance, which score over average. On the other side, the ratings for thriller, action, science fiction, and horror are noticeably below average.

- Hollywood crime dramas are referred to as "film-noir," especially those that stress cynical attitudes and sexual desires. In general, the "classic era" of American film-noir is thought to have been the 1940s and 1950s. Though it's possible that their particular audience is why some films earn the greatest ratings. For IMAX movies, the same reasoning holds true; hence, we only accounted for categories with a count of 500 or more in this graph.

---
We have now seen the the most popular and least popular genres, lets now dig a little deeper into the genres and find out if whether the genre preference has changed throughout the years, to investigate this let's created an animated bar plot.

---
'''
                st.markdown(gendec, unsafe_allow_html=True)
            if op_genre == "Genre average rating over the years":
            #if genre_options == "Genre average rating over the years":
                st.video('resources/imgs/download.mp4')
                st.write("Right off the bat of the bet, the bar charr race shows us that there has been a change in genre preferences over the years")
                st.write("Stangely Animation was the best rated genre in 1995.\n\n\n\nIn 1996 Animation dropped to the 8th position and the Documentary became the most rated genre\n\n\n\n1997 Animation toped the char again and the following year Documentaty took over, seems between those 4 years the most prefered genres where Animation and Documentary, Strange times indeed...\n\n\n\nIn 1999 Crime movies started being popular and became the highest rated genre that year\n\n\n\nDrame took over the top spot in the year 2000\n\n\n\n2001 We see Fantasy, Crime and Drama taking the 1st. 2nd and 3rd spots respectively and we see these genres taking turns over the next couple of years until 2013 when Romance takes the lead and Documentaries become more popular and toping the chart in 2015.")
            

        if choose == "Title Cast":
            op_genre = st.radio("Choose an option under Title Cast",("Top 3 Movie Actors with Highest Number of movies released","Top 3 Movie Actors with Highest Number of movies Rated(20+ movies released)"))
            
           
            if op_genre == "Top 3 Movie Actors with Highest Number of movies released":
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

            if op_genre == "Top 3 Movie Actors with Highest Number of movies Rated(20+ movies released)":
                st.image('resources/imgs/Mean Rating Per Actor (20+ movies released).png',use_column_width=True)
                #st.write("The likes of Samuel L. Jackson ,steve Buscemi ans Keith David are the most popular cast members according to the graph above.")
                actr = '''
                ### Top 3 Movie Actors with High ratings (20+ movies released)

<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-bt7_ZKFMU8UOOjlq-GYF5P0iNJVuqz9HuDI3GkLmLXDfifpy" alt="Photo of Tom Hanks" class="GeneratedImage">
<img height = "238" width = 950 src="https://i.ibb.co/fVWjWRQ/2tom-h.jpg" alt="Movies of Tom Hanks" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Tom_Hanks">Tom Hanks</a> is an American actor and filmmaker. Known for both his comedic and dramatic roles, he is one of the most popular and recognizable film stars worldwide, and is regarded as an American cultural icon. </a>
</br>
</br>
<img height = "238" width = 178 src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTWkkwUYKcdK296LMj5-aAkieIrvt7pqfHc4N16BIvL9EHFSpuf" alt="Photo of Edward Norton" class="GeneratedImage">
<img height = "238" width = 950 src="https://i.ibb.co/cbYn0CN/tempsnip.jpg" alt="Movies of Edward Norton" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Edward_Norton">Edward Norton</a> is an American actor and filmmaker. He has received numerous awards and nominations, including a Golden Globe Award and three Academy Award nominations. Born in Boston, Massachusetts and raised in Columbia, Maryland, Norton was drawn to theatrical productions at local venues as a child. </a>
</br>
</br>

<img height = "238" width = 178 src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2q9tvih6sHPAEEbPoCRrWpf2IWVG5IOo5jIxqCA7dgrggsQO5" alt="Photo of Leonardo DiCaprio" class="GeneratedImage">
<img height = "238" width = 950 src="https://i.ibb.co/0YGYhPd/leo.jpg" alt="Movies of Leonardo DiCaprio" class="GeneratedImage"></br>
<a href="https://en.wikipedia.org/wiki/Leonardo_DiCaprio">Leonardo DiCaprio</a> is an American actor and film producer. Known for his work as a leading man in biopics and period films, he is the recipient of numerous accolades, including an Academy Award, a British Academy Film Award, and three Golden Globe Awards.  </a>
</br>
</br>

### Key observatios
* As we can see from the list above, practically every actor is easily identifiable. Naturally, Tom Hanks and Leonardo DiCaprio are at the top of the list.

* The average mean rating of 3.6 for the top 3 actors further indicates how highly moviegoers regard their favorite actors.
---

'''
                st.markdown(actr, unsafe_allow_html=True)

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
        <h3 style="color:black;text-align:center;">To empower our clients to better manage their data using automated applications &#128515</h3>
        """

        contributors = """
        <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
        <h1 style="color:black;text-align:center;"> - Contributors -</h1>
        """
        
        
        st.image('resources/imgs/logosidebar-removebg-preview.png',use_column_width=True)
        st.markdown(mission, unsafe_allow_html=True)
        st.markdown(contributors, unsafe_allow_html=True)
        st.image('resources/imgs/MISSION STATEMENT (6).png',use_column_width=True)

    if page_selection == "Business Pitch":
        st.image('resources/imgs/BV_1.jpg',use_column_width=True)
        st.write("In this twenty-first century, some of the greatest corporations in the world made investments in streaming entertainment. We now have platforms like Netflix, Apple TV, Disney Plus, Amazon Prime, and many more thanks to the investment in streaming entertainment. Millions of people are subscribing to these sites as the world streams more content than ever before.")
        st.write("There are a number of reasons why people are turning more and more to streaming platforms, which may have you wondering why these services are drawing millions of members. The users have complete control over the pace at which they consume the information on streaming platforms, which provide a wide variety of content that can be accessed anytime, anywhere.")
        st.image('resources/imgs/BV_2-removebg-preview.png',use_column_width=True)
        st.write("Their capacity to suggest material that their customers are most likely to view and appreciate is another factor that significantly contributes to the growth and success of streaming platforms. They accomplish this by utilizing recommender algorithms. Each person is exposed to content they are interested in thanks to these algorithms. ")
        st.image('resources/imgs/increasing.jpg',use_column_width=True)
        st.write("We discovered through exploratory data analysis that the annual rise in movie releases is exponential. Due to the exponential rise in the number of movies being published, streaming companies require a superior recommender algorithm to guarantee that the films get seen by the intended audience.")
        st.image('resources/imgs/BV_L.jpg',use_column_width=True)
        st.write("Our recommender system comes into play in this situation. By providing each user-specific recommendations, our recommender algorithm will aid in retaining users. The platform will eventually expand as long as users stay on it.Another benefit is that any shopping site may utilize the same principles as our recommender system to provide consumers with recommendations for other products based on their previous purchases.")




if __name__ == '__main__':
    main()
