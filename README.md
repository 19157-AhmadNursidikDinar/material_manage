## Material Management Module

The "Material Management" module is an Odoo addon that extends the functionality of Odoo to manage materials used in a manufacturing process. It provides features for adding, editing, and deleting materials, along with their associated details such as material name, code, type, buy price, and related supplier information.

### Features

- Add new materials to the system.
- Edit existing materials and update their details.
- Delete materials that are no longer required.
- View the list of materials in both tree view and form view.
- Set the material type from predefined options: fabric, jeans, or cotton.
- Ensure the buy price of a material is greater than or equal to 100 through a constraint.

### Installation

1. Copy the "material_manage" folder to the Odoo addons directory.
2. Restart the Odoo server.
3. Install the "Material Management" module from the Odoo web interface or use the command-line to update the module.

### Usage

Once the "Material Management" module is installed, you can access the "Materials" menu under the "Sales" menu in Odoo. Here, you can manage the materials by adding, editing, and deleting records.

### Entity-Relationship Diagram (ERD)

Below is the Entity-Relationship Diagram (ERD) representing the main entities and their relationships in the "Material Management" module.

```
         +--------------+      +--------------+
         |   Material   |      |   Supplier   |
         +--------------+      +--------------+
         |              |      |              |
         | id           |1    *| id           |
         | name         |------| name         |
         | code         |      | address      |
         | type         |      | phone        |
         | buy_price    |      | email        |
         | supplier_id  |1     |              |
         +--------------+      +--------------+
```

In this ERD, we have two main entities:

- Material: Represents the materials used in the manufacturing process. It has attributes like `id`, `name`, `code`, `type`, `buy_price`, and a many-to-one relationship with the `Supplier` entity through the `supplier_id` field.

- Supplier: Represents the suppliers from which materials are purchased. It has attributes like `id`, `name`, `address`, `phone`, and `email`.

Please note that this is a simplified representation of the data model and may not include all attributes or relationships present in the actual implementation.

### Contributors

- [Ahmad Nursidik Dinar](https://github.com/19157-AhmadNursidikDinar) - Lead Developer

---
