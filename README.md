# greenops-ai-dashboard

# Hurdle 0 – Concept Check
1. What is a Resource Group in Azure, and why do we use one?

A Resource Group is a logical container that holds related Azure resources. It helps organize, manage, monitor, and control resources together.

2. What is the difference between a virtual environment and a global Python installation?

A global Python installation is shared across all projects, while a virtual environment provides an isolated workspace with its own packages and dependencies for a specific project.

3. Why is version control important from Day 1 of a project?

Version control tracks changes, enables collaboration, maintains history, allows rollback to previous versions, and helps prevent loss of work.

# Hurdle 1 – Concept Check
1. What does CO2e mean and why is it used as the standard unit for carbon accounting?

CO2e (Carbon Dioxide Equivalent) is a standardized metric used to measure the impact of different greenhouse gases in terms of the amount of carbon dioxide that would produce the same warming effect. It allows emissions from multiple gases to be compared and aggregated using a single unit, making carbon accounting more consistent and easier to understand.

2. Why is it important to separate emission factors by resource type rather than using a single flat rate?

Different cloud resources consume energy in different ways. CPU compute, storage, and data transfer have distinct power requirements and environmental impacts. Using separate emission factors provides a more accurate estimate of carbon emissions and helps identify which resources contribute most to the overall footprint.

3. What is the most carbon-intensive service type in your dataset?

The most carbon-intensive service type is the one with the highest total CO2e value after grouping the dataset by service_type and summing the co2e_kg column. Based on the analysis performed in the dataset, the service category with the largest CO2e contribution should be reported as the most carbon-intensive service.

# Hurdle 2 - Concept Check
1. Difference between Azure Blob Storage and Azure SQL Database?

Azure Blob Storage stores unstructured files such as CSVs, images, backups, logs, and model artifacts. It is cost-effective and scalable.

Azure SQL Database stores structured relational data in tables and supports SQL queries, transactions, indexing, and relationships.

Use Blob Storage for files and datasets. Use Azure SQL Database when data must be queried, filtered, and managed relationally.

2. What is LRS replication and what are its limitations vs GRS?

LRS (Locally Redundant Storage) stores three copies of data within a single Azure datacenter. It provides protection against local hardware failures at low cost.

GRS (Geo-Redundant Storage) stores additional copies in a secondary geographic region, providing disaster recovery if an entire region fails.

Limitation of LRS: it does not protect against regional outages.

3. Why is it a security risk to hardcode a connection string in source code?

Hardcoding connection strings exposes credentials to anyone with access to the code repository. If pushed to GitHub, attackers could access cloud resources, read data, modify resources, or incur costs. Environment variables or .env files should be used instead.
