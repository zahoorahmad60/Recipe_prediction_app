import streamlit as st
import data_preprocessor
import matplotlib.pyplot as plt
import helper
import streamlit as st
import seaborn as sns
# Set the page title and style it
st.title("🥗 Recipe Selection Preferences")
st.info("Note:  Model will Predict Top 5 Recipies on the basis of 1. Nutrition's value \n 2.Cuisine Preference \n 3.Other mentioned Factores")
# Create input fields and widgets for stakeholder preferences
st.sidebar.header("Stakeholder Preferences")
cuisine = st.sidebar.selectbox("Cuisine Preference:", ["Any", "Italian", "Mexican", "Asian", "Mediterranean", 'Turkish'])
Italian, Mexican, Asian, Turkish, Mediterranean, other = data_preprocessor.dummy_function()
meal_type = st.sidebar.selectbox("Meal Type:", ["Any", "Breakfast", "Lunch", "Dinner", "Snack"])
nutritions_type = st.sidebar.selectbox("Nutrition Type", ["Any", "medium protein", "High calories", "High Protien", "Mix"])
dietary_restrictions = st.sidebar.multiselect("Dietary Restrictions:", ["Vegetarian", "Vegan", "Gluten-Free", "Low Carb"])
max_prep_time = st.sidebar.slider("Max Preparation Time (minutes):", min_value=0, max_value=500, step=20, value=60)
max_calories_count = st.sidebar.slider("Max max_calories (cal):", min_value=0, max_value=1000,step=20, value=60)
max_protein_count = st.sidebar.slider("Max Protein count (g):", min_value=0, max_value=500, step=20, value=60)
max_fat_count = st.sidebar.slider("Max Fat count (g):", min_value=0, max_value=500, step=20, value=60)

# Create a button to trigger recipe selection based on preferences
data = helper.priority()
st.markdown("""
<style>
.stGrid > div {
    margin-left: 20px;  # Adjust this value as needed
}
</style>
""", unsafe_allow_html=True)
if cuisine == "Italian":
    recipe = Italian

elif cuisine == "Mexican":
    recipe = Mexican
elif cuisine == "Asian":
    recipe = Asian
    # st.dataframe(Asian['title'])
elif cuisine == "Mediterranean":
    recipe = Mediterranean
    # st.dataframe(Mediterranean['title'])
else:
    recipe = other
    # st.dataframe(other['title'])
def display_recipe(recipe):
    st.title(recipe["title"])
    st.subheader("Ingredients")
    st.write(", ".join(recipe["ingredients"]))
    st.subheader("Instructions")
    st.write(recipe["instructions"])
col1, col2 = st.columns(2)
with col1:
    st.title("Top 5 Predicted Recipies")
    new_dataframe = recipe.sample(5)
    information_how_to_cook = new_dataframe[['title', 'directions']]
    title = sorted(new_dataframe['title'])
    st.write(new_dataframe['title'])
    st.markdown("     ")
# col2 = st.columns(1)
with col2:
    st.title("Calories Count")
    fig, ax = plt.subplots()
    ax.bar(new_dataframe['title'], new_dataframe['calories'], color='orange')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.markdown("     ")

col3, col4 = st.columns(2)
with col3:
    st.title("Fat Count")
    fig, ax = plt.subplots()
    ax.bar(new_dataframe['title'], new_dataframe['fat'], color='red')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.markdown("     ")
with col4:
    st.title("Protein Count")
    fig, ax = plt.subplots()
    ax.bar(new_dataframe['title'], new_dataframe['protein'], color='green')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.markdown("     ")
st.title("How to Cook these Recipies")
title = st.sidebar.selectbox("Cooking list", title)
for i in new_dataframe['directions']:
    st.write(i)





