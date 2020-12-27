# Social-media-community-detection

Throughout history, humans formed communities based on the common ground between each other. A group of people who share similar interests and beliefs almost always proved to be stronger and more invulnerable to disasters. While the shape of communities might have changed over the centuries to a more digitalized form, humans are attached more than ever to a diverse selection of communities online. 

In this project, I attempt to detect some online communities, more specifically, on Twitter. This project sets the pathway for further research on this topic.

### Data Preprocessing

The [original dataset](https://www.kaggle.com/kazanova/sentiment140) contained 1.6 million tweets. After running the model for hours, the dataset was trimmed to 50 thousand tweets. All tweets were cleaned from non-alphanumeric characters except '@'. TF-IDF was then applied to the dataset, discounting stop words in the process.

### Tests and Progression

Initially, the project started with [this dataset](https://archive.org/details/twitter_cikm_2010). The goal was to use geolocation as a parameter in the model. Sadly the dataset was too corrupted and would need days of cleaning and refining. After deciding to scrap that dataset, the current dataset was found on Kaggle. Since we could not use geolocation anymore, another methodology had to be implemented.

### Defintion of Community

The new methodology required a slight change to the definition of a community. A **"community"** is a group of people who talk or behave similarly.

### Final Model

Using the TF-IDF calculation, a K-means model was trained on the dataset producing the 50 clusters. Some of them are random, but others are really interesting! Have a look below.

### Future Improvements

Studying one tweet for each user is not enough to characterize a person in a community. Therefore the next most logical step is to use the usernames to get more posts made by each user and to use it to train the model. Another good idea is to remove common English words and see what happens. This would eliminate some of the categories below. Finally, further cleaning of the dataset would help refine the results.
