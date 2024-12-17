import streamlit as st
from urllib import request

from func import frenchy_format

# https://developer.themoviedb.org/reference/movie-now-playing-list


url = "https://api.themoviedb.org/3/movie/now_playing?language=fr-FR&region=FR"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {st.secrets['TOKEN']}"
}

params = request.Request(url=url, headers=headers)
response = request.urlopen(params).read()
print(type(response))
print(response)


st.title("Les films du moment")

for el in response["results"]:
    st.header(el["title"])
    st.image(f"https://image.tmdb.org/t/p/w500{el['poster_path']}")
    st.subheader(el["overview"])
    st.caption(f"Sortie le {frenchy_format(el['release_date'])}")
    st.divider()
