Dear Students,

I hope you're all doing well. As discussed in class, your next homework assignment is an end-to-end data engineering project using the US campaign finance dataset provided in class. This project is designed to simulate a real-world scenario where you build a modular data pipeline on our Dataproc cluster using Jupyter Notebook and later transition the solution into a fully modular project in VS Code.

Below, you will find the detailed problem statement, project phases, and deliverables for this assignment.\
Project Deadline : 4th April 2025

* * * * *

### **Problem Statement**

You are tasked with developing a data engineering solution to analyze US campaign finance data for the 2019--2020 period. Your goal is to ingest data from multiple sources, clean and integrate the data, and prepare it for both predictive modeling and analytical reporting. You will create a robust, modular pipeline that adheres to industry best practices---including proper documentation, logging, and configuration management---while also producing meaningful visualizations and insights.

**Dataset Link** :-  <https://www.fec.gov/data/browse-data/?tab=bulk-data> (All information is provided here regarding the data)

* * * * *

### **Project Phases & Deliverables**

#### **Phase 1: Data Ingestion & Exploration**

-   **Objective:** Ingest the dataset from multiple sources and perform initial exploration.
-   **Tasks:**
    -   Ingest the application record data from a Google Cloud Storage bucket.
    -   Ingest the credit record data from a SQL Server database ( Keep 2 datasets in the SQL, use [filess.io](http://filess.io/) for free SQL server).
    -   Explore each dataset by printing schemas, displaying sample records, and generating summary statistics.
    -   Save the raw data in an efficient format (e.g., Parquet) in HDFS (Raw Layer).

#### **Phase 2: Data Cleaning & Transformation**

-   **Objective:** Clean, standardize, and enrich the ingested data.
-   **Tasks:**
    -   Handle missing values, correct data types, and normalize the datasets.
    -   Perform data enrichment (e.g., feature engineering such as vintage analysis to construct labels).
    -   Save the cleaned and processed data in the Processed Layer for further integration.

#### **Phase 3: Data Integration & Aggregation**

-   **Objective:** Integrate data from multiple sources and perform aggregations to derive business insights.
-   **Tasks:**
    -   Join the application and credit records on the client ID using optimized join strategies (broadcast, bucket, skew joins, etc.).
    -   Create aggregated datasets such as:
        -   Total orders per client.
        -   Average donation/campaign spending.
        -   Additional features for risk analysis.
    -   Save the integrated dataset for downstream analytics.

#### **Phase 4: Performance Optimization**

-   **Objective:** Optimize your entire data pipeline for scalability and efficiency.
-   **Tasks:**
    -   Apply caching, partitioning, and configuration tuning (e.g., adjusting shuffle partitions, executor memory).
    -   Implement advanced optimization techniques such as predicate pushdown and adaptive query execution.
    -   Ensure that each module adheres to industry best practices.

#### **Phase 5: Data Serving & Visualization**

-   **Objective:** Serve the final processed data for analysis and visualization.
-   **Tasks:**
    -   Save the final integrated dataset in optimized formats (e.g., Parquet and Hive tables) within our Dataproc environment.
    -   **Data Serving Deliverables -- Create at Least Five Visual Data Deliverables:**
        1.  **Total Donations per Candidate:** Aggregate total donation amounts over time for each candidate.
        2.  **Regional Donation Trends:** Analyze average donation amounts or spending by region/state.
        3.  **Monthly Campaign Spending:** Aggregate and visualize monthly campaign expenditure trends.
        4.  **Applicant Risk Analysis:** Use vintage analysis to segment applicants into 'good' and 'bad' categories.
        5.  **Donation Frequency & Distribution:** Create visualizations that display the frequency and distribution of donations.
    -   In your Jupyter Notebook, include embedded visualizations (using libraries such as Matplotlib or Seaborn) and flow diagrams that clearly present these deliverables.
    -   Document your data serving strategy in detail.

* * * * *

### **Final Deliverables**

1.  **Modular Project Code:**

    -   Submit your project as a set of modular Python scripts (or a well-structured VS Code project) that implements the complete data pipeline with proper logging, error handling, and configuration management. End to end code created based on logic of Jupyter Notebook.
2.  **Jupyter Notebook (IPYNB):**

    -   A comprehensive notebook that documents all the steps (from ingestion through serving) with embedded code, visualizations, and flow diagrams. This notebook should serve as both a summary and a presentation tool. All 5 jupyter notebooks. 
3.  **Project Report:**

    -   A detailed report (approximately 5 pages) covering:
        -   The problem statement and data sources.
        -   Architectural design and methodology.
        -   Key findings and business insights.
        -   Discussion of best practices and performance optimizations.
    -   Include diagrams, code snippets, and thorough explanations.
4.  **Data Serving Visual Deliverables:**

    -   At least five separate datasets/visualizations as specified above. These deliverables should demonstrate your ability to aggregate and transform data for various analytical use cases.
5.  **Documentation & Flow Diagrams:**

    -   Provide detailed documentation and flow diagrams explaining your overall pipeline. This will help you demonstrate your understanding of the project's structure and best practices, as well as prepare you for presenting your work in a professional setting. 
6.  **Share on Linkedin and tag me with the learnings and Architecture Diagram.

    **
7. ** Create a 10 minute video to explain the project properly - kinda company presentation. **

* * * * *

### **Additional Instructions**

-   **Modular Approach:**\
    Structure your project so that each module (Ingestion, Cleaning, Integration, Optimization, Serving) is self-contained. This approach simulates a production-grade data pipeline.

-   **Best Practices:**\
    Ensure that your code is well-commented, includes proper logging and error handling, and follows standard coding practices. Use configuration files or parameterized scripts for flexibility.

-   **Visualization & Documentation:**\
    Your Jupyter Notebook should include detailed visualizations and flow diagrams that explain your pipeline. These should be embedded within the notebook and used to illustrate your process clearly.

-   **Creativity & Innovation:**\
    Although the problem statement is defined, you are encouraged to explore additional insights and use cases. For example, consider analyzing donation trends over time, regional differences, or predictive risk modeling. Document any innovative approaches you take.

-   **Submission:**\
    Please submit your modular project code, Jupyter Notebook, final report, and all supplementary documentation by the deadline. Ensure all files are well-organized and clearly labeled.

* * * * *

If you have any questions or need further clarifications, please feel free to reach out. I look forward to seeing your creative and well-engineered solutions!

Best regards,

Mayank Aggarwal\
<https://www.linkedin.com/in/mayank953/>\
<https://www.youtube.com/@tech.mayankagg>

* * * * *

**PS :- **Request to see the class once where I have covered and would have answered every doubt as well. Further, make sure to send all the deliverables and try to draft it in the way I have done instead of just completing via AI. ( 100% AI based solution [ I will catch it somehow ] will be rejected).

**PPS** :- End to End project best practices will be covered in this weekend class. :)

**Prize**:- Top 3 students will be getting the prize.