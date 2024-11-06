# Amazon Workout Tools Data Project

 This project is a data engineering pipeline designed to extract, transform, and visualize workout tools data (e.g., dumbbells, push-up bars, pull-up bars) from Amazon. Developed as a graduation project for Dotpy Company, the pipeline uses Python, REST APIs, Pandas, Excel, and Power BI to deliver insights into the workout equipment market.

## Project Overview

 This project aims to build a data pipeline for analyzing workout tools available on Amazon. The pipeline consists of three main stages:

1. **Data Extraction**: Collecting data from Amazon product listings using Python and REST APIs.
2. **Data Transformation**: Cleaning and processing the data with Pandas and Excel.
3. **Data Visualization**: Creating an advanced Power BI dashboard to visualize product insights.

## Project Structure

### Data Extraction

Data is extracted from Amazon product pages for the following categories:
- Dumbbells
- Push-Up Bars
- Pull-Up Bars

**Techniques**:

- Python's `requests` library is used to make REST API calls to Amazon's endpoints.
- Pagination is implemented to gather data from multiple pages (3 pages per product category).

**Sample Extracted Fields**:

- Product Name
- Price
- Rating
- Number of Reviews

### Data Transformation

Data transformation is performed using Pandas and Excel. The transformation process includes:

1. **Cleaning**: Removing duplicates and handling missing values.
2. **Data Standardization**: Converting price formats, ratings, and review counts into numeric values.
3. **Aggregation**: Aggregating data to derive insights, such as average price per category and average rating.
4. **Export**: Saving the cleaned data as `.csv` files for visualization.

## Data Visualization

The cleaned and processed data is visualized using Power BI. The dashboard provides insights on:

- Average product price by category
- Distribution of ratings across products
- Top-rated products per category
- Price trends and comparisons across different categories

## Technologies Used

- **Python**: Data extraction and transformation
- **Pandas**: Data cleaning and transformation
- **Excel**: Additional data manipulation
- **Power BI**: Data visualization and dashboard creation
