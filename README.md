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
