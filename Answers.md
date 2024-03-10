1. Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

-> Product_Category Model represents product categories, serving as a reference table.

Product Model represents individual products, with a foreign key "category_id" linking each product to a specific category in the "Product_Category" table.

The relationship is one-to-many: Each product in the "Product" table is associated with exactly one category in the "Product_Category" table through the category_id foreign key.However, a single category in the "Product_Category" table can be linked to multiple products in the "Product" table.

2. How could you ensure that each product in the "Product" table has a valid category assigned to it?

->  
Foreign Key Relationship: The "Product" table includes a column (category_id) that serves as a foreign key.
This foreign key references the primary key column (id) in the "Product_Category" table.

One-to-Many Relationship: The relationship is structured as a one-to-many association, where each product belongs to one category.
A category, however, can be associated with multiple products.

Data Integrity through Foreign Key Constraint: A foreign key constraint is applied to the "Product" table to ensure that values in the category_id column must correspond to existing values in the primary key column of the "Product_Category" table.

Enforcement of Valid Assignments: When inserting or updating a product in the "Product" table, the database enforces the foreign key constraint.

Only valid category IDs existing in the "Product_Category" table can be assigned to products.
to follow these steps, we can ensure that each product in the "Product" table has a valid category assigned to it.
