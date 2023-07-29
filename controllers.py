# controllers.py

from odoo import http
from odoo.http import request

class MaterialController(http.Controller):
    @http.route('/material_manage/delete_material', type='json', auth='user')
    def delete_material(self, material_id):
        """Override delete action to show a custom message"""
        Material = request.env['material'].sudo()
        material = Material.browse(int(material_id))
        if material:
            material.unlink()
            return {
                'message': 'Material with ID %s has been deleted successfully.' % material_id,
                'type': 'success',
            }
        return {
            'message': 'Material with ID %s not found or already deleted.' % material_id,
            'type': 'warning',
        }
