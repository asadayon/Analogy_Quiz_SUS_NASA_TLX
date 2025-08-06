import streamlit as st
import random
import matplotlib.pyplot as plt
#import mysql.connector
#from mysql.connector import Error

def load_questions(who):
    if who=='Amina Rahman':
        return [
    {
        "question": "How can text similarity-based models be used in an advisor recommender system for Amina Rahman’s research interests?",
        "options": [
            "By analyzing personality traits of Amina and advisors to find the best match",
            "By comparing textual descriptions of context-aware mobile systems and adaptive applications from Amina and advisors to find the best alignment",
            "By ranking advisors based on their publication count in mobile phone technologies",
            "By considering the geographical location of Amina and advisors for recommendations"
        ],
        "answer": "By comparing textual descriptions of context-aware mobile systems and adaptive applications from Amina and advisors to find the best alignment",
        "question_number": 1
    },
    {
        "question": "What is the primary goal of using cosine similarity in an advisor recommendation system for Amina Rahman’s research? For example, if Amina’s keywords include 'context-aware systems' and 'adaptive mobile apps,' the system identifies advisors with similar keywords in their profiles.",
        "options": [
            "To find the shortest path between mobile technology topics",
            "To measure the similarity between Amina’s keywords (e.g., context-aware systems, adaptive mobile apps) and advisors’ research profiles",
            "To classify mobile user experience techniques into predefined categories",
            "To generate random advisor-student pairings for resource-constrained device research"
        ],
        "answer": "To measure the similarity between Amina’s keywords (e.g., context-aware systems, adaptive mobile apps) and advisors’ research profiles",
        "question_number": 2,
        "explanation": "Feature-Based: The system recommends advisors whose publication keywords (e.g., 'context-aware systems,' 'adaptive mobile apps') closely match Amina’s, as measured by cosine similarity."
    },
    {
        "question": "How is cosine similarity calculated between two vectors representing Amina’s and an advisor’s research interests in mobile adaptive systems?",
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
        "question": "Which of the following is true about cosine similarity when used for matching Amina’s interest in adaptive mobile apps with advisors? For instance, if Amina’s keywords are longer than an advisor’s, cosine similarity still compares their alignment effectively.",
        "options": [
            "It only works with binary data",
            "It ranges from -1 to 1, where 1 means completely dissimilar",
            "It is not affected by the length of the keyword vectors",
            "It is computationally intensive and not suitable for large datasets"
        ],
        "answer": "It is not affected by the length of the keyword vectors",
        "question_number": 4,
        "explanation": "Feature-Based: Cosine similarity focuses on the angle between vectors, so it effectively compares Amina’s keywords (e.g., 'adaptive mobile apps,' 'context-aware systems') with advisors’ profiles regardless of vector length."
    },
    {
        "question": "Why is it important to preprocess Amina’s research keywords (e.g., 'context-aware systems,' 'adaptive mobile apps,' 'resource-constrained devices') before applying cosine similarity?",
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
        "question": "Which preprocessing step is commonly applied to Amina’s research keywords before computing cosine similarity for advisor recommendations?",
        "options": [
            "Tokenization of terms like 'context-aware systems'",
            "Vector normalization of keyword counts",
            "Stop word removal from research descriptions",
            "All of the above"
        ],
        "answer": "All of the above",
        "question_number": 6
    },
    {
        "question": "What does a cosine similarity score of 1 indicate when matching Amina’s interest in context-aware mobile systems with an advisor? For example, if Amina’s keywords exactly match an advisor’s, the system recommends that advisor as a perfect fit.",
        "options": [
            "Amina’s and the advisor’s research interests in context-aware mobile systems are identical",
            "Amina’s and the advisor’s research interests are completely different",
            "Amina’s and the advisor’s research interests are orthogonal",
            "The cosine similarity score is invalid for this context"
        ],
        "answer": "Amina’s and the advisor’s research interests in context-aware mobile systems are identical",
        "question_number": 7,
        "explanation": "Feature-Based: A score of 1 means the advisor’s publications have the same keywords (e.g., 'context-aware systems,' 'adaptive mobile apps') as Amina’s input, indicating a perfect alignment."
    },
    {
        "question": "Why might cosine similarity be preferred over Euclidean distance for matching Amina’s mobile technology interests with advisors? If Amina’s keywords were 'mobile user experience' instead, Euclidean distance might penalize advisors with more publications.",
        "options": [
            "Because it is less affected by the size of the keyword vectors",
            "Because it considers the absolute positions of keywords",
            "Because it only works with large datasets of mobile technology research",
            "Because it is easier to interpret than other measures"
        ],
        "answer": "Because it is less affected by the size of the keyword vectors",
        "question_number": 8,
        "explanation": "Counterfactual-Based: If Amina’s keywords were 'mobile user experience,' Euclidean distance might lower similarity scores for advisors with more publications due to vector magnitude differences, whereas cosine similarity focuses on direction."
    },
    {
        "question": "Consider the research interests: [Context-Aware Systems, Adaptive Mobile Apps, Resource-Constrained Devices, Mobile User Experience, Machine Learning for Mobile, IoT Integration]. Amina Rahman’s interests are: [Context-Aware Systems, Adaptive Mobile Apps, Resource-Constrained Devices]. What is her vector representation?",
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
        "question": "Suppose Amina’s research interest vector is: [1,1,1,0,0]. Given advisor vectors: Advisor A: [1,0,1,1,0], Advisor B: [1,1,1,0,1], Advisor C: [0,1,0,1,1], Advisor D: [1,1,1,0,0]. Which advisor is most similar to Amina based on cosine similarity? The system recommends Advisor D because their keywords match exactly.",
        "options": [
            "Advisor A",
            "Advisor B",
            "Advisor C",
            "Advisor D"
        ],
        "answer": "Advisor D",
        "question_number": 10,
        "explanation": "Feature-Based: Advisor D’s vector [1,1,1,0,0] matches Amina’s exactly, yielding a cosine similarity of 1, as their research interests (context-aware systems, adaptive mobile apps, resource-constrained devices) are identical."
    },
    {
        "question": "Suppose Amina’s research interest vector for mobile technologies is [1,1,1,0] and Advisor X’s vector is [1,1,0,1]. What is the cosine similarity between Amina and Advisor X? If Amina omitted 'resource-constrained devices,' the similarity might increase.",
        "options": [
            "0.2",
            "0",
            "0.82",
            "0.87"
        ],
        "answer": "0.82",
        "question_number": 11,
        "explanation": "Counterfactual-Based: Cosine similarity is 2/(sqrt(3)*sqrt(2)) ≈ 0.82. If Amina’s vector were [1,1,0,0] (omitting 'resource-constrained devices'), the similarity with Advisor X would increase to 1.0, as the vectors would be identical."
    },
    {
        "question": "In the context of topic similarity search for Amina’s research, what is a 'topic'?",
        "options": [
            "A specific research paper on adaptive mobile apps",
            "A set of keywords representing areas like context-aware systems or resource-constrained devices",
            "The title of Amina’s Ph.D. proposal",
            "A list of publications by an advisor on mobile user experience"
        ],
        "answer": "A set of keywords representing areas like context-aware systems or resource-constrained devices",
        "question_number": 12
    },
    {
        "question": "How does Latent Dirichlet Allocation (LDA) help in matching Amina with advisors researching adaptive mobile apps? For example, it identifies topics like 'context-aware computing' in advisors’ publications.",
        "options": [
            "By classifying mobile apps into predefined categories",
            "By calculating the sentiment of mobile technology publications",
            "By predicting the next keyword in Amina’s research description",
            "By identifying underlying topics in context-aware systems and adaptive mobile app publications"
        ],
        "answer": "By identifying underlying topics in context-aware systems and adaptive mobile app publications",
        "question_number": 13,
        "explanation": "Feature-Based: LDA extracts topics such as 'context-aware computing' or 'adaptive mobile apps' from advisors’ publication data, enabling the system to match Amina with advisors whose topic distributions align with hers."
    },
    {
        "question": "What type of input data is required for topic similarity search using LDA to match Amina with advisors?",
        "options": [
            "Numerical data representing mobile device battery usage",
            "Keywords representing Amina’s and advisors’ interests in context-aware systems and adaptive mobile apps",
            "Images of mobile app interfaces",
            "Audio recordings of lectures on mobile user experience"
        ],
        "answer": "Keywords representing Amina’s and advisors’ interests in context-aware systems and adaptive mobile apps",
        "question_number": 14
    },
    {
        "question": "Why is it important to preprocess Amina’s keywords like 'context-aware systems' and 'adaptive mobile apps' before applying LDA?",
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
        "question": "What is the output of the LDA model when recommending advisors for Amina’s mobile technology research? For example, it assigns a topic distribution like [0.5, 0.3, 0.2] to an advisor’s profile.",
        "options": [
            "A single topic label for each of Amina’s keywords",
            "A ranked list of advisors for Amina based on mobile technology topics",
            "A probability distribution of topics for each publication or profile",
            "A list of recommended mobile user experience research papers"
        ],
        "answer": "A probability distribution of topics for each publication or profile",
        "question_number": 16,
        "explanation": "Feature-Based: The LDA model outputs topic distributions (e.g., [0.5, 0.3, 0.2] for context-aware systems, adaptive mobile apps, resource-constrained devices) for advisors’ profiles, which are compared to Amina’s topic distribution to find matches."
    },
    {
        "question": "What is a potential challenge when using LDA to match Amina with advisors studying resource-constrained devices?",
        "options": [
            "LDA requires labeled data for training mobile technology topics",
            "Determining the optimal number of topics for mobile technology research",
            "LDA is only effective with small datasets of adaptive mobile app papers",
            "Ensuring all mobile technology keywords are unique"
        ],
        "answer": "Determining the optimal number of topics for mobile technology research",
        "question_number": 17
    },
    {
        "question": "Why is it important to choose an appropriate number of topics in LDA for Amina’s advisor recommendation? If too few topics are chosen, 'resource-constrained devices' might merge with 'context-aware systems.'",
        "options": [
            "To ensure the model runs faster for mobile technology analysis",
            "To minimize the number of publications needed",
            "To balance between specificity (e.g., resource-constrained devices) and generality (e.g., mobile technology)",
            "To increase the number of keywords in each publication"
        ],
        "answer": "To balance between specificity (e.g., resource-constrained devices) and generality (e.g., mobile technology)",
        "question_number": 18,
        "explanation": "Counterfactual-Based: If only two topics are used, specific areas like 'resource-constrained devices' might be lumped with 'context-aware systems,' reducing the system’s ability to distinguish advisors with precise expertise."
    },
    {
        "question": "How does LDA represent Amina’s research document on adaptive mobile apps in the corpus?",
        "options": [
            "As a single topic like resource-constrained devices",
            "As a mixture of topics (e.g., context-aware systems, adaptive mobile apps) with different proportions",
            "As a random collection of mobile-related keywords",
            "As a sequence of mobile app code snippets"
        ],
        "answer": "As a mixture of topics (e.g., context-aware systems, adaptive mobile apps) with different proportions",
        "question_number": 19
    },
    {
        "question": "If LDA identifies that Amina’s research document has a topic proportion of [0.6, 0.2, 0.2] for topics related to context-aware systems, adaptive mobile apps, and resource-constrained devices, what can be inferred? The system prioritizes advisors with high 'context-aware systems' topic scores.",
        "options": [
            "Amina is mostly interested in the context-aware systems topic",
            "Amina has equal interest in all mobile-related topics",
            "Amina is least interested in the context-aware systems topic",
            "Amina’s interests are not related to any identified topics"
        ],
        "answer": "Amina is mostly interested in the context-aware systems topic",
        "question_number": 20,
        "explanation": "Feature-Based: The high proportion (0.6) for 'context-aware systems' indicates Amina’s primary interest, so the system recommends advisors with similar topic distributions."
    },
    {
        "question": "Amina’s topic distribution is [0.25, 0.25, 0.5] for context-aware systems, adaptive mobile apps, and resource-constrained devices. Which advisor’s topic distribution is the best match? If Amina’s distribution were [0.1, 0.1, 0.8], the best match might differ.",
        "options": [
            "[0.2, 0.8, 0.5]",
            "[0.4, 0.4, 0.2]",
            "[0.1, 0.5, 0.4]",
            "[0.3, 0.2, 0.5]"
        ],
        "answer": "[0.3, 0.2, 0.5]",
        "question_number": 21,
        "explanation": "Counterfactual-Based: The advisor with [0.3, 0.2, 0.5] is closest to Amina’s [0.25, 0.25, 0.5], especially in the dominant 'resource-constrained devices' topic. If Amina’s distribution were [0.1, 0.1, 0.8], an advisor with a higher 'resource-constrained devices' proportion (e.g., [0.2, 0.8, 0.5]) might be preferred."
    },
    {
        "question": "If a keyword like 'adaptive mobile apps' has a topic distribution of [0.3, 0.4, 0.3] across context-aware systems, adaptive mobile apps, and resource-constrained devices, and appears 10 times in Amina’s document, how many times is it expected to belong to the 'adaptive mobile apps' topic?",
        "options": [
            "3",
            "4",
            "5",
            "6"
        ],
        "answer": "4",
        "question_number": 22,
        "explanation": "Feature-Based: The keyword’s 0.4 proportion for 'adaptive mobile apps' means 0.4 * 10 = 4 occurrences are expected to belong to that topic."
    }
]
    elif who=='Emily Zhang':
        return [
    {
        "question": "How can text similarity-based models be used in an advisor recommender system for Emily Zhang’s research interests?",
        "options": [
            "By analyzing personality traits of Emily and advisors to find the best match",
            "By comparing textual descriptions of software process improvement and software quality assurance interests from Emily and advisors to find the best alignment",
            "By ranking advisors based on their publication count in software engineering",
            "By considering the geographical location of Emily and advisors for recommendations"
        ],
        "answer": "By comparing textual descriptions of software process improvement and software quality assurance interests from Emily and advisors to find the best alignment",
        "question_number": 1
    },
    {
        "question": "What is the primary goal of using cosine similarity in an advisor recommendation system for Emily Zhang’s research? For example, if Emily’s keywords include 'software process improvement' and 'design debt,' the system identifies advisors with similar keywords in their profiles.",
        "options": [
            "To find the shortest path between software engineering topics",
            "To measure the similarity between Emily’s keywords (e.g., software process improvement, design debt) and advisors’ research profiles",
            "To classify software quality assurance techniques into predefined categories",
            "To generate random advisor-student pairings for software evolution research"
        ],
        "answer": "To measure the similarity between Emily’s keywords (e.g., software process improvement, design debt) and advisors’ research profiles",
        "question_number": 2,
        "explanation": "Feature-Based: The system recommends advisors whose publication keywords (e.g., 'software process improvement,' 'design debt') closely match Emily’s, as measured by cosine similarity."
    },
    {
        "question": "How is cosine similarity calculated between two vectors representing Emily’s and an advisor’s research interests in software engineering?",
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
        "question": "Which of the following is true about cosine similarity when used for matching Emily’s interest in software quality assurance with advisors? For instance, if Emily’s keywords are longer than an advisor’s, cosine similarity still compares their alignment effectively.",
        "options": [
            "It only works with binary data",
            "It ranges from -1 to 1, where 1 means completely dissimilar",
            "It is not affected by the length of the keyword vectors",
            "It is computationally intensive and not suitable for large datasets"
        ],
        "answer": "It is not affected by the length of the keyword vectors",
        "question_number": 4,
        "explanation": "Feature-Based: Cosine similarity focuses on the angle between vectors, so it effectively compares Emily’s keywords (e.g., 'software quality assurance,' 'design debt') with advisors’ profiles regardless of vector length."
    },
    {
        "question": "Why is it important to preprocess Emily’s research keywords (e.g., 'software process improvement,' 'software system evolution,' 'design debt') before applying cosine similarity?",
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
        "question": "Which preprocessing step is commonly applied to Emily’s research keywords before computing cosine similarity for advisor recommendations?",
        "options": [
            "Tokenization of terms like 'design debt'",
            "Vector normalization of keyword counts",
            "Stop word removal from research descriptions",
            "All of the above"
        ],
        "answer": "All of the above",
        "question_number": 6
    },
    {
        "question": "What does a cosine similarity score of 1 indicate when matching Emily’s interest in software system evolution with an advisor? For example, if Emily’s keywords exactly match an advisor’s, the system recommends that advisor as a perfect fit.",
        "options": [
            "Emily’s and the advisor’s research interests in software system evolution are identical",
            "Emily’s and the advisor’s research interests are completely different",
            "Emily’s and the advisor’s research interests are orthogonal",
            "The cosine similarity score is invalid for this context"
        ],
        "answer": "Emily’s and the advisor’s research interests in software system evolution are identical",
        "question_number": 7,
        "explanation": "Feature-Based: A score of 1 means the advisor’s publications have the same keywords (e.g., 'software system evolution,' 'design debt') as Emily’s input, indicating a perfect alignment."
    },
    {
        "question": "Why might cosine similarity be preferred over Euclidean distance for matching Emily’s software engineering interests with advisors? If Emily’s keywords were 'software testing' instead, Euclidean distance might penalize advisors with more publications.",
        "options": [
            "Because it is less affected by the size of the keyword vectors",
            "Because it considers the absolute positions of keywords",
            "Because it only works with large datasets of software engineering research",
            "Because it is easier to interpret than other measures"
        ],
        "answer": "Because it is less affected by the size of the keyword vectors",
        "question_number": 8,
        "explanation": "Counterfactual-Based: If Emily’s keywords were 'software testing,' Euclidean distance might lower similarity scores for advisors with more publications due to vector magnitude differences, whereas cosine similarity focuses on direction."
    },
    {
        "question": "Consider the research interests: [Software Process Improvement, Software System Evolution, Software Quality Assurance, Design Debt, Software Testing, Agile Development]. Emily Zhang’s interests are: [Software Process Improvement, Software System Evolution, Design Debt]. What is her vector representation?",
        "options": [
            "[1,1,1,0,0,0]",
            "[1,1,0,1,0,0]",
            "[0,1,0,1,1,0]",
            "[1,0,1,0,0,1]"
        ],
        "answer": "[1,1,0,1,0,0]",
        "question_number": 9
    },
    {
        "question": "Suppose Emily’s research interest vector is: [1,1,0,1,0]. Given advisor vectors: Advisor A: [1,0,1,1,0], Advisor B: [1,1,0,1,1], Advisor C: [0,1,0,1,1], Advisor D: [1,1,0,1,0]. Which advisor is most similar to Emily based on cosine similarity? The system recommends Advisor D because their keywords match exactly.",
        "options": [
            "Advisor A",
            "Advisor B",
            "Advisor C",
            "Advisor D"
        ],
        "answer": "Advisor D",
        "question_number": 10,
        "explanation": "Feature-Based: Advisor D’s vector [1,1,0,1,0] matches Emily’s exactly, yielding a cosine similarity of 1, as their research interests (software process improvement, software system evolution, design debt) are identical."
    },
    {
        "question": "Suppose Emily’s research interest vector for software engineering is [1,1,0,1] and Advisor X’s vector is [1,1,0,0]. What is the cosine similarity between Emily and Advisor X? If Emily omitted 'design debt,' the similarity might increase.",
        "options": [
            "0.2",
            "0",
            "0.82",
            "0.87"
        ],
        "answer": "0.82",
        "question_number": 11,
        "explanation": "Counterfactual-Based: Cosine similarity is 2/(sqrt(3)*sqrt(2)) ≈ 0.82. If Emily’s vector were [1,1,0,0] (omitting 'design debt'), the similarity with Advisor X would increase to 1.0, as the vectors would be identical."
    },
    {
        "question": "In the context of topic similarity search for Emily’s research, what is a 'topic'?",
        "options": [
            "A specific research paper on design debt",
            "A set of keywords representing areas like software process improvement or software quality assurance",
            "The title of Emily’s Ph.D. proposal",
            "A list of publications by an advisor on software evolution"
        ],
        "answer": "A set of keywords representing areas like software process improvement or software quality assurance",
        "question_number": 12
    },
    {
        "question": "How does Latent Dirichlet Allocation (LDA) help in matching Emily with advisors researching software system evolution? For example, it identifies topics like 'design debt' in advisors’ publications.",
        "options": [
            "By classifying software systems into predefined categories",
            "By calculating the sentiment of software engineering publications",
            "By predicting the next keyword in Emily’s research description",
            "By identifying underlying topics in software process improvement and software evolution publications"
        ],
        "answer": "By identifying underlying topics in software process improvement and software evolution publications",
        "question_number": 13,
        "explanation": "Feature-Based: LDA extracts topics such as 'design debt' or 'software system evolution' from advisors’ publication data, enabling the system to match Emily with advisors whose topic distributions align with hers."
    },
    {
        "question": "What type of input data is required for topic similarity search using LDA to match Emily with advisors?",
        "options": [
            "Numerical data representing software bug counts",
            "Keywords representing Emily’s and advisors’ interests in software process improvement and design debt",
            "Images of software architecture diagrams",
            "Audio recordings of lectures on software quality assurance"
        ],
        "answer": "Keywords representing Emily’s and advisors’ interests in software process improvement and design debt",
        "question_number": 14
    },
    {
        "question": "Why is it important to preprocess Emily’s keywords like 'software system evolution' and 'design debt' before applying LDA?",
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
        "question": "What is the output of the LDA model when recommending advisors for Emily’s software engineering research? For example, it assigns a topic distribution like [0.5, 0.3, 0.2] to an advisor’s profile.",
        "options": [
            "A single topic label for each of Emily’s keywords",
            "A ranked list of advisors for Emily based on software engineering topics",
            "A probability distribution of topics for each publication or profile",
            "A list of recommended software quality assurance research papers"
        ],
        "answer": "A probability distribution of topics for each publication or profile",
        "question_number": 16,
        "explanation": "Feature-Based: The LDA model outputs topic distributions (e.g., [0.5, 0.3, 0.2] for software process improvement, software system evolution, design debt) for advisors’ profiles, which are compared to Emily’s topic distribution to find matches."
    },
    {
        "question": "What is a potential challenge when using LDA to match Emily with advisors studying software quality assurance?",
        "options": [
            "LDA requires labeled data for training software engineering topics",
            "Determining the optimal number of topics for software engineering research",
            "LDA is only effective with small datasets of software evolution papers",
            "Ensuring all software engineering keywords are unique"
        ],
        "answer": "Determining the optimal number of topics for software engineering research",
        "question_number": 17
    },
    {
        "question": "Why is it important to choose an appropriate number of topics in LDA for Emily’s advisor recommendation? If too few topics are chosen, 'design debt' might merge with 'software process improvement.'",
        "options": [
            "To ensure the model runs faster for software engineering analysis",
            "To minimize the number of publications needed",
            "To balance between specificity (e.g., design debt) and generality (e.g., software engineering)",
            "To increase the number of keywords in each publication"
        ],
        "answer": "To balance between specificity (e.g., design debt) and generality (e.g., software engineering)",
        "question_number": 18,
        "explanation": "Counterfactual-Based: If only two topics are used, specific areas like 'design debt' might be lumped with 'software process improvement,' reducing the system’s ability to distinguish advisors with precise expertise."
    },
    {
        "question": "How does LDA represent Emily’s research document on software system evolution in the corpus?",
        "options": [
            "As a single topic like design debt",
            "As a mixture of topics (e.g., software process improvement, software system evolution) with different proportions",
            "As a random collection of software-related keywords",
            "As a sequence of software code snippets"
        ],
        "answer": "As a mixture of topics (e.g., software process improvement, software system evolution) with different proportions",
        "question_number": 19
    },
    {
        "question": "If LDA identifies that Emily’s research document has a topic proportion of [0.6, 0.2, 0.2] for topics related to software process improvement, software system evolution, and design debt, what can be inferred? The system prioritizes advisors with high 'software process improvement' topic scores.",
        "options": [
            "Emily is mostly interested in the software process improvement topic",
            "Emily has equal interest in all software-related topics",
            "Emily is least interested in the software process improvement topic",
            "Emily’s interests are not related to any identified topics"
        ],
        "answer": "Emily is mostly interested in the software process improvement topic",
        "question_number": 20,
        "explanation": "Feature-Based: The high proportion (0.6) for 'software process improvement' indicates Emily’s primary interest, so the system recommends advisors with similar topic distributions."
    },
    {
        "question": "Emily’s topic distribution is [0.25, 0.25, 0.5] for software process improvement, software system evolution, and design debt. Which advisor’s topic distribution is the best match? If Emily’s distribution were [0.1, 0.1, 0.8], the best match might differ.",
        "options": [
            "[0.2, 0.8, 0.5]",
            "[0.4, 0.4, 0.2]",
            "[0.1, 0.5, 0.4]",
            "[0.3, 0.2, 0.5]"
        ],
        "answer": "[0.3, 0.2, 0.5]",
        "question_number": 21,
        "explanation": "Counterfactual-Based: The advisor with [0.3, 0.2, 0.5] is closest to Emily’s [0.25, 0.25, 0.5], especially in the dominant 'design debt' topic. If Emily’s distribution were [0.1, 0.1, 0.8], an advisor with a higher 'design debt' proportion (e.g., [0.2, 0.8, 0.5]) might be preferred."
    },
    {
        "question": "If a keyword like 'design debt' has a topic distribution of [0.3, 0.4, 0.3] across software process improvement, software system evolution, and design debt, and appears 10 times in Emily’s document, how many times is it expected to belong to the 'software system evolution' topic?",
        "options": [
            "3",
            "4",
            "5",
            "6"
        ],
        "answer": "4",
        "question_number": 22,
        "explanation": "Feature-Based: The keyword’s 0.4 proportion for 'software system evolution' means 0.4 * 10 = 4 occurrences are expected to belong to that topic."
    }
]
    elif who=='David Chen':
        return [
    {
        "question": "How can text similarity-based models be used in an advisor recommender system for David Chen’s research interests?",
        "options": [
            "By analyzing personality traits of David and advisors to find the best match",
            "By comparing textual descriptions of autonomous robot and multi-robot system interests from David and advisors to find the best alignment",
            "By ranking advisors based on their publication count in rescue robotics",
            "By considering the geographical location of David and advisors for recommendations"
        ],
        "answer": "By comparing textual descriptions of autonomous robot and multi-robot system interests from David and advisors to find the best alignment",
        "question_number": 1
    },
    {
        "question": "What is the primary goal of using cosine similarity in an advisor recommendation system for David Chen’s research? For example, if David’s keywords include 'autonomous robots' and 'multi-robot systems,' the system identifies advisors with similar keywords in their profiles.",
        "options": [
            "To find the shortest path between rescue robotics topics",
            "To measure the similarity between David’s keywords (e.g., autonomous robots, multi-robot systems) and advisors’ research profiles",
            "To classify rescue robot techniques into predefined categories",
            "To generate random advisor-student pairings for tele-operation research"
        ],
        "answer": "To measure the similarity between David’s keywords (e.g., autonomous robots, multi-robot systems) and advisors’ research profiles",
        "question_number": 2,
        "explanation": "Feature-Based: The system recommends advisors whose publication keywords (e.g., 'autonomous robots,' 'multi-robot systems') closely match David’s, as measured by cosine similarity."
    },
    {
        "question": "How is cosine similarity calculated between two vectors representing David’s and an advisor’s research interests in rescue robotics?",
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
        "question": "Which of the following is true about cosine similarity when used for matching David’s interest in multi-robot systems with advisors? For instance, if David’s keywords are longer than an advisor’s, cosine similarity still compares their alignment effectively.",
        "options": [
            "It only works with binary data",
            "It ranges from -1 to 1, where 1 means completely dissimilar",
            "It is not affected by the length of the keyword vectors",
            "It is computationally intensive and not suitable for large datasets"
        ],
        "answer": "It is not affected by the length of the keyword vectors",
        "question_number": 4,
        "explanation": "Feature-Based: Cosine similarity focuses on the angle between vectors, so it effectively compares David’s keywords (e.g., 'multi-robot systems,' 'tele-operation') with advisors’ profiles regardless of vector length."
    },
    {
        "question": "Why is it important to preprocess David’s research keywords (e.g., 'autonomous robots,' 'multi-robot systems,' 'tele-operation') before applying cosine similarity?",
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
        "question": "Which preprocessing step is commonly applied to David’s research keywords before computing cosine similarity for advisor recommendations?",
        "options": [
            "Tokenization of terms like 'multi-robot systems'",
            "Vector normalization of keyword counts",
            "Stop word removal from research descriptions",
            "All of the above"
        ],
        "answer": "All of the above",
        "question_number": 6
    },
    {
        "question": "What does a cosine similarity score of 1 indicate when matching David’s interest in autonomous robots with an advisor? For example, if David’s keywords exactly match an advisor’s, the system recommends that advisor as a perfect fit.",
        "options": [
            "David’s and the advisor’s research interests in autonomous robots are identical",
            "David’s and the advisor’s research interests are completely different",
            "David’s and the advisor’s research interests are orthogonal",
            "The cosine similarity score is invalid for this context"
        ],
        "answer": "David’s and the advisor’s research interests in autonomous robots are identical",
        "question_number": 7,
        "explanation": "Feature-Based: A score of 1 means the advisor’s publications have the same keywords (e.g., 'autonomous robots,' 'multi-robot systems') as David’s input, indicating a perfect alignment."
    },
    {
        "question": "Why might cosine similarity be preferred over Euclidean distance for matching David’s rescue robotics interests with advisors? If David’s keywords were 'robot navigation' instead, Euclidean distance might penalize advisors with more publications.",
        "options": [
            "Because it is less affected by the size of the keyword vectors",
            "Because it considers the absolute positions of keywords",
            "Because it only works with large datasets of rescue robotics research",
            "Because it is easier to interpret than other measures"
        ],
        "answer": "Because it is less affected by the size of the keyword vectors",
        "question_number": 8,
        "explanation": "Counterfactual-Based: If David’s keywords were 'robot navigation,' Euclidean distance might lower similarity scores for advisors with more publications due to vector magnitude differences, whereas cosine similarity focuses on direction."
    },
    {
        "question": "Consider the research interests: [Autonomous Robots, Multi-Robot Systems, Tele-Operation, Robot Navigation, Swarm Robotics, Disaster Response]. David Chen’s interests are: [Autonomous Robots, Multi-Robot Systems, Tele-Operation]. What is his vector representation?",
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
        "question": "Suppose David’s research interest vector is: [1,1,1,0,0]. Given advisor vectors: Advisor A: [1,0,1,1,0], Advisor B: [1,1,1,0,1], Advisor C: [0,1,0,1,1], Advisor D: [1,1,1,0,0]. Which advisor is most similar to David based on cosine similarity? The system recommends Advisor D because their keywords match exactly.",
        "options": [
            "Advisor A",
            "Advisor B",
            "Advisor C",
            "Advisor D"
        ],
        "answer": "Advisor D",
        "question_number": 10,
        "explanation": "Feature-Based: Advisor D’s vector [1,1,1,0,0] matches David’s exactly, yielding a cosine similarity of 1, as their research interests (autonomous robots, multi-robot systems, tele-operation) are identical."
    },
    {
        "question": "Suppose David’s research interest vector for rescue robotics is [1,1,1,0] and Advisor X’s vector is [1,1,0,1]. What is the cosine similarity between David and Advisor X? If David omitted 'tele-operation,' the similarity might increase.",
        "options": [
            "0.2",
            "0",
            "0.67",
            "0.87"
        ],
        "answer": "0.67",
        "question_number": 11,
        "explanation": "Counterfactual-Based: Cosine similarity is 2/(sqrt(3)*sqrt(3)) ≈ 0.67. If David’s vector were [1,1,0,0] (omitting 'tele-operation'), the similarity with Advisor X would increase to 0.82, as fewer differences exist."
    },
    {
        "question": "In the context of topic similarity search for David’s research, what is a 'topic'?",
        "options": [
            "A specific research paper on rescue robots",
            "A set of keywords representing areas like autonomous robots or multi-robot systems",
            "The title of David’s Ph.D. proposal",
            "A list of publications by an advisor on disaster response"
        ],
        "answer": "A set of keywords representing areas like autonomous robots or multi-robot systems",
        "question_number": 12
    },
    {
        "question": "How does Latent Dirichlet Allocation (LDA) help in matching David with advisors researching multi-robot systems? For example, it identifies topics like 'autonomous navigation' in advisors’ publications.",
        "options": [
            "By classifying robots into predefined categories",
            "By calculating the sentiment of rescue robotics publications",
            "By predicting the next keyword in David’s research description",
            "By identifying underlying topics in autonomous robots and multi-robot system publications"
        ],
        "answer": "By identifying underlying topics in autonomous robots and multi-robot system publications",
        "question_number": 13,
        "explanation": "Feature-Based: LDA extracts topics such as 'autonomous navigation' or 'multi-robot systems' from advisors’ publication data, enabling the system to match David with advisors whose topic distributions align with his."
    },
    {
        "question": "What type of input data is required for topic similarity search using LDA to match David with advisors?",
        "options": [
            "Numerical data representing robot sensor readings",
            "Keywords representing David’s and advisors’ interests in autonomous robots and tele-operation",
            "Images of rescue robots",
            "Audio recordings of lectures on disaster response"
        ],
        "answer": "Keywords representing David’s and advisors’ interests in autonomous robots and tele-operation",
        "question_number": 14
    },
    {
        "question": "Why is it important to preprocess David’s keywords like 'multi-robot systems' and 'tele-operation' before applying LDA?",
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
        "question": "What is the output of the LDA model when recommending advisors for David’s rescue robotics research? For example, it assigns a topic distribution like [0.5, 0.3, 0.2] to an advisor’s profile.",
        "options": [
            "A single topic label for each of David’s keywords",
            "A ranked list of advisors for David based on rescue robotics topics",
            "A probability distribution of topics for each publication or profile",
            "A list of recommended disaster response research papers"
        ],
        "answer": "A probability distribution of topics for each publication or profile",
        "question_number": 16,
        "explanation": "Feature-Based: The LDA model outputs topic distributions (e.g., [0.5, 0.3, 0.2] for autonomous robots, multi-robot systems, tele-operation) for advisors’ profiles, which are compared to David’s topic distribution to find matches."
    },
    {
        "question": "What is a potential challenge when using LDA to match David with advisors studying autonomous robots?",
        "options": [
            "LDA requires labeled data for training rescue robotics topics",
            "Determining the optimal number of topics for rescue robotics research",
            "LDA is only effective with small datasets of disaster response papers",
            "Ensuring all rescue robotics keywords are unique"
        ],
        "answer": "Determining the optimal number of topics for rescue robotics research",
        "question_number": 17
    },
    {
        "question": "Why is it important to choose an appropriate number of topics in LDA for David’s advisor recommendation? If too few topics are chosen, 'multi-robot systems' might merge with 'autonomous robots.'",
        "options": [
            "To ensure the model runs faster for rescue robotics analysis",
            "To minimize the number of publications needed",
            "To balance between specificity (e.g., multi-robot systems) and generality (e.g., rescue robotics)",
            "To increase the number of keywords in each publication"
        ],
        "answer": "To balance between specificity (e.g., multi-robot systems) and generality (e.g., rescue robotics)",
        "question_number": 18,
        "explanation": "Counterfactual-Based: If only two topics are used, specific areas like 'multi-robot systems' might be lumped with 'autonomous robots,' reducing the system’s ability to distinguish advisors with precise expertise."
    },
    {
        "question": "How does LDA represent David’s research document on multi-robot systems in the corpus?",
        "options": [
            "As a single topic like tele-operation",
            "As a mixture of topics (e.g., autonomous robots, multi-robot systems) with different proportions",
            "As a random collection of robot-related keywords",
            "As a sequence of robot sensor data"
        ],
        "answer": "As a mixture of topics (e.g., autonomous robots, multi-robot systems) with different proportions",
        "question_number": 19
    },
    {
        "question": "If LDA identifies that David’s research document has a topic proportion of [0.6, 0.2, 0.2] for topics related to autonomous robots, multi-robot systems, and tele-operation, what can be inferred? The system prioritizes advisors with high 'autonomous robots' topic scores.",
        "options": [
            "David is mostly interested in the autonomous robots topic",
            "David has equal interest in all robot-related topics",
            "David is least interested in the autonomous robots topic",
            "David’s interests are not related to any identified topics"
        ],
        "answer": "David is mostly interested in the autonomous robots topic",
        "question_number": 20,
        "explanation": "Feature-Based: The high proportion (0.6) for 'autonomous robots' indicates David’s primary interest, so the system recommends advisors with similar topic distributions."
    },
    {
        "question": "David’s topic distribution is [0.25, 0.25, 0.5] for autonomous robots, multi-robot systems, and tele-operation. Which advisor’s topic distribution is the best match? If David’s distribution were [0.1, 0.1, 0.8], the best match might differ.",
        "options": [
            "[0.2, 0.8, 0.5]",
            "[0.4, 0.4, 0.2]",
            "[0.1, 0.5, 0.4]",
            "[0.3, 0.2, 0.5]"
        ],
        "answer": "[0.3, 0.2, 0.5]",
        "question_number": 21,
        "explanation": "Counterfactual-Based: The advisor with [0.3, 0.2, 0.5] is closest to David’s [0.25, 0.25, 0.5], especially in the dominant 'tele-operation' topic. If David’s distribution were [0.1, 0.1, 0.8], an advisor with a higher 'tele-operation' proportion (e.g., [0.2, 0.8, 0.5]) might be preferred."
    },
    {
        "question": "If a keyword like 'multi-robot systems' has a topic distribution of [0.3, 0.4, 0.3] across autonomous robots, multi-robot systems, and tele-operation, and appears 10 times in David’s document, how many times is it expected to belong to the 'multi-robot systems' topic?",
        "options": [
            "3",
            "4",
            "5",
            "6"
        ],
        "answer": "4",
        "question_number": 22,
        "explanation": "Feature-Based: The keyword’s 0.4 proportion for 'multi-robot systems' means 0.4 * 10 = 4 occurrences are expected to belong to that topic."
    }
]
    if who=='Sara Lee':
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
    st.title("Quiz")
    st.write(f"**User**: {st.session_state["username"]}")
    st.write(f"**Scenario**: {st.session_state["selected_user"]}")
    st.write("_____________________________________________________")
    


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
        
    #name=st.text_input('Name: ')
    #attempt_num=st.text_input('Attempt Number:')
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
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("Student Advisor Recommender System Quiz")
    user_names=['Emily Zhang', 'Amina Rahman','David Chen', 'Sara Lee']
    selected_user = st.selectbox("Select a student scenario", user_names)
    username = st.text_input("Enter your name")

    if st.button("Start Quiz"):
        st.session_state.page = "quiz"
        questions = load_questions(selected_user)
        st.session_state.shuffled_questions = questions
        st.session_state["selected_user"] = selected_user
        st.session_state["username"] = username.strip()
        st.rerun()
elif st.session_state.page == "quiz":
    run_quiz()
    







