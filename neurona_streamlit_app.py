import streamlit as st


#
st.image("./image.jpg")

# Title
st.title("¡Hola neurona!")
st.write("")



# Tabs for each exercise
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.header("Una neurona con una entrada y un peso")
    # Input bar 1
    peso_t11 = st.number_input('Peso', key='t11_w0')

    # Input bar 2
    entrada_t11 = st.number_input('Introduzca el valor de la entrada', key='t11_x0')

    # If button is pressed
    if st.button("Calcular la salida", key='submit_tab1'):
        # Calculo de resultado
        salida_tab1 = peso_t11 * entrada_t11
        st.text(f"La salida de la neurona es {salida_tab1}")

with tab2:
    st.header("Una neurona con dos entradas y dos pesos")
    # Input bar 1
    peso_t21 = st.number_input('Peso 1', key='t21_w0')
    peso_t22 = st.number_input('Peso 2', key='t22_w1')

    # Input bar 2
    entrada_t21 = st.number_input('Introduzca el valor de la entrada 1', key='t21_x0')
    entrada_t22 = st.number_input('Introduzca el valor de la entrada 2', key='t22_x1')

    # If button is pressed
    if st.button("Calcular la salida", key='submit_tab2'):
        # Calculo de resultado
        salida_tab2 = peso_t21 * entrada_t21 + peso_t22 * entrada_t22
        st.text(f"La salida de la neurona es {salida_tab2}")

with tab3:
    st.header("Una neurona con tres entradas, tres pesos y bias")


    col1, col2, col3 = st.columns(3)
    with col1:
        peso_t31 = st.slider('Peso 1', 0., 5., key='t31_w0')
        entrada_t31 = st.number_input('Introduzca el valor de la entrada 1', key='t31_x0')
    with col2:
        peso_t32 = st.slider('Peso 2', 0., 5., key='t32_w1')
        entrada_t32 = st.number_input('Introduzca el valor de la entrada 2', key='t32_x1')
    with col3:
        peso_t33 = st.slider('Peso 3', 0., 5., key='t33_w2')
        entrada_t33 = st.number_input('Introduzca el valor de la entrada 3', key='t33_x2')

    bias_t3 = st.slider('Sesgo', 0., 5., 2.5, key='t3_b')
    #st.write("I'm ", age, 'years old')

    # If button is pressed
    if st.button("Calcular la salida", key='submit_tab3'):
        # Calculo de resultado
        salida_tab3 = peso_t31 * entrada_t31 + peso_t32 * entrada_t32 + peso_t33 * entrada_t33 + bias_t3
        st.text(f"La salida de la neurona es {salida_tab3}")
