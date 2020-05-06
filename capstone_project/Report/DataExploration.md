## Data Exploration

This is a demographic data from Kalahari !Kung San people collected by Nancy Howell. The data has 544 entries that contains height, weight, age and gender information. Below is a snapshot of the data:

![](pics/DataSnapshot.png)

The next figure shows the summary statistics of the data. 

![](pics/SummaryStatistics.png)

The data contains 257 male and 287 females as shown below.

![](pics/male_vs_female.png)

## Exploratory visualization

In this section, we will do exploratory visualizations to better understand the underlying data. For this work, we are primarily interested in understanding the height vs age relationship in the data. So the focus of this section will be on those columns of the data.

First, we'll look at the distribution of the height data, as shown in the figure below. The height values range from 50 cms to 180 cms and majority of the data lies between 140 cms to 170 cms.

![](pics/height_dist.png)

If we split the distribution based on gender, as shown in figure below, we see that the males on average are taller than females.

![](pics/height_dist_gender.png)

Next, we'll look at the distribution of age in the figure below. The data covers a wide range of age starting from newborns to around 90 years old. 

![](pics/age_dist.png)

On comparing the male vs female age distribution, we see that both the genders are well represented for all ages.

![](pics/age_dist_gender.png)

Finally, we can look at the scatter plot of age vs height. This plot is of particular interest as this is the relationship we would like to capture in a probabilistic model.

![](pics/age_vs_height.png)

As expected, the height seems to eventually plateau with age. For this dataset, that plateau seems to be occurring around age of 20. Moreover, male heights seem to be taller than females, in general. As this data was collected in a time span of 2 years, the decrease in height with ag towards the end is a very interesting feature. At a high-level, this indicates that younger generation is taller than the older generation which hints towards an improving lifestyle and better nutrition. Overall, the relationship is very non-linear in nature and can't be captured by a simple linear relationship between height and age.