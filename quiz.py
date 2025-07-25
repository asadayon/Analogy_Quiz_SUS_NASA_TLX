import streamlit as st
import random
import matplotlib.pyplot as plt
#import mysql.connector
#from mysql.connector import Error

def load_questions():
    return [
        
    {
        "question": "How can text similarity-based models be used in an advisor recommender system for Sara Lee's research interests?",
        "options": [
            "By analyzing personality traits of Sara and advisors to find the best match",
            "By comparing textual descriptions of web mining and online community analysis interests from Sara and advisors to find the best alignment",
            "By ranking advisors based on their publication count in web spam detection",
            "By considering the geographical location of Sara and advisors for recommendations"
        ],
        "answer": "By comparing textual descriptions of web mining and online community analysis interests from Sara and advisors to find the best alignment",
        "question_number": 1
    },
    {
        "question": "What is the primary goal of using cosine similarity in an advisor recommendation system for Sara Lee's research? For example, if Sara’s keywords include 'web mining' and 'web spam,' the system identifies advisors with similar keywords in their profiles.",
        "options": [
            "To find the shortest path between web mining research topics",
            "To measure the similarity between Sara’s keywords (e.g., web mining, web spam) and advisors’ research profiles",
            "To classify web spam detection techniques into predefined categories",
            "To generate random advisor-student pairings for online community research"
        ],
        "answer": "To measure the similarity between Sara’s keywords (e.g., web mining, web spam) and advisors’ research profiles",
        "question_number": 2,
        "explanation": "Feature-Based: The system recommends advisors whose publication keywords (e.g., 'web mining,' 'web spam detection') closely match Sara’s, as measured by cosine similarity."
    },
    {
        "question": "How is cosine similarity calculated between two vectors representing Sara’s and an advisor’s research interests in web mining?",
        "options": [
            "By adding the magnitudes of the two vectors",
            "By finding the difference between the two vectors",
            "By dividing the dot product of the vectors by the product of their magnitudes",
            "By calculating the Euclidean distance between the vectors"
        ],
        "answer": "By dividing the dot product of the vectors by the product of their magnitudes",
        "question_number": 3
    },
    {
        "question": "Which of the following is true about cosine similarity when used for matching Sara’s interest in web spam detection with advisors? For instance, if Sara’s keywords are longer than an advisor’s, cosine similarity still compares their alignment effectively.",
        "options": [
            "It only works with binary data",
            "It ranges from -1 to 1, where 1 means completely dissimilar",
            "It is not affected by the length of the keyword vectors",
            "It is computationally intensive and not suitable for large datasets"
        ],
        "answer": "It is not affected by the length of the keyword vectors",
        "question_number": 4,
        "explanation": "Feature-Based: Cosine similarity focuses on the angle between vectors, so it effectively compares Sara’s keywords (e.g., 'web spam,' 'online communities') with advisors’ profiles regardless of vector length."
    },
    {
        "question": "Why is it important to preprocess Sara’s research keywords (e.g., 'web mining,' 'online communities,' 'web spam') before applying cosine similarity?",
        "options": [
            "To increase the complexity of the algorithm",
            "To ensure keywords are in a uniform format for accurate comparison",
            "To reduce the dimensionality of the vectors",
            "To encrypt the data for security"
        ],
        "answer": "To ensure keywords are in a uniform format for accurate comparison",
        "question_number": 5
    },
    {
        "question": "Which preprocessing step is commonly applied to Sara’s research keywords before computing cosine similarity for advisor recommendations?",
        "options": [
            "Tokenization of terms like 'web spam'",
            "Vector normalization of keyword counts",
            "Stop word removal from research descriptions",
            "All of the above"
        ],
        "answer": "All of the above",
        "question_number": 6
    },
    {
        "question": "What does a cosine similarity score of 1 indicate when matching Sara’s interest in online community analysis with an advisor? For example, if Sara’s keywords exactly match an advisor’s, the system recommends that advisor as a perfect fit.",
        "options": [
            "Sara’s and the advisor’s research interests in online communities are identical",
            "Sara’s and the advisor’s research interests are completely different",
            "Sara’s and the advisor’s research interests are orthogonal",
            "The cosine similarity score is invalid for this context"
        ],
        "answer": "Sara’s and the advisor’s research interests in online communities are identical",
        "question_number": 7,
        "explanation": "Feature-Based: A score of 1 means the advisor’s publications have the same keywords (e.g., 'online communities,' 'web mining') as Sara’s input, indicating a perfect alignment."
    },
    {
        "question": "Why might cosine similarity be preferred over Euclidean distance for matching Sara’s web mining interests with advisors? If Sara’s keywords were 'data mining' instead, Euclidean distance might penalize advisors with more publications.",
        "options": [
            "Because it is less affected by the size of the keyword vectors",
            "Because it considers the absolute positions of keywords",
            "Because it only works with large datasets of web spam research",
            "Because it is easier to interpret than other measures"
        ],
        "answer": "Because it is less affected by the size of the keyword vectors",
        "question_number": 8,
        "explanation": "Counterfactual-Based: If Sara’s keywords were 'data mining,' Euclidean distance might lower similarity scores for advisors with more publications due to vector magnitude differences, whereas cosine similarity focuses on direction."
    },
    {
        "question": "Consider the research interests: [Web Mining, Online Communities, Web Spam Detection, Search Engine Optimization, Social Network Analysis, Data Mining]. Sara Lee’s interests are: [Web Mining, Online Communities, Web Spam Detection]. What is her vector representation?",
        "options": [
            "[1,1,1,0,0,0]",
            "[1,1,0,1,0,0]",
            "[0,1,0,1,1,0]",
            "[1,0,1,0,0,1]"
        ],
        "answer": "[1,1,1,0,0,0]",
        "question_number": 9
    },
    {
        "question": "Suppose Sara’s research interest vector is: [1,1,1,0,0]. Given advisor vectors: Advisor A: [1,0,1,1,0], Advisor B: [1,1,1,0,1], Advisor C: [0,1,0,1,1], Advisor D: [1,1,1,0,0]. Which advisor is most similar to Sara based on cosine similarity? The system recommends Advisor D because their keywords match exactly.",
        "options": [
            "Advisor A",
            "Advisor B",
            "Advisor C",
            "Advisor D"
        ],
        "answer": "Advisor D",
        "question_number": 10,
        "explanation": "Feature-Based: Advisor D’s vector [1,1,1,0,0] matches Sara’s exactly, yielding a cosine similarity of 1, as their research interests (web mining, online communities, web spam detection) are identical."
    },
    {
        "question": "Suppose Sara’s research interest vector for web mining is [1,1,1,0] and Advisor X’s vector is [1,1,0,1]. What is the cosine similarity between Sara and Advisor X? If Sara omitted 'web spam detection,' the similarity might increase.",
        "options": [
            "0.2",
            "0",
            "0.67",
            "0.87"
        ],
        "answer": "0.67",
        "question_number": 11,
        "explanation": "Counterfactual-Based: Cosine similarity is 2/(sqrt(3)*sqrt(3)) ≈ 0.67. If Sara’s vector were [1,1,0,0] (omitting 'web spam detection'), the similarity with Advisor X would increase to 0.82, as fewer differences exist."
    },
    {
        "question": "In the context of topic similarity search for Sara’s research, what is a 'topic'?",
        "options": [
            "A specific research paper on web spam",
            "A set of keywords representing areas like web mining or online community analysis",
            "The title of Sara’s Ph.D. proposal",
            "A list of publications by an advisor on search engine manipulation"
        ],
        "answer": "A set of keywords representing areas like web mining or online community analysis",
        "question_number": 12
    },
    {
        "question": "How does Latent Dirichlet Allocation (LDA) help in matching Sara with advisors researching online communities? For example, it identifies topics like 'web spam detection' in advisors’ publications.",
        "options": [
            "By classifying websites into predefined categories",
            "By calculating the sentiment of web mining publications",
            "By predicting the next keyword in Sara’s research description",
            "By identifying underlying topics in web mining and online community publications"
        ],
        "answer": "By identifying underlying topics in web mining and online community publications",
        "question_number": 13,
        "explanation": "Feature-Based: LDA extracts topics such as 'web spam detection' or 'online community analysis' from advisors’ publication data, enabling the system to match Sara with advisors whose topic distributions align with hers."
    },
    {
        "question": "What type of input data is required for topic similarity search using LDA to match Sara with advisors?",
        "options": [
            "Numerical data representing website traffic",
            "Keywords representing Sara’s and advisors’ interests in web mining and web spam",
            "Images of spammy websites",
            "Audio recordings of lectures on online communities"
        ],
        "answer": "Keywords representing Sara’s and advisors’ interests in web mining and web spam",
        "question_number": 14
    },
    {
        "question": "Why is it important to preprocess Sara’s keywords like 'web spam' and 'online communities' before applying LDA?",
        "options": [
            "To reduce noise and irrelevant information in the keyword set",
            "To correct grammatical errors in publication titles",
            "To increase the size of the publication dataset",
            "To ensure all keywords are in uppercase"
        ],
        "answer": "To reduce noise and irrelevant information in the keyword set",
        "question_number": 15
    },
    {
        "question": "What is the output of the LDA model when recommending advisors for Sara’s web mining research? For example, it assigns a topic distribution like [0.5, 0.3, 0.2] to an advisor’s profile.",
        "options": [
            "A single topic label for each of Sara’s keywords",
            "A ranked list of advisors for Sara based on web mining topics",
            "A probability distribution of topics for each publication or profile",
            "A list of recommended web spam research papers"
        ],
        "answer": "A probability distribution of topics for each publication or profile",
        "question_number": 16,
        "explanation": "Feature-Based: The LDA model outputs topic distributions (e.g., [0.5, 0.3, 0.2] for web mining, online communities, web spam) for advisors’ profiles, which are compared to Sara’s topic distribution to find matches."
    },
    {
        "question": "What is a potential challenge when using LDA to match Sara with advisors studying spammy website networks?",
        "options": [
            "LDA requires labeled data for training web spam topics",
            "Determining the optimal number of topics for web mining research",
            "LDA is only effective with small datasets of online community papers",
            "Ensuring all web mining keywords are unique"
        ],
        "answer": "Determining the optimal number of topics for web mining research",
        "question_number": 17
    },
    {
        "question": "Why is it important to choose an appropriate number of topics in LDA for Sara’s advisor recommendation? If too few topics are chosen, 'web spam detection' might merge with 'web mining.'",
        "options": [
            "To ensure the model runs faster for web spam analysis",
            "To minimize the number of publications needed",
            "To balance between specificity (e.g., web spam detection) and generality (e.g., web mining)",
            "To increase the number of keywords in each publication"
        ],
        "answer": "To balance between specificity (e.g., web spam detection) and generality (e.g., web mining)",
        "question_number": 18,
        "explanation": "Counterfactual-Based: If only two topics are used, specific areas like 'web spam detection' might be lumped with 'web mining,' reducing the system’s ability to distinguish advisors with precise expertise."
    },
    {
        "question": "How does LDA represent Sara’s research document on online community analysis in the corpus?",
        "options": [
            "As a single topic like web spam detection",
            "As a mixture of topics (e.g., web mining, online communities) with different proportions",
            "As a random collection of web-related keywords",
            "As a sequence of website URLs"
        ],
        "answer": "As a mixture of topics (e.g., web mining, online communities) with different proportions",
        "question_number": 19
    },
    {
        "question": "If LDA identifies that Sara’s research document has a topic proportion of [0.6, 0.2, 0.2] for topics related to web mining, online communities, and web spam, what can be inferred? The system prioritizes advisors with high 'web mining' topic scores.",
        "options": [
            "Sara is mostly interested in the web mining topic",
            "Sara has equal interest in all web-related topics",
            "Sara is least interested in the web mining topic",
            "Sara’s interests are not related to any identified topics"
        ],
        "answer": "Sara is mostly interested in the web mining topic",
        "question_number": 20,
        "explanation": "Feature-Based: The high proportion (0.6) for 'web mining' indicates Sara’s primary interest, so the system recommends advisors with similar topic distributions."
    },
    {
        "question": "Sara’s topic distribution is [0.25, 0.25, 0.5] for web mining, online communities, and web spam detection. Which advisor’s topic distribution is the best match? If Sara’s distribution were [0.1, 0.1, 0.8], the best match might differ.",
        "options": [
            "[0.2, 0.8, 0.5]",
            "[0.4, 0.4, 0.2]",
            "[0.1, 0.5, 0.4]",
            "[0.3, 0.2, 0.5]"
        ],
        "answer": "[0.3, 0.2, 0.5]",
        "question_number": 21,
        "explanation": "Counterfactual-Based: The advisor with [0.3, 0.2, 0.5] is closest to Sara’s [0.25, 0.25, 0.5], especially in the dominant 'web spam detection' topic. If Sara’s distribution were [0.1, 0.1, 0.8], an advisor with a higher 'web spam detection' proportion (e.g., [0.2, 0.8, 0.5]) might be preferred."
    },
    {
        "question": "If a keyword like 'web spam' has a topic distribution of [0.3, 0.4, 0.3] across web mining, online communities, and web spam detection, and appears 10 times in Sara’s document, how many times is it expected to belong to the 'online communities' topic?",
        "options": [
            "3",
            "4",
            "5",
            "6"
        ],
        "answer": "4",
        "question_number": 22,
        "explanation": "Feature-Based: The keyword’s 0.4 proportion for 'online communities' means 0.4 * 10 = 4 occurrences are expected to belong to that topic."
    }

    ]
# Shuffle questions and options once before loading
if "shuffled_questions" not in st.session_state:
    questions = load_questions()
    random.shuffle(questions)
    for question in questions:
        random.shuffle(question["options"])
    st.session_state.shuffled_questions = questions

#def connect_to_db():
 #   return mysql.connector.connect(
 #       host=st.secrets["HOST"],
 #       port=st.secrets["PORT"],
 #       user=st.secrets["USER"],
 #       password=st.secrets["PASSWORD"],
 #       database=st.secrets["DATABASE"]  # Replace with your actual database name
 #   )        
      
    



def run_quiz():
    questions = st.session_state.shuffled_questions

    st.title("Multiple Choice Quiz")

    user_answers = []
    correct_count = 0

    for i, question in enumerate(questions):
        st.write(f"Q{i+1}: {question['question']}")

        user_answer = st.radio(
            "Choose your answer:",
            question["options"],
            index=None,  # No option selected initially
            key=f"question_{i}"
        )
        user_answers.append(user_answer)
        
    name=st.text_input('Name: ')
    attempt_num=st.text_input('Attempt Number:')
    #connection = connect_to_db()
    #cursor = connection.cursor()
    if st.button("Submit"):
        for i, question in enumerate(questions):
            if user_answers[i] == question['answer']:
                correct_count += 1
                st.write(f"Q{i+1}: {question['question']}")
                st.success(f"Your answer: {user_answers[i]}", icon="✔")
            else:
                st.write(f"Q{i+1}: {question['question']}")
                st.error(f"Your answer: {user_answers[i]}", icon="❌")

        total_questions = len(questions)
        score_percentage = (correct_count / total_questions) * 100
        #cursor.execute("INSERT INTO QuizAttempts (user_id, attempt_number, final_score) VALUES (%s, %s, %s)", (name, attempt_num, correct_count))
        #attempt_id=cursor.lastrowid
        #for i, question in enumerate(questions):
        #    cursor.execute("INSERT INTO AttemptDetails (attempt_id, question_number, chosen_option, is_correct) VALUES (%s, %s, %s, %s)",
        #          (attempt_id, question['question_number'], user_answers[i], user_answers[i] == question['answer']))
        
        
        # Display score percentage bar
        fig, ax = plt.subplots(figsize=(8, 1))
        ax.barh(0, score_percentage, color='green', height=0.5)
        ax.barh(0, 100 - score_percentage, left=score_percentage, color='red', height=0.5)
        ax.set_xlim(0, 100)
        ax.axis('off')

        # Annotate the percentage under the bar
        plt.text(50, -0.3, f"Score: {score_percentage:.2f}%", ha='center', va='center', fontsize=12)

        st.pyplot(fig)

        st.write(f"Your raw score is: {correct_count}/{total_questions}")
        st.write(f"Your percentile score is: {score_percentage:.2f}%")
        #connection.commit()
        #cursor.close()
        #connection.close()

# Run the quiz
run_quiz()
