# Whatsapp-Chat-Analyzer
# 📱 WhatsApp Chat Analyzer (End-to-End Dashboard)

Gain deep insights into your conversations! This project is a comprehensive **WhatsApp Chat Analysis Tool** that transforms exported chat text files into an interactive visual dashboard using **Streamlit**.

---

## 🛠️ The Tech Stack
* **Language:** Python
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas, Regex (Regular Expressions)
* **Visualization:** Matplotlib, Seaborn, WordCloud
* **NLP Tools:** Emoji, URLExtract

---

## 🧠 Key Features & Insights

### 1. Top Statistics
* Total Messages, Total Words, Media Shared, and Links Shared.

### 2. Activity Maps
* **Timeline Analysis:** Monthly and Daily traffic trends.
* **Activity Patterns:** Identify the busiest days of the week and months of the year.
* **Hourly Heatmap:** Visualize when the group/user is most active during the day.

### 3. User-Level Analysis
* **Contribution:** "Most Busy Users" bar chart and percentage breakdown.
* **WordCloud:** A visual representation of the most frequently used terms.
* **Emoji Analysis:** A breakdown of the most used emojis in the chat.
* **Common Words:** Horizontal bar charts of the top 20 most used words (excluding stop words).

---

## 📂 Project Structure
* `App.py`: The main Streamlit entry point for the UI.
* `preprocessor.py`: Uses **Regex** to parse the WhatsApp text format (date, time, user, message).
* `helper.py`: Contains the logic for calculating stats, generating timelines, and extracting emojis.
* `whatsapp-chat-analysis.ipynb`: The original research notebook containing data exploration and logic testing.

---

## 🚀 How to Use

1. **Export Chat:** Open WhatsApp > Go to a Chat > Settings > More > Export Chat (Without Media).
2. **Clone this Repo:**
   ```bash
   git clone [https://github.com/Manaswi9123/Python-DataScience-Fundamentals.git](https://github.com/Manaswi9123/Python-DataScience-Fundamentals.git)

## Install Requirements:

   pip install streamlit pandas matplotlib seaborn wordcloud emoji urlextract  

## Run the App:

   streamlit run App.py

## Upload: 
   Drag and drop your exported .txt file into the sidebar!
