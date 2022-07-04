import json

import requests as re
import streamlit as st

url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-07-01&end_date=2022-07-04&detailed=false&api_key=DEMO_KEY"

headers = {"content-type": "application/json"}

# json flatten helper function
def flatten_json(y):
    out = {}

    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + "_")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + "_")
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Header
def header():
    st.set_page_config(page_title="Don't look up!", page_icon="🌱")
    st.markdown("# Don't Look Up!")


# Sidebar defined here
def sideBar():
    with st.sidebar:
        st.markdown("### Socials")
        st.markdown("* [ngmisl.lens](https://lenster.xyz/u/ngmisl.lens)")
        st.markdown("* [ngmisl.twitter](https://twitter.com/ngmisl)")
        st.markdown("* [ngmisl.github](https://github.com/ngmisl/)")


# Total Protocol stats
def pleaseLookup():
    query = """ query """

    r = re.get(url, json={"query": query}, headers=headers)

    json_data = json.loads(r.text)
    flat = flatten_json(json_data)

    st.write(flat)

    st.write(f'{flat["element_count"]}')


# App Layout
def main():
    header()
    sideBar()
    pleaseLookup()


if __name__ == "__main__":
    main()
