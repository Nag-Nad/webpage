import streamlit as st
import pandas
from datetime import datetime
import pytz

# Set the date and time
st.write(datetime(2023, 5, 27, 12, 38, tzinfo=pytz.timezone("EST")))

# Make two columns for the image and info
col1, col2 = st.columns(2)
with col1:
    light_title = st.title(':violet[Hey! It is me Naqme :sunglasses:]')
    content = """ Welcome to my website! I'm thrilled to have you here.

I'm a biotechnology student residing in the vibrant city of Berlin. While my journey has been filled with challenges, it has also fueled my drive to excel in everything I pursue. One of my recent passions is programming, and I am dedicated to mastering this powerful tool.

Cooking is an activity that brings immense joy to my life. In the kitchen, I experiment with flavors and ingredients, creating culinary delights that nourish both body and soul.

Perseverance is my guiding principle. I am known for my unwavering work ethic and determination. Challenges motivate me to push harder, and I refuse to give up easily. With every obstacle, I learn, adapt, and grow stronger.

Join me on this exciting journey as I explore the intersections of biotechnology, programming, and culinary delights. Together, we'll embrace the challenges, celebrate the successes, and make lasting connections along the way.
 
   """

    st.info(content)

with col2:
    st.image('images/Me.png', width=700 )
    
#make columns for images
col3, col4, col5 = st.columns([1.5, 2.0, 1.5])

col6, col7, col8 = st.columns([1.5, 1.5, 1.5])
with col8:
    st.image('images/food.png', caption='Yumm! pasta')
with col6:
    st.image('images/lab.png', caption='A nice lab day!')
with col7:
    st.image('images/trep.png', caption='Beautiful Treptower park, Berlin.')

# Make a selectbox to choose from
st.title(':violet[My Journey]')
my_journey = st.selectbox('Please choose one: ', options = ['My Education', 'My Experience'])

if my_journey == 'My Education':
        df = pandas.read_csv('files/education.csv', sep=';', index_col='name')
        st.write(df)
        
elif my_journey == 'My Experience':
        df1 = pandas.read_csv('files/experience.csv', sep=';', index_col='where')
        st.write(df1)

# Make checkbox for stay in touch section
st.subheader('Would you like to stay in touch?')           
st.subheader('Then ping me in :earth_americas:')
email= st.checkbox('Email')
if email:
    st.write('My gmail address is: naderi.nagmeh@gmail.com')
linkedin = st.checkbox('LinkedIn')
if linkedin:
    st.write('You can find me under this name on LinkedIn: Nagmeh Naderi')
gitHub = st.checkbox('github')
if gitHub:
    st.write('My github link is: https://github.com/Nag-Nad/python')
