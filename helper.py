from urlextract import  URLExtract
from wordcloud import WordCloud
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import pandas as pd
from collections import Counter
import emoji

ext=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user!='Overall':
        df = df[df['user'] == selected_user]
    num_msgs = df.shape[0]
    words = []
    for msg in df['message']:
        words.extend(msg.split())

    num_media_msg=df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for msg in df['message']:
        links.extend(ext.find_urls(msg))

    return num_msgs, len(words), num_media_msg,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()
    df=df.rename(columns={'user':'name','count':'percent'})
    return x,df

def create_wordcloud(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    wc = WordCloud(width=500, height=500, background_color='white',min_font_size=10)
    dfwc = wc.generate(temp['message'].str.cat(sep=' '))
    return dfwc

def most_common_words(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    stopwords = set(ENGLISH_STOP_WORDS)
    words = []
    for msg in temp['message']:
        for word in msg.lower().split():
            if word not in stopwords:
                words.append(word)
    most_commondf=pd.DataFrame(Counter(words).most_common(20))
    return most_commondf

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis = []
    for msg in df['message']:
        emojis.extend([c for c in msg if emoji.is_emoji(c)])
    emodf=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emodf

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap=df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)
    return user_heatmap