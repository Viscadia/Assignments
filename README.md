# Associate Consultant – SDE Role Assignment

Welcome to the assignment for candidates applying to the **Associate Consultant** position at **Viscadia**. This is a take-home evaluation designed to assess your technical depth, analytical thinking, and approach to solving real-world ETL and cloud infrastructure problems.

## 📦 Folder Structure

- `data.md` : Instructions to download data from AWS S3
- `deliverables/`: Submit your assignment files here
- `README.md`: Instructions for the assignment

## 🔧 Getting Started

1. Fork this repository.
2. Download the input files from [this AWS S3 link](https://assessment-case-study-data.s3.us-east-1.amazonaws.com/Assignment_AC/data.zip), which contains::
   - `products.csv`
   - `customers.json`
   - `sales/` folder containing 150 daily `.xlsx` files
   - `inventory.csv`
3. Begin your work and place all deliverables in the `deliverables/` folder.
4. Commit all your work directly to your fork.
5. Open a Pull Request (PR) named `submission-yourname` to the same branch of this repository as your submission .

### Important Notes

- Each candidate must open their own PR. Multiple PRs are not allowed (only one per candidate).
- Do not merge your PR. It will be used only for review and evaluation.
- Ensure all your deliverables are complete before opening the PR.
- If you face any issues with committing or submitting the PR, share the link to your forked repository directly with any person listed in the email invite for this test.
- If nothing works, compress your deliverables/ folder and send it to us via email or Google Drive.

## ⏰ Submission Timeline

You will be given **3** **hours** to complete and submit the assignment. You are allotted three (3) hours to complete and submit the assignment. Submit all completed work within this time frame. Partial submissions are acceptable.

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
- **Alternate Approach** (if unfamiliar with PySpark): Use **Pandas** and **Polars** with batching/loop-based ingestion.
  - Simulate scalability concerns and propose improvements.

### 3. **Data Warehousing**

- Define the final SQL schema to store the cleaned and transformed data.
- Use PostgreSQL/MySQL/SQlite syntax.

### 4. **Cloud Architecture (AWS)**

- Design a cloud-based infrastructure to support your ETL process.
- Draw your architecture by hand if time allows, or use tools like [draw.io](https://draw.io), Lucidchart, etc.

## 🌟 Bonus Question (Optional)

We encourage you to attempt the optional question listed below. While not mandatory, it may earn you extra credit during evaluation.

### Final Interview Bonus Question

You are provided with the following tables generated from the ETL pipeline:

- `sales`: Records of daily drug sales
- `products`: Product metadata including category and price
- `customers`: Customer demographics, including region and segment
- `inventory`: Daily inventory levels for each product

Each sale is linked to a product and a customer. Each product belongs to a category. Some products are approaching stockout, and the business wants to proactively monitor performance and supply risk.

### Your Task

1. Write a SQL Query that returns the top 3 selling products per region over the past 2 months.
2. Create a refreshable visual summary for the same.

### Constraints and Requirements

- **Design for performance**:
  - Suggest use of indexes, partitioning, or materialized views where applicable

Please place your SQL code and any dashboard screenshots or markdowns in the `bonus_answer.md` or a subfolder within `deliverables/`.

## ✅ Deliverables (inside `deliverables/` folder)

| File/Folder                     | Description                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| `sql_schema`                  | Pseudocode or representative SQL schema for the final transformed dataset |
| `aws_architecture.png/pdf`    | AWS architecture diagram (hand-drawn or digital) showing core components  |
| `etl_pipeline`                | Description of ETL approach, structure, and pseudocode-level logic        |
| `bonus_answer` _(optional)_ | Answer to the bonus question, if attempted                                |

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
