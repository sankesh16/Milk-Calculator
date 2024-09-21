import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Milk Calculator",
    page_icon="🐄",
)

# Custom CSS to hide Streamlit branding and menu
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton{visibility: hidden;}
    </style>
    """

st.markdown(hide_menu_style, unsafe_allow_html=True)

st.logo('images/aavin.png')
st.header('Milk Calculator', divider=True)

container = st.container(border=True)

price = container.text_input(f"Enter Price Per Packet", placeholder=0)

default = []
extras = []

container = st.container(border=True)

col1, col2 = container.columns(2)
for i in range(1,32):
    days = col1.text_input(f"Day - {i}", 3)
    extra = col2.text_input(f"Day - {i} Extra", placeholder=0)
    if days:
        default.append(int(days))
    else:
        default.append(0)
    if extra:
        extras.append(int(extra))
    else:
        extras.append(0)

dd_default = sum(default)
dd_extra = sum(extras)


if(st.button("Submit", type='primary')):
    if price:
        dd_default_price = dd_default * float(price)
        dd_extra_price = dd_extra * float(price)
        total_price = dd_default_price + dd_extra_price
        if float(price)>0:

            container = st.container(border=True)

            container.info(f'Price Per Packet: {float(price):.2f}')
            container.info(f'Number of default: {dd_default}')
            container.info(f'Number of extra: {dd_extra}')
            container.info(f'Number of default_price: {float(dd_default_price):.2f}')
            container.info(f'Number of extra_price: {float(dd_extra_price):.2f}')
            container.success(f'Total Price: {float(total_price):.2f}')
        else:
            st.error('Enter Price Per Packet')
    else:
            st.error('Enter Price Per Packet')



overall_packets = [a + b for a, b in zip(extras, default)]
days_in_month = [int(i) for i in range(1,32)]
df = pd.DataFrame(
    {'day':days_in_month, 'packet':overall_packets}
)
container = st.container(border=True)

container.line_chart(df,x='day', y='packet', x_label='Days', y_label='Packets',color=["#1A00F9"])

