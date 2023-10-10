import streamlit as st
import pandas as pd
import plotly.express as px
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import scipy

df=pd.read_csv('F:\\Data Set\\athlete_events.csv')
region_df=pd.read_csv('F:\\Data Set\\noc_regions.csv')

df=preprocessor.preprocess(df,region_df)
st.sidebar.title("Olympic Analysis")
st.sidebar.image('data:image/png;base64,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'
                 'rDo5vW2NPrUw0MDAwMDAwMDAwMDAwMDAwMDAwMDAweET8D5UZwHQnCdwhAAAAAElFTkSuQmCC')
user_menu=st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise analysis','Athlete-wise analysis')
)

#st.dataframe(df)

if user_menu=='Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country=helper.country_year_list(df)

    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)

    #medal_tally1=helper.medal_tally(df) in starting use its
    medal_tally =helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_country=='Overall' and selected_year=='Overall':
        st.title("Overall Tally")
    if selected_country!='Overall' and selected_year=='Overall':
        st.title(selected_country+" Overall Performance"+"In Olympic")
    if selected_country== 'Overall' and selected_year!='Overall':
        st.title("Medal Tally in  "+str(selected_year)+" Olympic" )
    if selected_country!='Overall' and selected_year!='Overall':
        st.title(selected_country+" Overall Performance In "+str(selected_year))
    st.table(medal_tally)

if user_menu=="Overall Analysis":
    editions=df['Year'].unique().shape[0] - 1  # -1 for 1906 it is not counted
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athletes=df['Name'].unique().shape[0] #Total athlete
    nations=df['region'].unique().shape[0]
    st.title("Top Statistics")
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athlete")
        st.title(athletes)

    nations_over_time2 = helper.data_over_time(df,'region')
    fig=px.line(nations_over_time2,x='Edition',y='region')
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time, x='Edition', y='Event')
    st.title("Events over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(events_over_time, x='Edition', y='Name')
    st.title("Athlete over the years")
    st.plotly_chart(fig)

    st.title("No. Of Events over time( Every Sport)")
    fig,ax=plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax=sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list=df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport=st.selectbox('Select a Sport',sport_list)
    x=helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu=='Country-wise analysis':

    st.title('Country-wise analysis')
    country_list=df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country1=st.sidebar.selectbox("Select a country",country_list)
    country_df=helper.yearwise_medal_tally(df,selected_country1)
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(selected_country1 + " Medal Tally over the years")
    st.plotly_chart(fig)

    pt=helper.country_event_heatmap(df,selected_country1)
    st.title(selected_country1 +" Excels in following  Sports")
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of "+ selected_country1)
    top10_df=helper.most_successful_countrywise(df,selected_country1)
    st.table(top10_df)

if user_menu=='Athlete-wise analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=800,height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    famous_sports = ['Basketball',
                     'Judo', 'Football', 'Tug-Of-War', 'Athletics', 'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions',
                     'Handball', 'Weightlifting', 'Wrestling', 'Water Polo', 'Hockey', 'Rowing', 'Fencing', 'Shooting',
                     'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Golf', 'Softball',
                     'Archery', 'Volleyball', 'Synchronized Swimming',
                     'Table Tennis', 'Baseball', 'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    x = []
    name = []
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(x,name,show_hist=False,show_rug=False)
    fig.update_layout(autosize=False, width=800, height=600)
    st.title('Distribution of Age wrt Sports(Gold Madalist)')
    st.plotly_chart(fig)

    st.title("Height vs Weight")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df=helper.weight_vs_height(df,selected_sport)
    fig,ax=plt.subplots()
    ax=sns.scatterplot(data=temp_df,x='Weight',y='Height',hue='Medal',style='Sex',s=60)
    st.pyplot(fig)

    st.title("Male Vs Female Participation over the Years")
    final=helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=700, height=500)
    st.plotly_chart(fig)