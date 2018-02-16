# -*- coding: utf-8 -*-
# Copyright 2018 Vignesh @ Annadurai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Click and Edit Form Fields',
    'category': 'Extra Tools',
    'summary': 'Click over the field and edit the form fields without clicking EDIT button',
    'version': '11.0.1.0.0',
    'author': " Vignesh ",
    'website': "viki2.odoo.com",
    'license': 'AGPL-3',
    'images':['images/main1.png','images/main2.png'],
    'depends': ['base','web'],
    'data': [
	'views/form_field_edit.xml',
    ],
    'installable': True,
    'auto_install': False,

}
