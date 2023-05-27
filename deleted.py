col9, col10, col11, col12, col13 = st.columns([1, 1, 0.5, 1, 1])

df = pandas.read_csv('files/education.csv', sep=';')

with col9:
    for index, row in df.iterrows():
        st.write(row['name'])


with col10:
    for index, row in df.iterrows():
        st.write(row['f'])
with col11:
    for index, row in df.iterrows():
        st.write(row['year'])
