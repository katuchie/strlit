from PIL import Image
import streamlit as st

st.set_page_config(page_title="Приюти кота!", page_icon=":cat:", layout="wide")
img = Image.open("UPAWcat.jpeg")
img_mika = Image.open("cat1.jpg")
img_tisha = Image.open("cat2.jpg")
img_hirotaka =Image.open("cat3.jpg")

with st.container():
    st.title("Shelter the cat!:cat:")
    st.text("A group of enthusiasts from Kostroma wants to reduce the number of homeless cats!")
    st.write("[Join us!](http://16.cshse.beget.tech/cat/3)")

with st.container():
    st.write("---")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(img)
    with text_col:
        st.header('the idea of us??')
        st.write(
            '''
            Seeing homeless cats became a commonplace nowadays. However, we ain't satisfied with
            such situation. We assert all our cats and cherish them! Being persistent is our 
            resposibility!
            '''
        )
with st.container():
    st.write("---")
    option = ["HIROTAKA", "MIKA", "TISHA"]
    sel = st.selectbox("Choose one cat to discover :)", options=option)

    if sel == "HIROTAKA":

        with st.container():
            image_col, text_col = st.columns((1, 2))
            with image_col:
                st.image(img_hirotaka)
            with text_col:
                st.header('HIROTAKA')
                st.write(
                    '''
                    Hirotaka is the first cat in out organization. Having survived in unbearable
                    conditional, now she is glowing all the time !
                    Her name is so unique and it is definitely her highlight.
                    
                    [find more information](http://16.cshse.beget.tech/cat/3)
                    '''
                )


    elif sel == "MIKA":

        image_col, text_col = st.columns((1, 2))
        with image_col:
            st.image(img_mika)
        with text_col:
            st.header('MIKA')
            st.write(
                '''
                Mika is one of the most popular cat due to her ordinary features.
                This kitten has harmful past, but we believe that her future will flourish.
                Being cutie, she is waiting for caring hosts!
                
                [find more information](http://16.cshse.beget.tech/cat/1)
                '''
            )
    else:

        image_col, text_col = st.columns((1, 2))
        with image_col:
            st.image(img_tisha)
        with text_col:
            st.header('TISHA')
            st.write(
            '''
            
            It has two beautiful eyes, adorably tiny paws, sharp claws,
            and two perky ears which are very sensitive to sounds. 
            It has a tiny body covered with smooth fur and it has a furry tail as well.
            Cats have an adorable face with a tiny nose, a big mouth and a few whiskers under its nose. 
            
            [find more information](http://16.cshse.beget.tech/cat/2)
            '''
            )
