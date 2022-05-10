# Social Data Final Project

## Contributions
| Description | s202182  | s174182 | s220034 |
| ------------- | ------------- |-----------|-----------|
| Web-Design (CSS&HTML)  | 100%  | | |
| Section 1 (Electricity) Visualizations, Data Analysis  |  | | 100% |
| Section 2 (Geography) Visualizations, Data Analysis | | 100% | |
| Section 3 (PCA) Visualizations, Data Analysis | 100% | | | 
| Readme & Explanatory Notebooks | 40% | 40% | 20% | 


# Section 1: Motivation 
* What is your dataset(s)
    We have a couple of different datasets , each addressing different questions. 
    * National Travel Household Survey: [Link]("https://nhts.ornl.gov/")
    * Electoral Data: [Link](https://alarm-redist.github.io/posts/2021-08-10-census-2020/)
    * Income Data: [Link](https://data.census.gov/cedsci/)
    * Distribution of EVs: [Link](http://www.energy.ca.gov/zevstats) 
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
* Regarding the spatial data not all sources provided the data at ZCTA level, aggregation was therefore nessecary, for instance regarding the political orientation plot, was delivered nationally for USA at cencus block level, this can be seen in [gov_data.ipynb](https://github.com/klaramaria/social_data_final/blob/main/notebooks/gov_data.ipynb) Section Election. All other states therefore needed to be sorted out afterwards the cencus level was aggregated to ZCTA level. Finally the data which had no corresponding coordinates where filtered out as well. This in principle meant that some data was lost, but in the purpose of spatial illustrations it was necessary.
* Write a short section that discusses the dataset stats, containing key points/plots from your exploratory data  analysis.

As we have 5 datasets we won't describte the pre-processing of all of them in detail, as a lot of them are analogous. We will take the two datasets of the National Travel Household Survey and of the Electric Vehicles per Zipcode, as those represent the biggest sets and encompass all the methods that we used on the other sets. 
* The basic stats of the National Travel Household Survey can be found in the notebook [nths.ipynb](https://github.com/klaramaria/social_data_final/blob/main/nationalTravelSurvey/nths.ipynb).
* The basic stats of vehicle distribution can be found in the notebook [gov_data.ipynb](https://github.com/klaramaria/social_data_final/blob/main/notebooks/gov_data.ipynb)


# Section 3: Data Analysis 
* Insights into what we have learned about ... 
* Insight into how we used Machine Learning can be found in the notebook [nths.ipynb](https://github.com/klaramaria/social_data_final/blob/main/nationalTravelSurvey/nths.ipynb), Section 3.

# Section 4: Genre 
* Which genre of data story did you use?
   The genre we have chosen is a combination of interactive slideshow with a few annotated elements. The slideshow is chosen as it gives some chronological story, and the annotated part is chosen to highlight focus points of the data which contributes to the overall story.
   
* Which tools did you use from each of the 3 categories of Visual Narrative (Figure 7 in Segal and Heer). Why?
    All of our choropleth maps contains the ability to zoom, further we use motion in our gif describing the energy sources of california from the past 10 years. The zooming enables the reader to chose a zertain geographical area of interest and then see how many cars for instance are in his or her neighbourhood. The motion forces the reader how each category grows and declines over time. 
* Which tools did you use from each of the 3 categories of Narrative Structure (Figure 7 in Segal and Heer). Why?

For the narative structure we used the interactivity: hover tool in the spatial data, this was a natural choice as we wanted the reader to
have the freedom of browing around them self and check data for certain geographical areas. Also we used annotation to guide the reader in which areas the most EV where or the richest people live, as it otherwise would have been troublesome to find. To optimize this part we could have implemted a search function which would highlight the ZCTA that one searched for.

For the ordering we used linear ordering as the overall genre is slideshow, but we also implemented buttons at the top enabling the reader to drop to a certain sections which could be understood as minor implementation of "user-directed path"

# Section 5: Visualizations
We have chosen the following visualizations: 

* Jitter Plot: To visualize the classes of EV and Non-EV-Owners along one axis (this axis being a principal component). See notebook  [nths.ipynb](https://github.com/klaramaria/social_data_final/blob/main/nationalTravelSurvey/nths.ipynb), section 4. 
* Chlorophleth Map: 
* Histogram: 
* Bar Plot: [CA_ER.ipynb](https://github.com/klaramaria/social_data_final/blob/main/notebooks/California_electricity_resources.ipynb)


# Section 6: Discussion
* What went well?
The Discussion of the energy resources easily serves us in making an argument that we need to look at electric mobility in a more holistic way. As we can see the biggest part in energy consumption is still coming from fossile fuels. The time-trend also doesn't give off the impression that any goals close to the 1.5% goal could be met. 
You can definitely see a lot of the trends that we expected: There's the income split when it comes to EV Owners, there's the regional differences which correspond to the political differences (poorer, more republican and less EVs on the countryside = countrywards side of California).
PCA went decently well - of course there's the issue of categorical data, which can be mitigated by normalizing and one-hot-encoding. We can see some principal components which are able to provide some insight to EV Owners.

* What is still missing? What could be improved? Why?
In general the Machine Learning Part was more difficult than expected. Already the mix between categorical and ordinal data makes the choice in algorithms a lot smaller. We tried then doing a classification, both a normal Cassification Tree and a Random Forest. Those seemed promising at first, but in closer view they had a very low precision (around 25%), which means that it classified a gread number of non-electric vehicles as electric. 
The second method was a clustering, which accounts for the categorical natrue of the data. It is called k-modes clustering (as compared to k-means clustering). This proved to be too undynamic, and mostly data stayed in the classes it was initialized in. But this heavily depends on the number of initialized clusters and how we initialized, so there's room for improvement there. 
