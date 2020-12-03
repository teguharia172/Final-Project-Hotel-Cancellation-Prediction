# Final-Project-Hotel-Cancellation-Prediction
Exploratory Data Analysis, Machine Learning Modeling, and Local Dashboard Deployment of the machine learning model. data could be found from [here](https://www.kaggle.com/jessemostipak/hotel-booking-demand) .

For Dashboard with the tuned model please check it [here](https://drive.google.com/drive/folders/1Bh5uxq4kvW7s-19wHRIg197fcbJInyjc?usp=sharing)

![Final Project Proposal](https://user-images.githubusercontent.com/57277832/100371305-27dd8f00-303a-11eb-8789-8143683bde7e.png)


## About The Project: 

Predicting Hotel Booking Cancellation in Portugal Project. Is a machine learning classification project that will try to predict whether a booking will be cancelled or a booking will not be cancelled using machine learning based on historical data.

The data for this project is from [Hotel Booking Demand Dataset Sciencedirect](https://www.sciencedirect.com/science/article/pii/S2352340918315191#s0005). This data was acquired by extraction from hotel’s Property management system from 2015 to 2017 from hotel in Region Algarve and Lisbon

## Background Information: 

Hotel industry is one of the faster growing businesses of tourism sector, especially with the rise of giant OTA that make booking a hotel as easy as is ever been. 
[According to Portugal’s National Institute of Statistic](https://www.hotelnewsnow.com/Articles/286991/Portugals-tourism-boom-sparks-economics-hotel-growth) in 2017 hotel revenue rose approximately **18%**  to **$3.6 billion**.The growth of hotel industry also could be seen from the total number of [hotel guests in portugal doubled it's population count in 2017.](https://skift.com/2018/03/07/portugals-tourism-boom-has-caused-a-hotel-labor-shortage/) 

**Total of hotel guest in 2017: 20.6 Million** 

**Total Portugal Population in 2017: 10.31 Million**

**Plus according to Deloitte Hospitality Atlas 2019 Lisbon is nominated as the most attractive European Cities for hotel investment**


![Final Project Proposal (1)](https://user-images.githubusercontent.com/57277832/100372671-2ad97f00-303c-11eb-9fd9-ed5caf6cc1e7.png)


**However** the growing trend of the hotel industry comes with problems too, one of the problem is the rising rate of cancellation in the hotel industry [**Cancellation rate rose from under 33% in 2014 to 40% in 2018**](https://www.emerchantpay.com/infographic-how-can-hotels-combat-rising-cancellation-rates/)

## Problem Statement:

With the increase trend of cancellation from year to year, [some hotel have think that high cancellation in hotel is  the new norm of the industry](https://www.mirai.com/blog/cancellations-shooting-up-implications-costs-and-how-to-reduce-them/) which is a completely wrong approach,
[**one out of four hotel guests**](https://www.phocuswire.com/Hotel-distribution-market-share-distribution-analysis#:~:text=The%20average%20cancelation%20rate%20in,of%206.4%25%20over%20four%20years) are cancelling hotel booking ahead of a stay. This cancellation trend has effect the hotel not being able to accurately forecast occupancy within their revenue management, and the trend of cancellation also have causes hotel loss in opportunity cost **(unsold room due to cancellation)**

## Goals: 

**1.** The Goals of this project is to find out the characteristic  of customers who cancelled and finding a pattern in cancelled booking by doing an exploratory data analysis 

**2.** Building classification machine learning model to predict cancellation, that has accuracy score around 0.75 - 0.9

**3.** Build and Deploy web application / dashboard using flask from our machine learning algorithm,  that can predict of  cancellation based on user input


## Business Questions:

**List of Questions to help project goals**

- How Market Segment Of Booking Affecting Cancellation ?

- How’s a lead time of a booking affecting cancellation ?

- How’s different deposit type affecting cancellation of a booking ?

- How does cancellation rate of booking from portugal and booking that’s made outside portugal ?

- What Are The Other Factors that affecting cancellation of booking ?

- What machine learning algorithm that has the highest accuracy when it comes predicting hotel booking cancellations ?

## Workflow:

- **Data Cleaning :** 
  - Imputing missing value with median / mode **(based on the context)** using median instead of mean here because there are many outliers in the dataset 
  - **Dropping columns that has more than 30% missing values**
  - **Dropping rows with abnormal values**
    - 0 Total guests / adults in the booking 
    - **negative** daily rate
   - **Dropping** row with outliers that's super different compared to the other row in the columns 
      - Row with daily rate that's above **5000 euro**
      
 - **Exploratory Data Analysis :** 
    - Feature Engineering 
    - Binning 
    - Aggregating Columns
    - Visualization
    - Insight & Conclusion
  
 - **Feature Selection for machine learning process**
    - Label encoding for certain columns that needs to be encoded
    - association checking using dython
    - Feature selection based on EDA and dython association 
  
 - **Model Building**
    - Train Test Split
    - Using pipeline for model building 
      - scaling for numerical features
      - label encoder for categorical features
    - Creating base model with few algorithm *(Logistic Regression, K Neighbors Classifier, Decision Tree Classifier, Random Forest classifier, XGB Classifier)*
    - Checking evaluation matrix
    - Hyperparameter tuning on all algorithm
    - checking evaluation matrix on the tuned model
    - Export the model with the best accuracy score
    
 - **Dashboard Building Using Flask**
 
 
 <details>
  <summary><h2> Tl;dr (Summary)</h2></summary>
  
  <details>
    <summary><h2> Exploratory Data Analysis (Summary)</h2></summary>
  
## Conclusion & Recommendation


### Conclusion :


### 1. Market Segment & Booking Cancellation 

- *How does Market Segment of a booking affecting cancellation ?*

    - from our analysis we see that **corporate** , **Direct**, and **Aviation** has a cancellation rate around **18 - 22 %** of their booking
    - **Travel Agent (Online / Offline)** has a cancellation rate around **34 - 36 %**
    - Lastly **Group** has the highest cancellation rate around **61 %**

Based on this we conclude that **group booking are the market segment that's most likely to be canceled** compared to other market segment while **Direct has the lowest cancellation rate at 15%**  *(Outside Complimentary)*


### 2. Lead Time & Cancellation Rate
- *How does a Lead time of a booking **(arrival date - booking date) total days** affecting cancellation rate* 

    - in this case we group the lead time into monthly *(30 days month)* lead time to make it more general to analyze compared to a specific number of days 
    
For Lead time and cancellation rate we're comparing each monthly lead time confirmed booking & canceled rate. **Booking That has 0 - 7 months lead time** have a higher confirmed booking rate **( > 50%)** to it's canceled rate.


For **Booking that has more than 7 months lead time** have a higher cancelation rate **( > 50%)** to it's confirmed rate. Based on this pattern of lead time and cancellation we conclude that.

- booking that has **more than 7 months of lead time are more likely to be canceled** than confirmed
- **cancellation is positively correlated with lead time** *(the higher the lead time the higher the cancellation rate)*
- the shorter the lead time the **less likely the booking will be canceled**


### 3. Deposit Type & Cancellation Rate
- *How does a different Deposit type affecting booking cancellation*

    - This Dataset has 3 kinds of deposit type **NO Deposit, NO Refund, and Refundable**, all of the name is kind of self explanatory, based on our analysis we found out that:
    
- **No Refund Booking has the highest cancellation rate at 99.4%**
- **No Deposit has cancellation rate of 28.3 %**
- **While Refundable has cancellation rate around 22%**

For the hotels this is nothing alarming since they don't lose revenue when  no refund booking is canceled, but it's always a good practice to question something is extraordinary,  **why does non refundable booking are most likely to be canceled?** isn't just like wasting money cancelling your non refundable booking. To answer that question let's look at the median lead time of each deposit type


#### 3.1 Deposit Type & Lead Time

   - previously we found out that the longer lead time he more likely the booking will be canceled, the median lead time of each deposit type:
   
 - **Median Lead Time Non Refund 183 Days**
 - **Median Lead Time Refundable 169 Days**
 - **Median Lead Time No Deposit 56 Days**
 
 Looking at the median lead time it shows that **No Deposit** booking has the highest median lead time compared to the other booking and based on our analysis on lead time and cancellation it shows that higher lead time are more prone to cancellation compared to the short one this is definitely one of the reason why cancellation rate is high in **No Refund Deposit**


### 4.Cancellation & Booking Location 
-  How does cancellation rate of **booking that's made from Portugal** compared to the **booking that's made from outisde Portugal *(International)***

For booking location in this dataset we originally have **177 countries *(including Portugal)***, it's not efficient and not effective to aggregating every country with portugal in this one we split the **booking location into 2 Local (Booking that is from Portugal) and International (Booking Outside Portugal)**

- International Booking have **24% cancellation Rate** while Local Booking have **56% cancellation Rate**

**This arise question why does local booking are more likely to be canceled compared to international booking ?**

#### 4.1 Booking Location & Previously Cancellation
- comparison of previously canceled booking from 2 different booking location
    - From the Analysis **booking that's previously canceled have 92% cancellation rate**
    

For **International Booking 99.5%** of the booking were never canceled before comparison to the **local booking that only 87 %** booking that's never been canceled before this definitely play a factor why **Local Booking** has a higher cancellation rate compared to **International Booking** 


### 5. Factors That Affecting Cancellation

- aside from the "common cancellation variable" this dataset provide some other information that might have information about cancellation


#### 5.1 Repeated Guests & Cancellation

in this dataset we only have around **3%** of repeated guest, tho we still see the difference of cancellation pattern in both repeated guest and non repeated guest 

- **Repeated Guest has cancellation rate around 14%**
- **Non Repeated Guest are more than 2X more likely to cancelled the booking compared to repeated guest**

 
*in conclusion:*

**Repeated Guest are more likely to confirm their booking compared to non repeated guest** 


#### 5.2 Previous Cancellation & Cancellation


- **Booking that's previouly canceled have 92%  cancellation rate**
- **Booking that's originally wasn't canceled has 34% Cancellation rate**


**This shows that booking that's previously canceled will likely to be canceled again in the future**


#### 5.3 Parking Space & Cancellation 

this is one of the not common metrics to look at when it comes to predictiing cancellation and analyzing cancellation, however in this data set there are around **7407 (6.2 %)** that required car parking space(s).


out of **7407 Bookings** that require a parking space **there not a single booking thats Canceled (0 Cancellation)**

**this conclude that booking that required a parking space will high likely to be confirmed** 



#### 5.4 Booking Changes & cancellation

- Customer Who made booking Changes to their booking have a lower cancellation rate **(16%)** compared to the custoamers who never made booking changes to their booking **(41%)** 


#### 5.5 Special Request & Cancellation 

the number of special request(s) in a booking apperently affecting the cancellation rate of a booking from our analysis we see that booking that has no special request are more likely to canceled compared to booking that has a special request 

- **The cancellation rate of booking that has a special request is ranging from 5 - 22 % with booking with 5 special requests has the lowest cancellation rate** 

- **While Booking with no special request has cancellation rate of 48%**


## Recommendation


### Only Non Refundable Deposit For  Group Booking 

- from the analysis we see that group booking has the highest cancellation rate among all market segment, only allowing non refundable deposit for group booking will help protect the hotel from losing revenue due to last minute cancellation and not able to find replacement. **Only Allowing Non Refundable Rates might result in fewer bookings for Group**, however it might protect the hotel from losing revenue 

### Setting Maximum Lead Time for Booking

- we see a pattern that booking that has more than **210 days of lead** time are more likely to be canceled, setting up maximum lead time means it wont be able to make booking that's too far in advance (**> 210 days**), and setting maximum advance reservation will help you to reduce cancellation


### Combination of Restriction 

- as we know that booking that's made **210 days in advance** are more likely to result in cancellation, however setting up a maximum lead time for booking might have resulted visibility of the hotel in potential guest search. Combining deposit type policy with with the restriction might help the hotel get more exposure without higher risk of cancellation **(eg. Non Refundable Deposit for booking that's more than 210 days in advance**) or taking an partial advance payment for booking that's over **210 days**


### Additional Resource / Research For Local Customers 


- **56% of booking that's made in the Portugal are cancelled** this is hotel responsibility to research why does the local market are more likely to cancel compared to confirmed, and why does international customer are less likely to cancel. there are  intagible & tangible aspect in this research outside the PMS dataset, such as 
    1. **Comparison of hotel service satisfaction of local and international customers**
    
    
### Increase Direct Booking Market Segment 

- from this dataset we see that direct booking has the least cancellation rate **15%** *(outside complimentary)* compared to other market segment, with only being 10% of total booking market segment having more booking from direct market segment will likely to reduce the number of cancellation. 

**Strategy to increase Direct Booking**
1. *Leverage the power of a well optimized website* 
     - Visually attractive website
     - Offer & Ensure Best Rate Guarantee
     - Multilanguage & multi currency features 
     
     
2. *Increase Hotel Online Reputation*
    - Almost 98% of travelers read hotel reviews and 80% of them consider them extremely important before making the final reservation. **A one-point increase** in a hotel’s average user rating on a 5-point scale (eg, 3.8 to 4.8) makes potential customers **13.5% more likely to book that hotel**
    
    
3. *Offer Loyalty program with difference*
    - Incentivizing your guest with loyalty programs to book directly at the hotel website, by giving them points that could easily be redeemed not only at the hotel but at also at certain POS outlets
    

 Source : <a href = "https://www.hotelspeak.com/2019/05/9-strategies-to-increase-hotel-direct-bookings/">Hotel Speak</a>
 
 Direct Booking Impact : <a href = "https://www.hotelogix.com/blog/2019/04/22/the-impact-of-direct-bookings-on-your-hotel/?utm_medium=referral&utm_source=hotelspeak&utm_campaign=hoteldirectbookingblog04">Impact of Direct Booking towards the hotel </a>
 
### Stricter Cancellation For Previously Canceled Booking
 
- Booking that was previously canceled has **92% Cancellation Rate** looking at this pattern we know that booking that's **previously canceled are most likely to be canceled again**. to protect the hotel from losing revenue due to this pattern hotel need to **set booking payment in advance for booking that was canceled before**, this will help hotel preventing lose of revenue from last minute cancellation from this kind of booking


### Attracting Customer That Drive

- there are around **6% of total booking that required parking space (7407 bookings)** from July 2015 to August 2017, and out of 7407 **not a single one of the booking were canceled**, that amount is **around 10% of confirmed booking**. Hotel could promote to attract customer that drives



**Strategy to Attract More Customer Who Drives**

1. *Incetivize Customer Who Drives*
    - Free Valet Parking 
    - Free Charging for Electric Car
    - Free Parking
    
    
2. *Host The Launch of New Car*
    - Hosting a car event will more likely to bring customers who drives to the hotel, and we know that customers who drives never canceled their booking from this data 
    

  </details>
  

  <details>
    <summary><h2> Machine Learning (Summary)</h2></summary>
 
## Conclusion, Limitation & Improvement (Future Research)

*For Exploratory Data Analysis Conclusion Please Check The Other Notebook*


#### Conclusion

- **Tuned Random Forest Has The Best Accuracy Among All Algorithm That We Tried**
    - From all the evaluation matrix to predict hotel cancellation classification case, we see that  **Tuned Random Forest** has the best accuracy when it comes to predicting hotel cancellation based on certain features **(85.2 %)**


- **Reservation Status Column**
    - Reservation Status have 1.00 Association Value with the Target, because of the reservation status will tell whether the booking has been canceled, no show or checkout, using this column to build a model is prohibitted because you won't be able to predict future booking, since the future booking still doesn't have it status yet
    
    
    
- **Overfitting**
    - For the base model we see that there are only 2 algorithms that doesn't have an overfitting condition **(Logistic Regression & XGB)**
    
    - After Hyperparameter Tuning on all algorithm all of the algorithm don't have an overfitting condition, and after hyperparameter tuning **(Random Forest)** has the highest accuracy score 



- **Using Accuracy As The Primary Evaluation Metrics**

    1. The First Reason Why Accuracy is used as the evaluation metric here because we have somehow a balance data **63 % Confirmed Booking** and **37% Canceled Booking** in this case our dataset is balance and hence using accuracy is acceptable in this case 
    2. in this case **every class is equally important** 
    
    
- **How This Model Will Help Hotels ?**

    - this model will allow hotel managers / revenue manager to take actions on bookings that's identified as "potentially going to be canceled", **furthermore the development of these model should contribute to hotel revenue management.**
    - **These prediction models enable hotel managers to mitigate revenue loss derived from booking cancellations and to mitigate the risks associated with overbooking (reallocation costs, cash or service compensations, and, particularly important today, social reputation costs)**. Booking cancellations models also allow hotel managers to **implement less rigid cancellation policies, without increasing uncertainty**. This has the potential to translate into more sales, since less rigid cancellation policies generate more bookings 
    
    
 ## Limitation & Future Research 




- The machine learning model in this notebook implemented data from **City & Resort Hotels** in Portugal, which raise some question that further research will help to explain:



- **1**.**Can a similar result obtained from hotel outside of portugal ?**
- **2. Can Model have a better result if more hotels are integrated into the machine learning modeling?**
- **3. Is the result only specific of the type of hotels integrated into this modeling?**


- **Situation Limitation**
    - all of this booking are recording during 2015 - 2017, however now in 2020 we have a pandemic that's going on **(Covid - 19)**, this model needs to be double checked for current situation wheter a similar result obtained after the pandemic 

#### Further Research

- For further research weather information, hotel factors (star of the hotels, brand, and etc) could be included into the dataset in hope to  improve the models and measure the importance of these features


- Additional research with different location, additional hotel could contribute to a better understanding of booking cancellations
  
  
  </details> 
</details>

<details>
  <summary><h2> Notebook Highlight </h2></summary>
  
  
 ## Coming Soon
</details>
