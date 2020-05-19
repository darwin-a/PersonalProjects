# The Age At Which Most People Are Dying By Suicide

| **Original** | **Mine**|
| --------- | --------|
|<img src = "https://i.postimg.cc/7YhnhvRm/deaths-by-age.png"></iframe>" width = "500">| <img src = "https://media.giphy.com/media/KZSFlqPEBIaDOKLL9D/giphy.gif" width = "500"> 

[Source](https://data.world/makeovermonday/2019w43) 


[Article](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/articles/middleagedgenerationmostlikelytodiebysuicideanddrugpoisoning/2019-08-13)


[Finished Visualization](https://public.tableau.com/views/MM2019W43_15790458278290/Dashboard1?:display_count=y&:origin=viz_share_link)


The goal of every makeover monday is to try and create a better visualization than the one given based on the context of the article.

This could have been done in different ways but I noticed one thing. The visualizations all

made a reference towards **generational suicide**, however none of the visualizations had this.

I took it upon myself to re-create the visualization to fit the context of the article better.


## What I did

I recreated the Visualization given in the [Source](https://data.world/makeovermonday/2019w43) and made it better

How I made it better

1. Data Enrichment (Give labels to each individual in the dataset)
	- Used Python and Pandas to create a generation column not present in the original dataset
	- Used Python and Pandas to create a column stating which year each individual was born
2. Data Visualization
	- With my new dataset I was able to show that suicide rates and poison deaths are higher for those born in **Generation X**
	- The old dataset made the consumer have to look at a general age (40-50) to prove that point.
	- This reduces the amount of work the consumer has to do so they can grab the idea relatively quickly. 	
	
