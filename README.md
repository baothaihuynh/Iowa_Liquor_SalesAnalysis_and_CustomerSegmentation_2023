## **🔍Project Overview**  

- This is a project based on wholesale liquor sales data for the state of Iowa in the United States  with more than 2.6 million transactions in 2023. The Iowa government purchases liquor from suppliers and then distributes it to all retail or wholesale entities in the state. As a data analyst, I see this as a business operation issue for the Iowa state government to carry out the entire project.  

- This project focuses on in-depth analysis of the Iowa wholesale liquor market, providing insights into purchasing trends, customer segments, and sales performance. This project aims to help the Iowa state government in particular make data-driven decisions and optimize its business strategy. At the same time, it can also be considered a sample analysis for individuals or businesses involved in the alcohol industry for their own business purposes.  

- You can view and download the raw data for this project at [Website](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data).  


## **📌Business Goal**

- Customer segmentation based on purchasing behavior (RFM) using Machine Learning to provide more effective customer care strategies and gain a deeper understanding of their customers.  

- Analyze sales trends by product, geography, and time to make recommendations for optimizing inventory, product allocation, and order quantities.  

- Identify factors affecting sales and make recommendations to improve performance in 2024.  

- Provide market insights to support informed business decisions.  


## **🗂Work Scope**

- Gather and process Iowa wholesale liquor sales data from the official [Website](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy/about_data).  

- Analyze the data using statistical and machine learning techniques.    

- Create visualizations and reports to present the results.  

- Analyze market trends and make recommendations.  


## **💡Domain Knowledge**

#### **What is Customer Segmentation?**
![Image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GuPZRzN0IBLfyDCfn7-7NA.jpeg)  
Customer segmentation (also known as market segmentation) is a marketing practice of dividing a customer base into sub-groups. It could be according to geographic, demographic, psychographic, behavioral, and other characteristics. The key to effective segmentation is to divide customers into groups based on; the prediction of their value to the business. After that target each group with different strategies in order to extract maximum value from both high and low-profit customers.  
[Read more...](https://www.liveagent.com/academy/customer-segmentation/)

#### **Whate are RFM and K-Means in Customer Segmentation?**
![Image](https://clevertap.com/wp-content/uploads/2018/03/Incontent_image.png)  
RFM stands for Recency, Frequency, and Monetary Value, and it is a technique used in marketing and customer segmentation to analyze and categorize customers based on their transaction behavior. Each of the three components has a specific meaning:  

- Recency (R): How recently did the customer make a purchase?  

- Frequency (F): How often does the customer make purchases within a specific timeframe?  

- Monetary (M): How much money has the customer spent within a specific timeframe?  

RFM Customer Segmentation helps businesses better understand their customers, target specific segments with tailored marketing efforts, enhance customer loyalty, and increase profitability through optimized marketing strategies.  

K-Means is a clustering algorithm used for partitioning a dataset into a specified number of clusters based on the similarity of data points. When using K-Means with RFM analysis, you are essentially using the three RFM components as features to group similar customers into clusters. The algorithm aims to minimize the variance within each cluster and maximize the variance between clusters.  


## **💻Technologies and Tools**  

- Clean data: Using Python’s libraries like Pandas and Numpy.  

- Machine Learning: Using Python’s library Sklearn with KMeans algorithm.  

- Analysis: Using Python’s libraries like Scipy, Pandas and Numpy.  

- Visualization: Creating informative visualizations using Python’s libraries like Matplotlib, Seaborn and Power BI tool.  

- Dashboard: Using Power BI tool.  

- Insights Presentation: Summarize my findings and insights based on the analysis of the data set.  


## **🛠Work Reference**  

#### **I. Data Preparation**  

Using file: Iowa_Liquor_Preparation.ipynb

#### **II. Customer Segmentation Analysis**    

Using file: Iowa_Liquor_RFM_CustomerSegmentation.ipynb  

- 1. Read Summary Dataset  

- 2. Calculate RFM  

- 3. RFM Data Preparation  

- 4. Customer Segmentation using Machine Learning  

- 5. Conclusion  

#### **III. Sales Analysis**  

Using file: Iowa_Liquor_Analyze.ipynb  

`Case study questions:`  

- Dimension: Sales  

    - Question 1: What is the revenue, cost, and profit for each month?

    - Question 2: What is the monthly growth rate (MGR) of revenue?

    - Question 3: Is there any seasonal variation in revenue?

- Dimension: Orders

    - Question 4: How many orders are placed each month?

    - Question 5: What is the average revenue per order?

- Dimension: Customer

    - Question 6: How many monthly active customers (MACs) are there?

    - Question 7: What is the monthly retention rate (MRR)?

    - Question 8: What is the revenue and profit per customer?

    - Question 9: What is the revenue and profit per customer segment?

- Dimension: Product

    - Question 10: What are the top-selling products for the year?

    - Question 11: How many units of each product are sold each month?

    - Question 12: How many different wine products does each customer consume?

    - Question 13: Do customers who consume a more diverse variety of wines tend to purchase more products and generate more profit?

    - Question 14: Is the number of wine types consumed affected by customer segment?

- Dimension: Place

    - Question 15: Is the number of customers affected by geographic location?

    - Question 16: Is profit affected by geographic location?  

#### **IV. Dashboard**  

Using file: IowaLiquor2023_Dashboard.pbix  


`💭Thank you for reading!!!`
