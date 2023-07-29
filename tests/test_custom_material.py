# tests.py

from odoo.tests import common

class TestMaterial(common.TransactionCase):

    def test_material_buy_price_constraint(self):
        Material = self.env['material']
        supplier = self.env['supplier'].create({'name': 'Supplier A'})

        # Create a material with a buy price < 100
        with self.assertRaises(Exception):
            Material.create({
                'name': 'Test Material',
                'code': 'TEST001',
                'type': 'fabric',
                'buy_price': 50,
                'supplier_id': supplier.id,
            })

        # Create a material with a valid buy price
        material = Material.create({
            'name': 'Test Material',
            'code': 'TEST001',
            'type': 'fabric',
            'buy_price': 150,
            'supplier_id': supplier.id,
        })
        self.assertTrue(material)

    def test_material_type_filter(self):
        Material = self.env['material']
        supplier = self.env['supplier'].create({'name': 'Supplier B'})

        # Create materials with different types
        fabric_material = Material.create({
            'name': 'Fabric Material',
            'code': 'FAB001',
            'type': 'fabric',
            'buy_price': 200,
            'supplier_id': supplier.id,
        })
        cotton_material = Material.create({
            'name': 'Cotton Material',
            'code': 'COT001',
            'type': 'cotton',
            'buy_price': 180,
            'supplier_id': supplier.id,
        })

        # Filter materials by type
        fabric_materials = Material.search([('type', '=', 'fabric')])
        self.assertEqual(len(fabric_materials), 1)
        self.assertEqual(fabric_materials, fabric_material)

        cotton_materials = Material.search([('type', '=', 'cotton')])
        self.assertEqual(len(cotton_materials), 1)
        self.assertEqual(cotton_materials, cotton_material)
