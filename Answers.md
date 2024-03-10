1. Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

-> Product_Category Model represents product categories, serving as a reference table.

Product Model represents individual products, with a foreign key "category_id" linking each product to a specific category in the "Product_Category" table.

The relationship is one-to-many: Each product in the "Product" table is associated with exactly one category in the "Product_Category" table through the category_id foreign key.However, a single category in the "Product_Category" table can be linked to multiple products in the "Product" table.
