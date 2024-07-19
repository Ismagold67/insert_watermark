import streamlit as st
from PIL import Image, ImageFont, ImageDraw

def text_on_image(image, text, font_size, color):
    img = Image.open(image)
    font = ImageFont.truetype('Roboto-Regular.ttf', font_size)
    draw = ImageDraw.Draw(img)

    iw, ih = img.size
    bbox = draw.textbbox((0, 0), text, font=font)
    fw = bbox[2] - bbox[0]
    fh = bbox[3] - bbox[1]

    draw.text(
        ((iw - fw) / 2, (ih - fh) / 2),
        text,
        fill=color,
        font=font
    )
    img.save('last_image.jpg')

st.title('Adicione uma Marca d\'água à sua Imagem')

image = st.file_uploader('Uma imagem', type=['jpg'])
text = st.text_input('Sua marca d\'água')
color = st.selectbox('Cor da sua marca', ['black', 'white', 'red', 'green'])
font_size = st.number_input('Tamanho da fonte', min_value=50)

if image and text:
    if st.button('Aplicar'):
        text_on_image(image, text, font_size, color)
        st.image('last_image.jpg')
else:
    st.warning('Por favor, envie uma imagem e insira o texto da marca d\'água.')
