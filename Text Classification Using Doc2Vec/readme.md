# Text Analysis using Twitter Data

## Data:
	

 - Sentiment140 dataset from Kaggle.
 - 2 columns -- Polarity with values 0- Negative and 4-Positive and Tweet column containing the tweets.
## Data Wrangling:
 - Removing special characters from tweet text by using python’s regex.
 - With demoji library all emoji that are present in the text were cleaned up.
## Model Building:
 - Genism’s Doc2Vec is used to build the model.
 - This involves 1st transforming the data into Tagged Documents format that is used in Doc2Vec.  We use an inbuilt method for this.
 - The entire corpus is split into train and test sets.
 - Doc2Vec is initialized and the training set is used, post that we use build_vocab to build a vocabulary from the training set.
 - We then convert the training and test data into vectors i.e texts to a matrix of numerical values. Using .infer_vector methodsover the model.
 - LogisticRegrssion model from sklearn learn is used to train a model and then using it to predict.
