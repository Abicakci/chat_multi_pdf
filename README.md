# chat_multi_pdf

Langchain Chatbot pour plusieurs PDF
Langchain Chatbot est un chatbot conversationnel alimenté par des modèles OpenAI et Hugging Face. Il est conçu pour fournir une interface de chat fluide permettant de rechercher des informations dans plusieurs documents PDF. 
Le chatbot utilise les capacités des modèles linguistiques et des embeddings pour effectuer une recherche conversationnelle, permettant aux utilisateurs de poser des questions et de recevoir des réponses pertinentes à partir du contenu des PDF.

Objectif
L'objectif de ce projet est de créer un chatbot capable d'interagir avec les utilisateurs et de fournir des réponses à partir d'une collection de documents PDF. 
Le chatbot utilise des techniques de traitement du langage naturel et d'apprentissage automatique pour comprendre les requêtes des utilisateurs et extraire des informations pertinentes des PDF. 
En incorporant des modèles OpenAI et Hugging Face, le chatbot exploite des modèles linguistiques et des embeddings puissants pour améliorer ses capacités conversationnelles et la précision des réponses.

Fonctionnalités
Prise en charge de plusieurs PDF : Le chatbot prend en charge le téléchargement de plusieurs documents PDF, permettant aux utilisateurs de rechercher des informations à partir d'une gamme diversifiée de sources.
Recherche conversationnelle : Le chatbot utilise des techniques de recherche conversationnelle pour fournir des réponses pertinentes et contextuelles aux requêtes des utilisateurs.
Modèles linguistiques : Le projet intègre des modèles OpenAI et Hugging Face pour la compréhension et la génération de langage naturel, permettant au chatbot d'engager des conversations significatives.
Extraction de texte PDF : Les documents PDF sont traités pour extraire le contenu textuel, qui est utilisé pour l'indexation et la recherche.
Découpage de texte : Le texte extrait est divisé en de plus petits morceaux pour améliorer l'efficacité de la recherche et fournir des réponses plus précises.

Installation
Pour installer et exécuter le Chatbot Langchain, suivez ces étapes :

Clonez le dépôt
git clone https://github.com/Abdullahw72/langchain-chatbot-multiple-PDF

Créez un environnement virtuel
pip install virtualenv
python<version> -m venv <nom-environnement-virtuel>
<nom-environnement-virtuel>\Scripts\activate

Installez les dépendances à l'aide de requirements.txt
pip install -r requirements.txt

Ajoutez votre clé OpenAI en créant un fichier .env dans le dossier et ajoutez ce qui suit :
OPENAI_API_KEY="<votre clé>"

Pour ceux d'entre vous qui souhaitent utiliser l'approche HuggingFace, assurez-vous d'ajouter la clé d'API HuggingFace dans votre fichier .env :
HUGGINGFACEHUB_API_TOKEN="<votre clé>"

Exécutez l'application

streamlit run app.py
Consultez les meilleurs modèles d'embedding : https://huggingface.co/blog/mteb

Consultez les meilleurs LLMs : https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

REMARQUE : Veuillez garder à l'esprit que vous devez vérifier les exigences matérielles pour le modèle que vous choisissez en fonction de votre machine, 
car les embeddings et le modèle s'exécuteront localement sur votre système et seront chargés dans votre RAM. Assurez-vous de faire des recherches avant d'exécuter le code avec n'importe quel modèle choisi.

Utilisation
Téléchargez des documents PDF : Utilisez la barre latérale de l'application pour télécharger un ou plusieurs fichiers PDF.
Posez des questions : Dans l'interface principale du chat, saisissez vos questions relatives au contenu des PDF téléchargés.
Recevez des réponses : Le chatbot générera des réponses en fonction des informations extraites des PDF.


# Architecture

![image](https://github.com/Abicakci/chat_multi_pdf/assets/121668685/3118c73d-e437-4037-8312-5ae7a2f9c592)

