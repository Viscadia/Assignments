# Associate Consultant – SDE Role Assignment

Welcome to the assignment for candidates applying to the **Associate Consultant** position at **Viscadia**. This is a take-home evaluation designed to assess your technical depth, analytical thinking, and approach to solving real-world ETL and cloud infrastructure problems.


## 📦 Folder Structure

- `data/`
  - `data_gen.py`: Script to generate synthetic data
  - `enum_config.py`: Enum configuration used in data generation
- `deliverables/`: Submit your assignment files here
- `README.md`: Instructions for the assignment


## 🔧 Getting Started

1. **Fork** this repository.
2. Run the `data/data_gen.py` script. This will generate the following input files:
   - `products.csv`
   - `customers.json`
   - `sales/` folder containing 150 daily `.xlsx` files
   - `inventory.csv`
3. Begin your work and place all deliverables in the `deliverables/` folder.


## ⏰ Submission Timeline

You will be given **X hours/days** (timeframe to be finalized by the recruitment team) to complete and submit the assignment.


## 📌 Problem Overview

You are expected to:

### 1. **Data Cleaning**

- Clean inconsistencies, missing values, and formatting issues across all generated files.

### 2. **ETL Pipeline Design**

- `sales/` contains 150 separate Excel workbooks, each representing sales for a single day.
- Design an ETL pipeline capable of ingesting, transforming, and loading this data at scale.
- **Preferred Approach**: Use **PySpark** to demonstrate a distributed pipeline.
  - You may share core logic and explanations via markdown cells.
  - A complete implementation is not expected; focus on clarity and approach.
- **Alternate Approach** (if unfamiliar with PySpark): Use **Pandas** with batching/loop-based ingestion.
  - Simulate scalability concerns and propose improvements.

### 3. **Data Warehousing**

- Define the final SQL schema to store the cleaned and transformed data.
- Use PostgreSQL/MySQL syntax.

### 4. **Cloud Architecture (AWS)**

- Design a cloud-based infrastructure to support your ETL process.
- Include services such as:
  - S3 (data storage)
  - Glue/Athena or EC2/SageMaker (compute)
  - RDS/Redshift (data warehouse)
  - Airflow/Lambda (orchestration)
- 📌 Draw your architecture by hand if time allows, or use tools like [draw.io](https://draw.io), Lucidchart, etc.


## 🌟 Bonus Question (Optional)

We encourage you to attempt the optional question listed below. While not mandatory, it may earn you extra credit during evaluation.

### Final Interview Bonus Question (Visualization + SQL + Procedure + Window Function)

📝 **Scenario**You are provided with the following tables generated from the ETL pipeline:

- `sales`: Records of daily drug sales
- `products`: Product metadata including category and price
- `customers`: Customer demographics, including region and segment
- `inventory`: Daily inventory levels for each product

Each sale is linked to a product and a customer. Each product belongs to a category. Some products are approaching stockout, and the business wants to proactively monitor performance and supply risk.

### Your Task

1. **Write a SQL Stored Procedure** that returns the **top 3 selling products per region** over the **past 2 months**.
2. **Design a visual dashboard** using any tool (Jupyter/Excel/Tableau/Power BI/Markdown) that includes the following views:

   - A **bar/column chart** showing the **top 3 selling products per region**
   - A **highlighted table** or visual cue for **products with inventory levels below reorder threshold**
   - A **monthly revenue trend chart**, broken down by **product category**
   - A **combined line/area chart** overlaying **sales vs. inventory levels** to detect **stockouts and overstock risks**

### Constraints and Requirements

- **Use SQL window functions** (e.g., `RANK`, `ROW_NUMBER`, `SUM OVER`) for ranking and cumulative revenue
- **Use multi-table joins** across `sales`, `products`, `customers`, and `inventory`
- **Design for performance**:
  - Suggest use of **indexes**, **partitioning**, or **materialized views** where applicable
- **Clearly justify**:
  - Your **SQL approach** in a markdown cell or `.md` file
  - Your **choice of chart types** and **any trade-offs** in the dashboard visuals

📂 Please place your SQL code and any dashboard screenshots or markdowns in the `bonus_answer.md` or a subfolder within `deliverables/`.


## ✅ Deliverables (inside `deliverables/` folder)

| File/Folder                        | Description                                               |
| ---------------------------------- | --------------------------------------------------------- |
| `etl_pipeline.ipynb`             | Jupyter notebook with ETL logic and markdown explanations |
| `aws_architecture.png/pdf`       | AWS Infra diagram (hand-drawn or digital)                 |
| `sql_schema.sql`                 | SQL schema for final transformed data                     |
| `bonus_answer.md` _(optional)_ | Answer to the bonus question, if attempted                |


## 🧠 Evaluation Criteria

You will be assessed on:

- **Data Cleaning** – Handling inconsistencies, nulls, and malformed records.
- **ETL Design** – Scalability, modularity, and realism of your pipeline.
- **Python Proficiency** – OOP, functional design, use of decorators or patterns.
- **SQL Skills** – Schema design, joins, and query logic.
- **Cloud Understanding** – Knowing AWS components and their interactions.
- **Communication** – Clarity of markdown explanations and assumptions.

---

_This assignment is confidential and intended solely for the candidate receiving it. Do not share or publish without permission._

For any clarifications, please contact your recruiter or point of contact at **Viscadia**.
