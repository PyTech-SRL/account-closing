# Copyright 2013-2021 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Cut-off Picking",
    "version": "14.0.2.0.0",
    "category": "Accounting",
    "license": "AGPL-3",
    "summary": "Accrued and prepaid expense/revenue from pickings",
    "author": "Akretion,Odoo Community Association (OCA)",
    "maintainers": ["alexis-via"],
    "website": "https://github.com/OCA/account-closing",
    "depends": ["account_cutoff_base", "purchase_stock", "sale_stock"],
    "data": ["views/res_config_settings.xml", "views/account_cutoff.xml"],
    "images": [
        "images/accrued_expense_draft.jpg",
        "images/accrued_expense_journal_entry.jpg",
        "images/accrued_expense_done.jpg",
    ],
    "installable": True,
    "application": True,
}
