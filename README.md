# 📊 Price Range Analysis & Rating Insights

## 📌 Overview
This project analyzes restaurant price ranges and their relationship with customer ratings. It also explores how rating colors correspond to performance levels and visualizes key trends in the dataset.

## 🎯 Objective
- Identify the most common price range of restaurants  
- Analyze average ratings across different price ranges  
- Explore rating distribution based on color indicators  
- Visualize price and rating relationships  

## 🛠️ Tools & Technologies
- Python  
- Pandas  
- Matplotlib  

## 📂 Dataset Details
The dataset includes:
- Restaurant Name  
- Aggregate Rating  
- Price Range  
- Rating Color  
- Votes  

## 🔍 Methodology

### 1. Price Range Distribution
- Counted number of restaurants in each price category  
- Identified the most frequent price range  

### 2. Rating Analysis by Price
- Calculated average rating for each price range  

### 3. Rating Color Analysis
- Grouped restaurants by rating color  
- Calculated average rating for each color  
- Identified the highest performing color category  

### 4. Visualization
- Bar chart for:
  - Price Range Distribution  
  - Average Rating by Price Range  

## 📊 Key Insights

- **Price Range 1** has the highest number of restaurants (~4444)  
- As price range increases, number of restaurants decreases  

- Average ratings increase with price:
  - Price 1 → ~2.0  
  - Price 2 → ~2.94  
  - Price 3 → ~3.68  
  - Price 4 → ~3.81  

👉 Higher-priced restaurants generally have **better ratings**

- Rating color insights:
  - **Dark Green** → Highest rating (~4.65)  
  - **Green** → High rating (~4.16)  
  - **Orange/Red** → Medium/Low ratings  
  - **White** → Lowest (no rating / poor data)  

## 📷 Output



## 🚀 How to Run

1. Install required libraries:
```bash
pip install pandas matplotlib
```

2. Run the script:
```bash
python "Task 5.py"
```

## 📁 Project Structure

```
Price-Range-Analysis/
│
├── Task 5.py
├── Dataset.csv
├── price_distribution.png
├── avg_rating_price.png
└── README.md
```

## 🚀 Conclusion
This analysis shows a strong relationship between pricing and customer satisfaction. Higher-priced restaurants tend to deliver better experiences, reflected in higher ratings. Rating colors also effectively represent quality levels.

---

