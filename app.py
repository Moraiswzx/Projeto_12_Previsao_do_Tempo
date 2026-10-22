import streamlit as st
from dados_api import previsao_temperatura

# Cidades
cidades = {
    "Berlim" : [52.52472990015798, 13.404144710329106 ],
    "Tóquio" : [35.71956932601952, 139.78334788318642],
    "Denver" : [39.73773219672083, -104.99209317859481],
    "Rio de Janeiro" : [-22.91311627504152, -43.19575025609735],
    "Moscou" : [55.78435195702379, 37.61856861684324],
    "Nairóbi" : [-1.2915376142150232, 36.81958407391947]
}





# ------------------------- SIDEBAR
st.sidebar.title("Previsão do tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude , longitude = cidades[cidade]


# ------------------------- BODY
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)


for i, d in temperatura_media.iterrows():
    # st.write(d['dia'], d['mes'], d['temperatura_media'])
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}º")

        with col3:
            if d['temperatura_media'] < 10:
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "warm.png"

            st.image(temp, width=40)

            

