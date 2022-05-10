# Social Data Final Project

# Section 1: Motivation 
* What is your dataset(s)
    We have a couple of different datasets , each addressing different questions. 
    * National Travel Household Survey: [Link]("https://nhts.ornl.gov/")
    * Electoral Data: [Link](https://alarm-redist.github.io/posts/2021-08-10-census-2020/)
    * Income Data: [Link](https://data.census.gov/cedsci/)
    * Distribution of EVs: [Link]("http://www.energy.ca.gov/zevstats") 
    * Energy Generation: [Link](https://www.energy.ca.gov/data-reports/energy-almanac/california-electricity-data/california-electrical-energy-generation)
    * California Power Plants: [Link](https://cecgis-caenergy.opendata.arcgis.com/datasets/CAEnergy::california-power-plants/about)
* Why did you choose those datasets:
    We wanted to examine the issue of the distribution and benefits of electric vehicles from a couple of different angles. One was the electricity, for which we need the datasets of electricity generation and of the power plants. Those give us insights into the different energy sources, and whether they change over time. 
    The next angle was comparing the placement of EVs with other metrics, such as electoral and income data. Our suspicion is that those are strongly correlated. This data is broken down into geographical areas. 
    Last, for the ML-task we wanted a dataset that helps us get a very wide overview over all kinds of different factors, in order to make prediction possible. As we'll see later, that was not quite the case, but some interesting insights could be extracted. 
* What was your goal for user experience:
    We try to foresee the questions that a critical reader would have, while reading about EVs, and answer them to a certain degree. Our goal is of course not to diminish the benefits of EVs, but to allow the reader to get a realistic, non glorifying image of them, all while allowing them to draw their own conclusions. 


# Section 2: Basic Stats 
* Write about your choices in data cleaning and preprocessing
* Write a short section that discusses the dataset stats, containing key points/plots from your exploratory data  analysis.

As we have 5 datasets we won't describte the pre-processing of all of them in detail, as a lot of them are analogous. We will take the two datasets of the National Travel Household Survey and of the Electric Vehicles per Zipcode, as those represent the biggest sets and encompass all the methods that we used on the other sets. 
* The basic stats of the National Travel Household Survey can be found in the notebook [nths.ipynb](https://github.com/klaramaria/social_data_final/blob/main/nationalTravelSurvey/nths.ipynb).
* The basic stats of 

# Section 3: Data Analysis 
* Insights into what we have learned about ... 
* Insight into how we used Machine Learning can be found in the notebook [nths.ipynb](https://github.com/klaramaria/social_data_final/blob/main/nationalTravelSurvey/nths.ipynb), Section 3.

# Section 4: Genre 
* Which genre of data story did you use?
* The genre we have chosen is a combination of slideshow and 
* Which tools did you use from each of the 3 categories of Visual Narrative (Figure 7 in Segal and Heer). Why?
* Which tools did you use from each of the 3 categories of Narrative Structure (Figure 7 in Segal and Heer). Why?

# Section 5: Visualizations
We have chosen the following visualizations: 

* Jitter Plot: To visualize the classes of EV and Non-EV-Owners along one axis (this axis being a principal component). See notebook  [nths.ipynb](https://github.com/klaramaria/social_data_final/blob/main/nationalTravelSurvey/nths.ipynb), section 4. 
* Chlorophleth Map: 
* Histogram: 
* Bar Plot: (James please fill in - link to your notebook)


# Section 6: Discussion
