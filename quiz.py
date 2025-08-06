import streamlit as st
import random
import matplotlib.pyplot as plt
#import mysql.connector
#from mysql.connector import Error

def load_survey():
    return [
    "I can identify appropriate advisors for my research interests based on the system’s explanations.",
    "The system’s explanations help me judge how trustworthy the advisor recommendations are.",
    "The system’s explanations help me understand how my research interests influence the advisor recommendations.",
    "I can identify cases where the system’s advisor recommendations might be less relevant or incorrect.",
    "The system’s explanations of how recommendations are generated (e.g., keyword matching and topic modeling) are clear and easy to understand.",
    "The system’s explanations help me understand why specific advisors were recommended for my research interests.",
    "I feel confident in using the system’s recommendations to make decisions about selecting an advisor."
]

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
        "question_number": 1,
        "explanation": "Feature-Based: The text similarity model uses cosine similarity to compare Amina’s keywords, such as 'mobile devices' and 'mobile applications,' with advisors’ publication keywords to identify alignment."
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
        "question": "What role does LDA topic modeling play in recommending advisors for Amina’s research interests in mobile devices and adaptive systems?",
        "options": [
            "It calculates the Euclidean distance between keyword vectors",
            "It groups Amina’s keywords into research themes like mobile technologies and compares them to advisors’ topic profiles",
            "It ranks advisors based on their citation counts",
            "It directly matches individual keywords without considering themes"
        ],
        "answer": "It groups Amina’s keywords into research themes like mobile technologies and compares them to advisors’ topic profiles",
        "question_number": 3,
        "explanation": "Model Inner Working: LDA assigns keywords like 'mobile devices' to topics (e.g., Topic 22: mobil, devic, system) and compares Amina’s topic distribution to advisors’ profiles."
    },
    {
        "question": "Why does the advisor recommendation system for Amina use both cosine similarity and LDA topic modeling?",
        "options": [
            "To reduce the computational complexity of keyword matching",
            "To combine specific keyword matches with broader research theme alignment for robust recommendations",
            "To ensure all advisors have the same ranking in both models",
            "To eliminate the need for user-provided keywords"
        ],
        "answer": "To combine specific keyword matches with broader research theme alignment for robust recommendations",
        "question_number": 4,
        "explanation": "General: Using both models ensures precise keyword matches (cosine) and thematic alignment (LDA), improving recommendation accuracy for Amina’s interests."
    },
    {
        "question": "What does Oriana Riva’s cosine similarity score of 0.9104 indicate for Amina’s research interests in mobile applications?",
        "options": [
            "A weak alignment with Amina’s research interests",
            "A strong alignment with Amina’s research interests",
            "No alignment with Amina’s research interests",
            "A random match unrelated to mobile technologies"
        ],
        "answer": "A strong alignment with Amina’s research interests",
        "question_number": 5,
        "explanation": "Scenario-Specific: A score of 0.9104, close to 1, indicates a strong match between Amina’s keywords (e.g., 'mobile devices,' 'context information') and Oriana’s profile."
    },
    {
        "question": "Which of Amina’s keywords likely contributed most to Oriana Riva’s top ranking in the cosine similarity model?",
        "options": [
            "Resource-constrained mobile devices",
            "Parallel processing",
            "Software evolution",
            "Static program analysis"
        ],
        "answer": "Resource-constrained mobile devices",
        "question_number": 6,
        "explanation": "Feature-Based: Oriana’s keywords include 'resource-constrained mobile device,' directly matching Amina’s interest, contributing to her high score of 0.9104."
    },
    {
        "question": "Why was Sotirios I. Maniatis ranked first in the LDA topic modeling results for Amina?",
        "options": [
            "His keywords focus on static program analysis",
            "His topic distribution aligns strongly with Topic 22 (mobil, devic, system)",
            "He has the highest cosine similarity score",
            "His research is unrelated to mobile technologies"
        ],
        "answer": "His topic distribution aligns strongly with Topic 22 (mobil, devic, system)",
        "question_number": 7,
        "explanation": "Scenario-Specific: Maniatis’ topic profile aligns with Topic 22, which includes Amina’s keywords like 'mobile devices,' leading to a high similarity score of 0.9899."
    },
    {
        "question": "What does the LDA topic probability of 0.7456 for Topic 22 mean for Amina’s research interests?",
        "options": [
            "Her interests are weakly aligned with mobile technologies",
            "Her interests are strongly aligned with mobile-related research themes",
            "Her interests are unrelated to Topic 22",
            "Her interests are evenly distributed across all topics"
        ],
        "answer": "Her interests are strongly aligned with mobile-related research themes",
        "question_number": 8,
        "explanation": "Scenario-Specific: A high probability for Topic 22 (mobil, devic, system) indicates strong alignment with Amina’s mobile-focused research."
    },
    {
        "question": "Which of Amina’s keywords likely influenced Enrico Rukzio’s second-place ranking in the cosine similarity model?",
        "options": [
            "Mobile interaction technique",
            "Worst-case execution time",
            "Software quality",
            "Topological space"
        ],
        "answer": "Mobile interaction technique",
        "question_number": 9,
        "explanation": "Feature-Based: Enrico’s keywords like 'mobile interaction technique' align with Amina’s focus on mobile applications, contributing to his score of 0.8383."
    },
    {
        "question": "How did Amina’s keyword 'mobile users' contribute to Cory Cornelius’ ranking in the cosine similarity model?",
        "options": [
            "It had no impact due to lack of overlap",
            "It matched Cory’s focus on 'personal mobile device' and 'mobile application'",
            "It reduced Cory’s ranking due to mismatch",
            "It aligned with Cory’s focus on static analysis"
        ],
        "answer": "It matched Cory’s focus on 'personal mobile device' and 'mobile application'",
        "question_number": 10,
        "explanation": "Feature-Based: Cory’s keywords overlap with Amina’s 'mobile users' and 'mobile applications,' leading to his score of 0.8224."
    },
    {
        "question": "Which advisor’s keywords least align with Amina’s in the cosine similarity model?",
        "options": [
            "Oriana Riva",
            "Enrico Rukzio",
            "Cory Cornelius",
            "All align equally"
        ],
        "answer": "Cory Cornelius",
        "question_number": 11,
        "explanation": "Scenario-Specific: Cory has the lowest cosine similarity score (0.8224) among the top three, indicating the least keyword alignment."
    },
    {
        "question": "Why does Nico Zazworka rank second in LDA but not in the top three for cosine similarity?",
        "options": [
            "His keywords focus on mobile devices",
            "His topic distribution aligns with Topic 22, but his keywords focus on software engineering",
            "His cosine similarity score is higher than Oriana’s",
            "His research has no overlap with Amina’s"
        ],
        "answer": "His topic distribution aligns with Topic 22, but his keywords focus on software engineering",
        "question_number": 12,
        "explanation": "Scenario-Specific: Nico’s topic alignment with Topic 22 is strong, but his keywords (e.g., 'software evolution') differ from Amina’s mobile focus."
    },
    {
        "question": "If Amina removes 'resource-constrained mobile devices' from her keywords, what might happen to Oriana Riva’s cosine similarity ranking?",
        "options": [
            "It would likely increase her score",
            "It would likely decrease her score",
            "It would have no effect",
            "It would make her rank third"
        ],
        "answer": "It would likely decrease her score",
        "question_number": 13,
        "explanation": "Counterfactual-Based: Removing 'resource-constrained mobile devices' reduces the overlap with Oriana’s keywords, lowering her cosine similarity score."
    },
    {
        "question": "If Amina adds 'wearable sensor' to her keywords, which advisor might rise to the top in cosine similarity?",
        "options": [
            "Oriana Riva",
            "Enrico Rukzio",
            "Cory Cornelius",
            "Sotirios I. Maniatis"
        ],
        "answer": "Cory Cornelius",
        "question_number": 14,
        "explanation": "Counterfactual-Based: Cory’s keywords include 'wearable sensor,' increasing alignment with Amina’s updated interests, potentially boosting his score."
    },
    {
        "question": "How would adding 'wireless network' to Amina’s keywords affect the LDA topic modeling rankings?",
        "options": [
            "It would likely boost Sotirios I. Maniatis’ ranking",
            "It would lower Nico Zazworka’s ranking",
            "It would have no effect on rankings",
            "It would make Reinhold Heckmann rank first"
        ],
        "answer": "It would likely boost Sotirios I. Maniatis’ ranking",
        "question_number": 15,
        "explanation": "Counterfactual-Based: Maniatis’ keywords include 'wireless network,' aligning with Topic 22, likely increasing his LDA similarity score."
    },
    {
        "question": "How is Amina’s keyword 'mobile devices' represented in the cosine similarity model?",
        "options": [
            "As a topic probability",
            "As a numerical count in a keyword vector",
            "As a static analysis metric",
            "As a software evolution score"
        ],
        "answer": "As a numerical count in a keyword vector",
        "question_number": 16,
        "explanation": "Model Inner Working: Keywords like 'mobile devices' are converted into a count vector (e.g., [2, 1, 0, 1]) for cosine similarity calculations."
    },
    {
        "question": "What does the dot product in cosine similarity represent for Amina’s keywords?",
        "options": [
            "The sum of matching keyword frequencies",
            "The total number of publications",
            "The Euclidean distance between vectors",
            "The probability of topic alignment"
        ],
        "answer": "The sum of matching keyword frequencies",
        "question_number": 17,
        "explanation": "Model Inner Working: The dot product sums the product of matching keyword counts, e.g., for [2, 1] and [2, 2], it’s (2*2) + (1*2) = 6."
    },
    {
        "question": "If Amina’s keyword vector is [2, 1, 0, 1] for [mobile devices, mobile applications, sensor data, resource-constrained] and Oriana’s is [2, 2, 0, 1], what is the dot product?",
        "options": [
            "4",
            "5",
            "6",
            "7"
        ],
        "answer": "6",
        "question_number": 18,
        "explanation": "Model Inner Working: Dot product = (2*2) + (1*2) + (0*0) + (1*1) = 4 + 2 + 0 + 1 = 6."
    },
    {
        "question": "In LDA topic modeling, how are Amina’s keywords grouped into Topic 22?",
        "options": [
            "Based on their frequency in her input",
            "Based on their co-occurrence in mobile-related research themes",
            "Based on their cosine similarity scores",
            "Based on their static analysis relevance"
        ],
        "answer": "Based on their co-occurrence in mobile-related research themes",
        "question_number": 19,
        "explanation": "Model Inner Working: LDA groups keywords like 'mobile devices' into Topic 22 (mobil, devic, system) based on co-occurrence patterns."
    },
    {
        "question": "What does a cosine similarity score of 0.8224 for Cory Cornelius imply for Amina’s research interests?",
        "options": [
            "No alignment with Amina’s interests",
            "A moderate alignment, still meaningful for niche areas",
            "A perfect match with Amina’s interests",
            "An error in the recommendation system"
        ],
        "answer": "A moderate alignment, still meaningful for niche areas",
        "question_number": 20,
        "explanation": "Scenario-Specific: A score of 0.8224 indicates a good but not perfect match, relevant for niche areas like mobile sensors in Amina’s interests."
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
        "question": "What is the primary purpose of the cosine similarity model in the advisor recommendation system for David Chen’s research interests?",
        "options": [
            "To group keywords into topics for matching advisors",
            "To compare the direction of David’s and advisors’ keyword vectors",
            "To predict advisors’ research output based on David’s keywords",
            "To calculate the probability of topics in David’s inputs"
        ],
        "answer": "To compare the direction of David’s and advisors’ keyword vectors",
        "question_number": 1,
        "explanation": "Feature-Based: Cosine similarity measures the angle between David’s keyword vector (e.g., rescue robot, autonomous mobile robot) and advisors’ vectors to find alignment."
    },
    {
        "question": "How does the LDA topic modeling approach contribute to the advisor recommendation system for David Chen?",
        "options": [
            "It calculates exact keyword matches between David and advisors",
            "It groups keywords into research themes and compares topic distributions",
            "It ranks advisors based on their publication count",
            "It converts David’s keywords into numerical vectors for cosine similarity"
        ],
        "answer": "It groups keywords into research themes and compares topic distributions",
        "question_number": 2,
        "explanation": "Model Inner Working: LDA identifies topics like Topic 22 (mobil, robot, autonom) and matches David’s topic distribution to advisors’ profiles."
    },
    {
        "question": "Why does the system use both cosine similarity and LDA topic modeling for David Chen’s advisor recommendations?",
        "options": [
            "To increase computational complexity",
            "To provide a robust match by combining keyword and thematic alignment",
            "To reduce the number of recommended advisors",
            "To prioritize advisors with the most publications"
        ],
        "answer": "To provide a robust match by combining keyword and thematic alignment",
        "question_number": 3,
        "explanation": "General: Combining cosine similarity (exact keyword matches) and LDA (thematic alignment) ensures a comprehensive recommendation for David’s interests."
    },
    {
        "question": "What does a cosine similarity score of 0.9011 for Fumitoshi Matsuno indicate for David Chen?",
        "options": [
            "No alignment with David’s research interests",
            "A moderate level of keyword overlap",
            "A strong alignment with David’s keyword vector",
            "Exactly 90.11% of David’s keywords match"
        ],
        "answer": "A strong alignment with David’s keyword vector",
        "question_number": 4,
        "explanation": "Scenario-Specific: A score of 0.9011 shows strong alignment between David’s keywords (e.g., rescue robot) and Matsuno’s profile."
    },
    {
        "question": "How is David Chen’s research interest represented in the cosine similarity model?",
        "options": [
            "As a probability distribution over 30 topics",
            "As a numerical count vector of keywords",
            "As a list of advisor publication titles",
            "As a weighted sum of advisor profiles"
        ],
        "answer": "As a numerical count vector of keywords",
        "question_number": 5,
        "explanation": "Model Inner Working: David’s keywords (e.g., [rescue robot, autonomous mobile robot]) are converted to a vector like [1, 1, 0, …]."
    },
    {
        "question": "What is a key difference between cosine similarity and LDA topic modeling in David Chen’s recommendation system?",
        "options": [
            "Cosine similarity uses topics, while LDA uses exact keywords",
            "Cosine similarity compares keyword vectors, while LDA compares topic distributions",
            "Cosine similarity is probabilistic, while LDA is deterministic",
            "Cosine similarity ranks advisors, while LDA does not"
        ],
        "answer": "Cosine similarity compares keyword vectors, while LDA compares topic distributions",
        "question_number": 6,
        "explanation": "General: Cosine similarity focuses on exact keyword matches, while LDA groups keywords into themes like Topic 22 for matching."
    },
    {
        "question": "Which of David Chen’s keywords likely contributed most to Fumitoshi Matsuno’s top cosine similarity ranking?",
        "options": [
            "Software engineering",
            "Neural network",
            "Rescue robot",
            "Topological space"
        ],
        "answer": "Rescue robot",
        "question_number": 7,
        "explanation": "Feature-Based: Matsuno’s keywords (e.g., rescue robot, tele-operation mode) directly match David’s, driving his high score of 0.9011."
    },
    {
        "question": "Why does Tamio Arai rank second in the cosine similarity model for David Chen?",
        "options": [
            "His keywords include unrelated terms like software process",
            "His keywords have less overlap with David’s than Matsuno’s",
            "His topic distribution is less aligned with Topic 22",
            "His similarity score is higher than Matsuno’s"
        ],
        "answer": "His keywords have less overlap with David’s than Matsuno’s",
        "question_number": 8,
        "explanation": "Feature-Based: Arai’s keywords (e.g., mobile robot) overlap but lack specific terms like rescue robot, leading to a lower score (0.7654)."
    },
    {
        "question": "Which keyword likely contributed to Michita Imai’s third rank in the cosine similarity model?",
        "options": [
            "Rescue robot",
            "Robot system",
            "Neural network",
            "Software quality"
        ],
        "answer": "Robot system",
        "question_number": 9,
        "explanation": "Feature-Based: Imai’s keywords like robot system align with David’s, but terms like humanoid robot reduce relevance, yielding a score of 0.75."
    },
    {
        "question": "Why is Reinhold Heckmann recommended by the LDA model despite no direct keyword overlap with David Chen’s interests?",
        "options": [
            "His publications have the highest word count",
            "His topic distribution aligns with Topic 22 (mobil, robot, autonom)",
            "His cosine similarity score is higher than Matsuno’s",
            "He has more publications than other advisors"
        ],
        "answer": "His topic distribution aligns with Topic 22 (mobil, robot, autonom)",
        "question_number": 10,
        "explanation": "Scenario-Specific: Heckmann’s high LDA score (0.9888) reflects thematic alignment with Topic 22, relevant to David’s interests."
    },
    {
        "question": "If David Chen adds ‘humanoid robot’ to his keywords, who is likely to rank highest in the cosine similarity model?",
        "options": [
            "Fumitoshi Matsuno",
            "Tamio Arai",
            "Michita Imai",
            "Reinhold Heckmann"
        ],
        "answer": "Michita Imai",
        "question_number": 11,
        "explanation": "Counterfactual-Based: Adding ‘humanoid robot’ aligns with Imai’s keywords, likely increasing his score above Matsuno’s."
    },
    {
        "question": "If David Chen removes ‘rescue robot’ from his keywords, what is the likely impact on the cosine similarity rankings?",
        "options": [
            "Matsuno’s score will remain unchanged",
            "Matsuno’s score will decrease, possibly dropping his rank",
            "Imai’s score will increase significantly",
            "Arai’s score will become the highest"
        ],
        "answer": "Matsuno’s score will decrease, possibly dropping his rank",
        "question_number": 12,
        "explanation": "Counterfactual-Based: Removing ‘rescue robot’ reduces overlap with Matsuno’s profile, lowering his score."
    },
    {
        "question": "If David Chen emphasizes ‘neural network’ in his keywords, who might rank higher in the LDA model?",
        "options": [
            "Fumitoshi Matsuno",
            "Tamio Arai",
            "Kil To Chong",
            "Michita Imai"
        ],
        "answer": " Kil To Chong",
        "question_number": 13,
        "explanation": "Counterfactual-Based: Chong’s keywords (e.g., neural network) align with a topic distribution that would increase his LDA score."
    },
    {
        "question": "If David Chen shifts his keywords to ‘software engineering,’ who might rank higher in the LDA model?",
        "options": [
            "Heckmann’s ranking would decrease",
            "Zazworka’s ranking would increase",
            "Chong’s ranking would become the highest",
            "Matsuno would be recommended by LDA"
        ],
        "answer": "Zazworka’s ranking would increase",
        "question_number": 14,
        "explanation": "Counterfactual-Based: Zazworka’s keywords (e.g., software engineering) align with a topic distribution matching the new emphasis."
    },
    {
        "question": "How is David Chen’s keyword list [rescue robot, autonomous mobile robot, tele-operation mode] represented in the cosine similarity model?",
        "options": [
            "As a probability distribution over 30 topics",
            "As a vector like [1, 1, 1, 0, …] based on keyword presence",
            "As a list of topic probabilities",
            "As a weighted sum of advisor keywords"
        ],
        "answer": "As a vector like [1, 1, 1, 0, …] based on keyword presence",
        "question_number": 15,
        "explanation": "Model Inner Working: Keywords are converted to a vector where 1 indicates presence (e.g., rescue robot) and 0 indicates absence."
    },
    {
        "question": "What does the dot product in cosine similarity calculate for David Chen’s keywords and Matsuno’s profile?",
        "options": [
            "The sum of matching keyword counts",
            "The total number of keywords in both profiles",
            "The product of topic probabilities",
            "The Euclidean distance between vectors"
        ],
        "answer": "The sum of matching keyword counts",
        "question_number": 16,
        "explanation": "Model Inner Working: The dot product sums the product of corresponding vector elements, reflecting shared keywords."
    },
    {
        "question": "For a simplified example with David’s keywords [rescue robot, mobile robot] and Matsuno’s vector [1, 1], what is the cosine similarity if vectors are identical?",
        "options": [
            "0",
            "0.5",
            "1",
            "2"
        ],
        "answer": "1",
        "question_number": 17,
        "explanation": "Model Inner Working: Identical vectors (e.g., [1, 1] and [1, 1]) yield a cosine similarity of 1, indicating perfect alignment."
    },
    {
        "question": "How is Topic 22 (mobil, robot, autonom, system) used in the LDA model for David Chen’s recommendations?",
        "options": [
            "By counting exact matches of ‘mobil’ and ‘robot’",
            "By comparing David’s topic probability (0.7871) to advisor profiles",
            "By calculating cosine similarity of topic keywords",
            "By ranking advisors based on publication counts in Topic 22"
        ],
        "answer": "By comparing David’s topic probability (0.7871) to advisor profiles",
        "question_number": 18,
        "explanation": "Model Inner Working: LDA compares David’s high probability for Topic 22 with advisors’ topic distributions."
    },
    {
        "question": "Why is Fumitoshi Matsuno the top recommended advisor in the cosine similarity model for David Chen?",
        "options": [
            "His keywords include software engineering and neural network",
            "His keywords like rescue robot and tele-operation mode match David’s",
            "His topic distribution has the highest probability for Topic 8",
            "His similarity score is lower than Arai’s but more relevant"
        ],
        "answer": "His keywords like rescue robot and tele-operation mode match David’s",
        "question_number": 19,
        "explanation": "Scenario-Specific: Matsuno’s keywords directly match David’s, resulting in a high score of 0.9011."
    },
    {
        "question": "What does Reinhold Heckmann’s high LDA score (0.9888) indicate for David Chen’s recommendation?",
        "options": [
            "His keywords exactly match David’s",
            "His research themes align with Topic 22 (mobil, robot, autonom)",
            "His cosine similarity score is higher than Matsuno’s",
            "He has more publications than other advisors"
        ],
        "answer": "His research themes align with Topic 22 (mobil, robot, autonom)",
        "question_number": 20,
        "explanation": "Scenario-Specific: Heckmann’s high LDA score reflects thematic alignment with Topic 22, relevant to David’s interests."
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
    pass

def run_post_quiz():
   pass

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

if st.session_state.page == "post_quiz":
    username = st.session_state.get("username", "anonymous")
    st.markdown("### Post Quiz Survey")
    st.markdown("---")

    st.write(f"Hello, {username}")
    opts = list(range(1,8))
    likert_labels = {
        1: "Strongly Disagree",
        2: "Disagree",
        3: "Somewhat Disagree",
        4: "Neutral",
        5: "Somewhat Agree",
        6: "Agree",
        7: "Strongly Agree"
    }
    if opts[-1] == 5:
        likert_labels = {
            1: "Strongly Disagree",
            2: "Disagree",
            3: "Neutral",
            4: "Agree",
            5: "Strongly Agree"
        }

        
    st.write("#### 📝 Please complete the following survey")
    st.markdown(
        """This survey helps us understand how well the system’s explanations supported your understanding of the advisor recommendation process and your trust in its recommendations. Your feedback will help us improve the clarity and usefulness of the explanations for future users, whether delivered through static text or an interactive interface."""
    )
    
    st.write("---")

    if "post_quiz_questions" not in st.session_state:        
        post_quiz_questions = load_survey()

        random.shuffle(post_quiz_questions)

        st.session_state.post_quiz_questions = post_quiz_questions
        #st.session_state.post_quiz_answers = {q["id"]: None for q in post_quiz_questions}
    
    #def post_quiz_on_option_change(qid):
            #st.session_state["post_quiz_answers"][qid] = st.session_state.get(f"q_{qid}", None)
    
    for idx,q in enumerate (st.session_state.post_quiz_questions):

        question = q
        print(question)
        qid = idx
        
        st.markdown(f"**Q{idx+1}. {question}**")
        col1,col2,col3 = st.columns([2.5, 6, 2])
        with col1:
            st.markdown("""
            <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                Strongly Disagree
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.radio(
                label=f"Q{idx+1}. {question}",
                label_visibility = "collapsed",
                options=opts,
                index=None,
                key=f"q_{qid}",
                horizontal = True,
                on_change = lambda qid=qid:post_quiz_on_option_change(qid)
            )
        with col3:
            st.markdown("""
            <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                Strongly Agree
            </div>
            """, unsafe_allow_html=True)
        st.markdown("")
    if st.button("Done"):
        #unanswered = [qid for qid, ans in st.session_state.post_quiz_answers.items() if ans is None]

        #if unanswered:
         #   st.error("Please answer all questions before submitting.")
        #else:
            st.write("Thank you for Submitting the Survey")




if st.session_state.page == "quiz":
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
        if st.button("Go To Survey"):
            st.session_state.page  = "post_quiz"
            st.rerun()














