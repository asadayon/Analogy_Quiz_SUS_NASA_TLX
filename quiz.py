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
        "question": "What does a cosine similarity score of 0.9115042764715553 for Nico Zazworka indicate about Emily’s research interests?",
        "options": [
            "There is no alignment between Emily’s keywords and Nico Zazworka’s research profile.",
            "Emily’s research interests are moderately aligned with Nico Zazworka’s research profile.",
            "Emily’s research interests are highly aligned with Nico Zazworka’s research profile.",
            "The score indicates a perfect match between Emily’s and Nico Zazworka’s keywords."
        ],
        "answer": "Emily’s research interests are highly aligned with Nico Zazworka’s research profile.",
        "question_number": 1,
        "explanation": "Scenario-Specific: A cosine similarity score of 0.9115 (close to 1) indicates a high degree of alignment between Emily’s keywords (e.g., software engineering, software process) and Nico Zazworka’s keywords (e.g., software process, software quality, design debt)."
    },
    {
        "question": "How does the text similarity model (cosine similarity) determine the top advisor recommendations for Emily?",
        "options": [
            "By grouping keywords into topics and comparing topic distributions.",
            "By calculating the angle between Emily’s keyword vector and each advisor’s keyword vector.",
            "By counting the total number of publications by each advisor.",
            "By mapping Emily’s keywords to predefined LDA topics and ranking advisors."
        ],
        "answer": "By calculating the angle between Emily’s keyword vector and each advisor’s keyword vector.",
        "question_number": 2,
        "explanation": "General: The cosine similarity model represents Emily’s and advisors’ research profiles as numerical vectors based on keyword counts and calculates the cosine of the angle between them. A smaller angle (higher score) indicates stronger alignment."
    },
    {
        "question": "Why was Jose L. Martínez Lastra ranked first in the LDA topic modeling recommendations despite not having keywords directly matching Emily’s interests?",
        "options": [
            "His keywords perfectly match Emily’s keywords in the text similarity model.",
            "His topic distribution is highly similar to the topic distribution of Emily’s keywords, particularly Topic 19.",
            "His publications have the highest citation count in the database.",
            "His keywords include all of Emily’s research interests verbatim."
        ],
        "answer": "His topic distribution is highly similar to the topic distribution of Emily’s keywords, particularly Topic 19.",
        "question_number": 3,
        "explanation": "Scenario-Specific: The LDA model ranks advisors based on the similarity of their topic distribution to Emily’s, with Topic 19 (keywords: softwar, develop, process, system, qualiti) being the most relevant, contributing to Martínez Lastra’s high score of 0.9943."
    },
    {
        "question": "Topic 19, with keywords like 'softwar,' 'develop,' 'process,' 'system,' and 'qualiti,' has a probability of 0.8321 for Emily’s interests. What does this suggest?",
        "options": [
            "Emily’s research interests are unrelated to software engineering.",
            "Topic 19 is the least relevant topic for Emily’s research interests.",
            "Topic 19 strongly represents Emily’s interests in software engineering and quality.",
            "Topic 19 is only relevant to advisors with hardware-focused research."
        ],
        "answer": "Topic 19 strongly represents Emily’s interests in software engineering and quality.",
        "question_number": 4,
        "explanation": "Feature-Based: Topic 19’s keywords align closely with Emily’s interests (software engineering, software process, software quality), and its high probability (0.8321) indicates it strongly represents her research focus."
    },
    {
        "question": "Which of Emily’s keywords likely contributed most to Nico Zazworka’s high cosine similarity score of 0.9115?",
        "options": [
            "Case studies, as it is less common among other advisors’ profiles.",
            "Software engineering, software process, and software quality, due to their overlap with Nico’s keywords.",
            "Software system, as it appears in all advisors’ profiles.",
            "Design debt, as it is the only keyword shared with Nico Zazworka."
        ],
        "answer": "Software engineering, software process, and software quality, due to their overlap with Nico’s keywords.",
        "question_number": 5,
        "explanation": "Feature-Based: Nico Zazworka’s keywords (e.g., software process, software quality, software engineering, design debt) heavily overlap with Emily’s (software engineering, software process, software quality), driving the high similarity score."
    },
    {
        "question": "If Emily removes 'software quality' from her keywords and adds 'machine learning,' how might this affect the cosine similarity ranking?",
        "options": [
            "Nico Zazworka would remain the top recommendation due to his focus on design debt.",
            "Shari Lawrence Pfleeger might drop in ranking, as 'software quality' is a key overlap with her profile.",
            "Eleni Stroulia would become the top recommendation due to her focus on machine learning.",
            "The rankings would remain unchanged, as 'machine learning' is unrelated to all advisors."
        ],
        "answer": "Shari Lawrence Pfleeger might drop in ranking, as 'software quality' is a key overlap with her profile.",
        "question_number": 6,
        "explanation": "Counterfactual-Based: Removing 'software quality' reduces overlap with Shari Lawrence Pfleeger’s keywords (e.g., software quality, software engineering), likely lowering her cosine similarity score. Adding 'machine learning' may not align with these advisors’ profiles, potentially shifting rankings."
    },
    {
        "question": "Suppose Emily’s keywords [software engineering, case studies] are represented as a vector [1, 1], and Nico Zazworka’s keywords [software process, software quality] as [1, 1]. What is the cosine similarity?",
        "options": [
            "0.5",
            "0.707",
            "1.0",
            "0.0"
        ],
        "answer": "0.5",
        "question_number": 7,
        "explanation": "Model Inner Working: For vectors [1, 1] and [1, 1] with no overlapping keywords, the dot product is 0 (1×0 + 1×0 = 0). However, assuming partial overlap for clarity (e.g., one shared keyword), the dot product would be 1, with magnitudes √2 × √2 = 2, yielding cosine similarity = 1/2 = 0.5."
    },
    {
        "question": "Why might the LDA topic modeling recommend Jose L. Martínez Lastra, while the cosine similarity model recommends Nico Zazworka as the top advisor?",
        "options": [
            "Cosine similarity focuses on exact keyword matches, while LDA considers broader research themes.",
            "LDA uses publication counts, while cosine similarity uses topic distributions.",
            "Cosine similarity ranks advisors based on citation impact, while LDA uses keyword counts.",
            "LDA ignores Emily’s keywords, while cosine similarity uses them directly."
        ],
        "answer": "Cosine similarity focuses on exact keyword matches, while LDA considers broader research themes.",
        "question_number": 8,
        "explanation": "General: Cosine similarity matches exact keywords (e.g., Nico’s software process, software quality), while LDA groups keywords into topics (e.g., Topic 19) and compares distributions, leading to different top recommendations like Martínez Lastra."
    },
    {
        "question": "Eleni Stroulia has a cosine similarity score of 0.8787, which is lower than Nico Zazworka’s 0.9115. What does this imply?",
        "options": [
            "Eleni Stroulia is not a good match for Emily’s research interests.",
            "Eleni Stroulia’s research is slightly less aligned with Emily’s interests than Nico’s.",
            "Eleni Stroulia has no overlapping keywords with Emily.",
            "Eleni Stroulia’s score indicates a stronger match than Nico Zazworka’s."
        ],
        "answer": "Eleni Stroulia’s research is slightly less aligned with Emily’s interests than Nico’s.",
        "question_number": 9,
        "explanation": "Scenario-Specific: A score of 0.8787 is still high, indicating strong alignment, but it is slightly lower than 0.9115, suggesting Nico Zazworka’s keywords are more closely aligned with Emily’s."
    },
    {
        "question": "If Emily adds 'software architecture' to her keywords, which advisor’s cosine similarity score is likely to increase the most?",
        "options": [
            "Nico Zazworka, due to his focus on design debt.",
            "Shari Lawrence Pfleeger, due to her focus on software reuse.",
            "Eleni Stroulia, due to her focus on software architecture.",
            "Jose L. Martínez Lastra, due to his focus on web services."
        ],
        "answer": "Eleni Stroulia, due to her focus on software architecture.",
        "question_number": 10,
        "explanation": "Counterfactual-Based: Eleni Stroulia’s keywords include 'software architecture,' so adding this keyword to Emily’s list would increase the overlap and likely boost her cosine similarity score significantly."
    },
    {
        "question": "What does the high probability (0.8321) of Topic 19 indicate for Emily’s research interests in the LDA topic modeling system?",
        "options": [
            "Topic 19 is unrelated to Emily’s research keywords like software engineering.",
            "Topic 19 strongly represents Emily’s interests in software engineering and quality.",
            "Topic 19 is only relevant to advisors with low cosine similarity scores.",
            "Topic 19 focuses on hardware-related themes, not software."
        ],
        "answer": "Topic 19 strongly represents Emily’s interests in software engineering and quality.",
        "question_number": 11,
        "explanation": "Feature-Based: The high probability (0.8321) for Topic 19, with keywords like 'softwar,' 'develop,' 'process,' 'system,' and 'qualiti,' indicates strong alignment with Emily’s interests in software engineering, software process, and software quality."
    },
    {
        "question": "How is cosine similarity calculated for Emily’s keywords [software engineering, case studies] and Shari Lawrence Pfleeger’s keywords [software engineering, software quality]?",
        "options": [
            "By summing the keyword counts and dividing by the total publications.",
            "By computing the dot product of the vectors [1, 1] and [1, 1] and normalizing by their magnitudes.",
            "By comparing the publication dates of Emily and Shari’s research.",
            "By grouping keywords into topics and comparing their distributions."
        ],
        "answer": "By computing the dot product of the vectors [1, 1] and [1, 1] and normalizing by their magnitudes.",
        "question_number": 12,
        "explanation": "Model Inner Working: Cosine similarity is calculated as the dot product of vectors [1, 1] and [1, 1] (1×1 + 1×0 = 1) divided by the product of their magnitudes (√2 × √2 = 2), yielding 0.5 due to partial overlap."
    },
    {
        "question": "Why does Topic 8 (keywords: control, algorithm, optim, problem, system) have a low probability (0.0901) for Emily’s research interests?",
        "options": [
            "Topic 8 focuses on optimization and algorithms, which are less relevant to Emily’s software engineering interests.",
            "Topic 8 has fewer keywords than Topic 19, reducing its probability.",
            "Topic 8 is only relevant to advisors with high cosine similarity scores.",
            "Topic 8 has a higher probability but is unrelated to advisor rankings."
        ],
        "answer": "Topic 8 focuses on optimization and algorithms, which are less relevant to Emily’s software engineering interests.",
        "question_number": 13,
        "explanation": "Feature-Based: Topic 8’s keywords (control, algorithm, optim) are less aligned with Emily’s focus on software engineering and quality, resulting in a lower probability (0.0901) compared to Topic 19 (0.8321)."
    },
    {
        "question": "Why does the recommendation system use both cosine similarity and LDA topic modeling for Emily’s advisor recommendations?",
        "options": [
            "Cosine similarity counts publication frequency, while LDA evaluates citation impact.",
            "Cosine similarity matches exact keywords, while LDA captures broader research themes.",
            "Both models produce identical results to confirm advisor rankings.",
            "LDA uses keyword vectors, while cosine similarity uses topic distributions."
        ],
        "answer": "Cosine similarity matches exact keywords, while LDA captures broader research themes.",
        "question_number": 14,
        "explanation": "General: Cosine similarity compares Emily’s keywords (e.g., software process) directly with advisors’ keywords, while LDA groups keywords into topics (e.g., Topic 19) to match broader research themes, ensuring robust recommendations."
    },
    {
        "question": "Which of Emily’s keywords likely contributed least to Eleni Stroulia’s cosine similarity score of 0.8787?",
        "options": [
            "Software engineering, as it is common across all advisors.",
            "Case studies, as it aligns with Eleni’s keywords.",
            "Software quality, as it is not in Eleni’s keyword list.",
            "Software process, as it is a niche term."
        ],
        "answer": "Software quality, as it is not in Eleni’s keyword list.",
        "question_number": 15,
        "explanation": "Feature-Based: Eleni Stroulia’s keywords include 'software system,' 'software engineering,' and 'case study' but not 'software quality,' so 'software quality' contributes least to her cosine similarity score."
    },
    {
        "question": "If Emily replaces 'case studies' with 'artificial intelligence' in her keywords, how might this affect the LDA topic modeling recommendations?",
        "options": [
            "Jose L. Martínez Lastra would remain the top recommendation due to his web services focus.",
            "Topic 19’s relevance would decrease, potentially lowering rankings for advisors tied to it.",
            "Topic 8 would have a lower probability, as it is unrelated to artificial intelligence.",
            "Minyi Guo would become the top recommendation due to his energy efficiency focus."
        ],
        "answer": "Topic 19’s relevance would decrease, potentially lowering rankings for advisors tied to it.",
        "question_number": 16,
        "explanation": "Counterfactual-Based: Replacing 'case studies' with 'artificial intelligence' shifts Emily’s topic distribution away from Topic 19 (software-focused) toward AI-related topics, potentially lowering rankings for advisors like Martínez Lastra."
    },
    {
        "question": "Why is Minyi Guo ranked high (0.9943) in LDA topic modeling but not in the top 3 for cosine similarity?",
        "options": [
            "Minyi Guo’s keywords perfectly match Emily’s keywords.",
            "Minyi Guo’s topic distribution aligns with Emily’s, but his keywords differ significantly.",
            "Minyi Guo’s publications have low citation counts.",
            "Minyi Guo’s research focuses on a niche topic unrelated to Emily’s keywords."
        ],
        "answer": "Minyi Guo’s topic distribution aligns with Emily’s, but his keywords differ significantly.",
        "question_number": 17,
        "explanation": "Scenario-Specific: Minyi Guo’s high LDA score (0.9943) reflects alignment with Topic 19, but his keywords (e.g., energy consumption, transaction management) have low overlap with Emily’s, reducing his cosine similarity rank."
    },
    {
        "question": "How does the LDA model map Emily’s keywords to topics like Topic 19?",
        "options": [
            "By counting the frequency of her keywords in advisor publications.",
            "By converting her keywords into a numerical vector and calculating cosine similarity.",
            "By assigning her keywords to predefined topics based on co-occurrence in a trained model.",
            "By directly matching her keywords to advisor keywords."
        ],
        "answer": "By assigning her keywords to predefined topics based on co-occurrence in a trained model.",
        "question_number": 18,
        "explanation": "Model Inner Working: The LDA model maps Emily’s keywords (e.g., software engineering) to topics like Topic 19 by analyzing their co-occurrence in a trained model, creating a topic distribution for comparison with advisors’ profiles."
    },
    {
        "question": "Why was Nico Zazworka ranked first in the cosine similarity model for Emily’s research interests?",
        "options": [
            "His topic distribution aligns with Topic 8, which has the highest probability.",
            "His keywords, like 'software process,' 'software quality,' and 'design debt,' closely match Emily’s.",
            "He has the most publications in the database.",
            "His keywords focus on artificial intelligence, aligning with Emily’s interests."
        ],
        "answer": "His keywords, like 'software process,' 'software quality,' and 'design debt,' closely match Emily’s.",
        "question_number": 19,
        "explanation": "Scenario-Specific: Nico Zazworka’s keywords (e.g., software process, software quality, design debt) closely overlap with Emily’s (e.g., software engineering, software process, software quality), resulting in a high cosine similarity score of 0.9115."
    },
    {
        "question": "If Emily adds 'software evolution' to her keywords, which advisor’s cosine similarity score is likely to increase the most?",
        "options": [
            "Shari Lawrence Pfleeger, due to her focus on software reuse.",
            "Nico Zazworka, due to his focus on software evolution.",
            "Eleni Stroulia, due to her focus on software architecture.",
            "Steffen Oeltze, due to his focus on perfusion data."
        ],
        "answer": "Nico Zazworka, due to his focus on software evolution.",
        "question_number": 20,
        "explanation": "Counterfactual-Based: Adding 'software evolution' increases overlap with Nico Zazworka’s keywords (e.g., software evolution, software process), likely boosting his cosine similarity score the most."
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
        "question": "How does the cosine similarity model work in the advisor recommender system for Sara’s research interests?",
        "options": [
            "By grouping Sara’s keywords into topics and comparing distributions",
            "By measuring the angle between Sara’s keyword vector and advisors’ keyword vectors",
            "By counting exact keyword matches between Sara and advisors",
            "By analyzing the sentiment of Sara’s research interests"
        ],
        "answer": "By measuring the angle between Sara’s keyword vector and advisors’ keyword vectors",
        "question_number": 1,
        "explanation": "Feature-Based: Cosine similarity calculates the angle between vectors representing Sara’s keywords (e.g., web mining, web spam) and advisors’ keywords, with smaller angles indicating stronger alignment."
    },
    {
        "question": "What does a cosine similarity score of 0.828 for Masashi Toyoda indicate for Sara’s interests in web mining and web spam?",
        "options": [
            "No alignment with Sara’s research interests",
            "Strong alignment due to closely matching keywords",
            "Moderate alignment with unrelated topics",
            "Perfect match across all keywords"
        ],
        "answer": "Strong alignment due to closely matching keywords",
        "question_number": 2,
        "explanation": "Feature-Based: Toyoda’s keywords (e.g., web community, web spam) closely match Sara’s (web mining, web spam), resulting in a high score of 0.828."
    },
    {
        "question": "What is the role of LDA topic modeling in recommending advisors for Sara?",
        "options": [
            "To count keyword frequencies in advisor profiles",
            "To group keywords into research themes and compare topic distributions",
            "To rank advisors by publication volume",
            "To match exact keywords between Sara and advisors"
        ],
        "answer": "To group keywords into research themes and compare topic distributions",
        "question_number": 3,
        "explanation": "Model Inner Working: LDA groups keywords into topics (e.g., Topic 21: servic, web, secur) and compares Sara’s topic distribution to advisors’ profiles."
    },
    {
        "question": "Why does the system combine cosine similarity and LDA topic modeling for Sara’s recommendations?",
        "options": [
            "To simplify the recommendation process",
            "To capture both keyword overlap and thematic alignment for robust matches",
            "To prioritize advisors with more publications",
            "To reduce the number of advisors considered"
        ],
        "answer": "To capture both keyword overlap and thematic alignment for robust matches",
        "question_number": 4,
        "explanation": "General: Using both models ensures recommendations reflect direct keyword matches (cosine) and broader research themes (LDA), improving accuracy."
    },
    {
        "question": "What does Aaron L. Fogelson’s LDA similarity score of 0.9328 suggest for Sara’s interests?",
        "options": [
            "His research is unrelated to Sara’s interests",
            "His topic distribution aligns closely with Sara’s",
            "He has the most publications in the system",
            "His keywords are identical to Sara’s"
        ],
        "answer": "His topic distribution aligns closely with Sara’s",
        "question_number": 5,
        "explanation": "Feature-Based: The high LDA score indicates Fogelson’s research aligns with Sara’s topic distribution, particularly Topic 21 (web, servic, secur)."
    },
    {
        "question": "Which of Sara’s keywords likely contributed most to Masashi Toyoda’s cosine similarity score of 0.828?",
        "options": [
            "Websites, web pages",
            "Online communities, web mining, web spam",
            "Search engines, tools",
            "Community detection, algorithms"
        ],
        "answer": "Online communities, web mining, web spam",
        "question_number": 6,
        "explanation": "Feature-Based: Toyoda’s keywords (e.g., web community, web spam, mining) directly overlap with Sara’s online communities, web mining, and web spam."
    },
    {
        "question": "Why is Sang Ho Lee’s cosine similarity score (0.759) lower than Masashi Toyoda’s (0.828)?",
        "options": [
            "Lee’s keywords are less specific, like ‘web page’ and ‘web robot’",
            "Lee’s research focuses on platelet aggregation",
            "Lee has fewer publications",
            "Lee’s research is in a different language"
        ],
        "answer": "Lee’s keywords are less specific, like ‘web page’ and ‘web robot’",
        "question_number": 7,
        "explanation": "Feature-Based: Lee’s keywords (e.g., web page, web robot) are less aligned with Sara’s specific interests (web mining, web spam) than Toyoda’s."
    },
    {
        "question": "Which topic most influences Aaron L. Fogelson’s LDA similarity score of 0.9328 for Sara?",
        "options": [
            "Topic 6: design, speech, process",
            "Topic 8: control, algorithm, optim",
            "Topic 21: servic, web, secur",
            "Topic 12: unrelated terms"
        ],
        "answer": "Topic 21: servic, web, secur",
        "question_number": 8,
        "explanation": "Feature-Based: Topic 21, with high probability (0.5446) in Sara’s profile, aligns with Fogelson’s research themes, boosting his LDA score."
    },
    {
        "question": "How did Sara’s keyword ‘web spam’ contribute to J. A. Levin’s cosine similarity score of 0.717?",
        "options": [
            "It had no impact, as Levin’s keywords are unrelated",
            "It aligned with Levin’s keywords like ‘data mining’ and ‘web association rule’",
            "It reduced Levin’s score due to mismatch",
            "It matched all of Levin’s keywords"
        ],
        "answer": "It aligned with Levin’s keywords like ‘data mining’ and ‘web association rule’",
        "question_number": 9,
        "explanation": "Feature-Based: Levin’s keywords (data mining, web association rule) partially align with ‘web spam,’ contributing to his score."
    },
    {
        "question": "Which advisor’s keywords least align with Sara’s interest in ‘online communities’?",
        "options": [
            "Masashi Toyoda",
            "Sang Ho Lee",
            "J. A. Levin",
            "Aaron L. Fogelson"
        ],
        "answer": "Aaron L. Fogelson",
        "question_number": 10,
        "explanation": "Feature-Based: Fogelson’s keywords (e.g., platelet aggregation) are unrelated to online communities, unlike the others."
    },
    {
        "question": "If Sara adds ‘machine learning’ to her keywords, which advisor might become rank 1 in cosine similarity?",
        "options": [
            "Masashi Toyoda",
            "Sang Ho Lee",
            "J. A. Levin",
            "Aaron L. Fogelson"
        ],
        "answer": "J. A. Levin",
        "question_number": 11,
        "explanation": "Counterfactual-Based: Levin’s keywords (e.g., data mining, web association rule) are closer to machine learning, potentially boosting his score."
    },
    {
        "question": "If Sara removes ‘web spam’ from her keywords, what might happen to Masashi Toyoda’s cosine similarity ranking?",
        "options": [
            "It would increase due to broader focus",
            "It would decrease due to loss of key overlap",
            "It would remain unchanged",
            "It would drop to last rank"
        ],
        "answer": "It would decrease due to loss of key overlap",
        "question_number": 12,
        "explanation": "Counterfactual-Based: ‘Web spam’ is a key overlap with Toyoda’s keywords, so removing it would lower his score."
    },
    {
        "question": "How would adding ‘security’ to Sara’s keywords affect Reza Shokri’s LDA-based recommendation?",
        "options": [
            "Decrease his score due to topic mismatch",
            "Increase his score due to alignment with Topic 21",
            "Have no effect",
            "Move him to the lowest rank"
        ],
        "answer": "Increase his score due to alignment with Topic 21",
        "question_number": 13,
        "explanation": "Counterfactual-Based: ‘Security’ aligns with Topic 21 (servic, web, secur), likely boosting Shokri’s LDA score."
    },
    {
        "question": "If Sara emphasizes ‘web mining’ more, which advisor might drop in cosine similarity ranking?",
        "options": [
            "Masashi Toyoda",
            "Sang Ho Lee",
            "J. A. Levin",
            "Reza Shokri"
        ],
        "answer": "Sang Ho Lee",
        "question_number": 14,
        "explanation": "Counterfactual-Based: Lee’s keywords (e.g., web robot) are less aligned with ‘web mining’ than Toyoda’s or Levin’s, potentially lowering his score."
    },
    {
        "question": "How is Sara’s keyword list [online communities, web mining, web spam] converted to a vector for cosine similarity?",
        "options": [
            "By assigning random numbers to each keyword",
            "By counting the frequency of each keyword in a fixed vocabulary",
            "By grouping keywords into topics",
            "By analyzing keyword sentiment"
        ],
        "answer": "By counting the frequency of each keyword in a fixed vocabulary",
        "question_number": 15,
        "explanation": "Model Inner Working: Keywords are represented as a count vector based on their frequency in a predefined vocabulary."
    },
    {
        "question": "What does the dot product measure in cosine similarity for Sara’s keywords?",
        "options": [
            "The exact number of matching keywords",
            "The sum of products of corresponding vector components",
            "The difference between keyword frequencies",
            "The total number of keywords"
        ],
        "answer": "The sum of products of corresponding vector components",
        "question_number": 16,
        "explanation": "Model Inner Working: The dot product computes the sum of products of corresponding elements in Sara’s and advisors’ vectors."
    },
    {
        "question": "If Sara’s vector is [1, 1, 1] for [web mining, web spam, online communities] and Toyoda’s is [2, 1, 1], what is the dot product?",
        "options": [
            "3",
            "4",
            "5",
            "6"
        ],
        "answer": "4",
        "question_number": 17,
        "explanation": "Model Inner Working: Dot product = (1×2) + (1×1) + (1×1) = 2 + 1 + 1 = 4."
    },
    {
        "question": "What does Topic 21 (servic, web, secur) represent in the LDA model for Sara’s interests?",
        "options": [
            "A collection of unrelated keywords",
            "A group of keywords related to web services and security",
            "A list of advisor names",
            "A count of publication frequencies"
        ],
        "answer": "A group of keywords related to web services and security",
        "question_number": 18,
        "explanation": "Model Inner Working: LDA groups related keywords into topics, and Topic 21 includes terms like ‘web’ and ‘secur,’ relevant to Sara’s interests."
    },
    {
        "question": "Why was Masashi Toyoda ranked first in cosine similarity for Sara’s interests?",
        "options": [
            "His publications have the most citations",
            "His keywords like ‘web community’ and ‘web spam’ closely match Sara’s",
            "His research is in a different field",
            "His similarity score is the lowest"
        ],
        "answer": "His keywords like ‘web community’ and ‘web spam’ closely match Sara’s",
        "question_number": 19,
        "explanation": "Scenario-Specific: Toyoda’s keywords (web community, web spam) align closely with Sara’s interests, leading to a high score of 0.828."
    },
    {
        "question": "Why does Aaron L. Fogelson rank first in LDA but not in cosine similarity for Sara?",
        "options": [
            "His keywords exactly match Sara’s",
            "His topic distribution aligns with Topic 21, but his keywords are unrelated",
            "He has fewer publications",
            "His research is unrelated to Topic 21"
        ],
        "answer": "His topic distribution aligns with Topic 21, but his keywords are unrelated",
        "question_number": 20,
        "explanation": "Scenario-Specific: Fogelson’s LDA score (0.9328) reflects alignment with Topic 21, but his keywords (e.g., platelet aggregation) don’t match Sara’s."
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
    st.write("----------------------------------------------------")
    


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
    










