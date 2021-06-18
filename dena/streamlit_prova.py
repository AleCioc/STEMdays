import streamlit as st
import numpy as np
import pandas as pd

# Running the code
# streamlit run your_script.py [-- script args]
# streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py


#Code for all pages
st.title('My first app')
st.header("This will be in all pages")
st.subheader("Select a page from the left!")



#Sidebar
bla = st.sidebar.selectbox(
    'This is a sidebar', ["Page 1", "Page 2", "Page 3"]
)

if bla == "Page 1":
    st.write("We are in Page 1")

    # Area chart
    df_area = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    df_area

    st.area_chart(df_area)

    # Markdown
    st.markdown(
        """
        * option 1
        * option 2

        ** bold **
        """
    )

    # Latex
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

    # Progress bar
    import time

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(11):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i}')
        bar.progress(i * 10)
        time.sleep(0.1)

    '...and now we\'re done!'

elif bla == "Page 2":
    ## Button
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    # Display image
    from PIL import Image

    image = Image.open("Dolomites-Italian-Alps.jpg")
    st.image(image, caption="Dolomiti!")

    # Display sound
    audio_bytes = open("file_example_WAV_1MG.wav", "rb").read()
    st.audio(audio_bytes, format="audio/ogg")



elif bla == "Page 3":
    #Columns, button
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Press me?')
    if pressed:
        right_column.write("Woohoo!")

    #Expander
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")


    #Checkbox
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['Hidden', 'df', 'c'])

        chart_data


    #Selectbox
    option = st.selectbox(
        'Which number do you like best?',
         [1, 5, 22, 89])

    'You selected: ', option

    #Display a dataframe with magic
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 50]
    })
    # df

    #Line chart
    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])

    # st.line_chart(chart_data)

    #Map of random spots in Torino
    map_df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [45.0736, 7.6351],
        columns=['lat', 'lon'])

    map_df
    st.map(map_df)

    #Display code
    def get_user_name():
        return 'John'

    with st.echo():
        # Everything inside this block will be both printed to the screen
        # and executed.

        def get_punctuation():
            return '!!!'

        greeting = "Hi there, "
        value = get_user_name()
        punctuation = get_punctuation()

        st.write(greeting, value, punctuation)

    # And now we're back to _not_ printing to the screen
    foo = 'bar'
    st.write('Done!')

    #Give link to Gianlu
    st.write("Link: https://pastebin.com/CGwyiebS")

