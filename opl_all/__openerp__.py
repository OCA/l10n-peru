# -*- coding: utf-8 -*-                                                       #
##
#    Module Writen to OpenERP, Open Source Management Solution                #
#                                                                             #
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com                        #
#    All Rights Reserved.                                                     #
#    info@vauxoo.com                                                          #
##
#    Coded by: Sabrina Romero (sabrina@vauxoo.com)                            #
##
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU Affero General Public License as           #
#    published by the Free Software Foundation, either version 3 of the       #
#    License, or (at your option) any later version.                          #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU Affero General Public License for more details.                      #
#                                                                             #
#    You should have received a copy of the GNU Affero General Public License #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
##

{"name": "OpenERP Peruvian Localization",
    "version": "",
    "author": "Vauxoo",
    "category": "Localization/Application",
    "description": """
Install all apps needed to comply with Peruvian laws plus all oficial modules
=============================================================================

This module will install for you:

  - OPL module

  - All oficial modules (account, stock, mrp, etc.)

                    """,
    "website": "http://www.vauxoo.com/",
    "license": "AGPL-3",
    "depends": [
                "opl",
#                Start list of all oficial modules
                "account",
                "auth_openid",
                "event",
                "l10n_bo",
                "l10n_pe",
                "pad_project",
#                "project_mrp",    [Migration V8]
                "account_accountant",
                "auth_signup",
#                 "event_moodle",    [Migration V8]
                "l10n_br",
                "l10n_pl",
#                 "plugin",  [Migration V8]
                "project_timesheet",
                "account_analytic_analysis",
                "base_action_rule",
                "event_sale",
                "l10n_ca",
                "l10n_pt",
#                 "plugin_outlook",  [Migration V8]
                "purchase",
                "account_analytic_default",
#                 "base_calendar",   [Migration V8]
                "fetchmail",
                "l10n_ch",
                "l10n_ro",
#                 "plugin_thunderbird",  [Migration V8]
#                 "purchase_analytic_plans",#Error to fix
#                 "account_analytic_plans",#Error to fix
                "base_gengo",
                "fleet",
                "l10n_cl",
                "l10n_si",
                "point_of_sale",
                "purchase_double_validation",
                "account_anglo_saxon",
                "base_iban",
#                "google_base_account", [Migration V8]
                "l10n_cn",
                "l10n_syscohada",
                "portal",
                "purchase_requisition",
                "account_asset",
                "base_import",
#                "google_docs", [Migration V8]
                "l10n_co",
                "l10n_th",
#                "portal_anonymous",    [Migration V8]
                "report_intrastat",
                "account_bank_statement_extensions",
                "base_report_designer",
                "hr",
                "l10n_cr",
                "l10n_tr",
                "portal_claim",
                "report_webkit",
                "account_budget",
                "base_setup",
                "hr_attendance",
                "l10n_de",
                "l10n_uk",
#                "portal_crm",  [Migration V8]
                "resource",
                "account_cancel",
#                "base_status", [Migration V8]
                "hr_contract",
                "l10n_ec",
                "l10n_us",
#                "portal_event",    [Migration V8]
                "sale",
                "account_chart",
                "base_vat",
                "hr_evaluation",
                "l10n_es",
                "l10n_uy",
#                "portal_hr_employees", [Migration V8]
#                "sale_analytic_plans",# Error to fix
                "account_check_writing",
                "board",
                "hr_expense",
                "l10n_et",
                "l10n_ve",
                "portal_project",
                "sale_crm",
#                "account_followup",    [Migration V8]
                "claim_from_delivery",
                "hr_holidays",
                "l10n_fr",
                "l10n_vn",
                "portal_project_issue",
                "sale_journal",
                "account_payment",
                "contacts",
                "hr_payroll",
                "l10n_fr_hr_payroll",
                "lunch",
#                "portal_project_long_term",    [Migration V8]
                "sale_margin",
#                "account_report_company",  [Migration V8]
                "crm",
                "hr_payroll_account",
                "l10n_fr_rib",
                "mail",
                "portal_sale",
                "sale_mrp",
                "account_sequence",
                "crm_claim",
                "hr_recruitment",
                "l10n_gr",
                "marketing",
                "portal_stock",
                "sale_order_dates",
                "account_test",
                "crm_helpdesk",
                "hr_timesheet",
                "l10n_gt",
                "marketing_campaign",
#                "process", [Migration V8]
                "sale_stock",
                "account_voucher",
#                "crm_partner_assign",#Make a error of geolocalization:
#                https://bugs.launchpad.net/openobject-addons/+bug/1295545
                "hr_timesheet_invoice",
                "l10n_hn",
                "marketing_campaign_crm_demo",
                "procurement",
                "share",
                "analytic",
                "crm_profiling",
                "hr_timesheet_sheet",
                "l10n_hr",
                "membership",
                "product",
                "stock",
                "analytic_contract_hr_expense",
#                "crm_todo",    [Migration V8]
#                "idea",    [Migration V8]
                "l10n_in",
                "mrp",
                "product_expiry",
                "stock_invoice_directly",
                "analytic_user_function",
                "decimal_precision",
                "knowledge",
#                "l10n_in_hr_payroll",# Error
#                https://gist.github.com/moylop260/21f158bd24a59ade583b
                "mrp_byproduct",
#                "product_manufacturer",    [Migration V8]
#                "stock_location", #Error to fix
                "anonymization",
                "delivery",
                "l10n_ar",
                "l10n_it",
#                "mrp_jit", [Migration V8]
                "product_margin",
#                "stock_no_autopicking",    [Migration V8]
                "association",
                "document",
                "l10n_at",
                "l10n_lu",
                "mrp_operations",
                "product_visible_discount",
                "subscription",
#                "audittrail",  [Migration V8]
#                "document_ftp", # No test
                "l10n_be",
                "l10n_ma",
                "mrp_repair",
                "project",
                "survey",
                "auth_crypt",
#                "document_page",   [Migration V8]
                "l10n_be_coda",
                "l10n_multilang",
                "multi_company",
#                "project_gtd", [Migration V8]
                "warning",
#                "auth_ldap", # No test
#                "document_webdav", [Migration V8]
                "l10n_be_hr_payroll",
                "l10n_mx",
                "note",
                "project_issue",
                "web_analytics",
                "auth_oauth",
                "edi",
                "l10n_be_hr_payroll_account",
                "l10n_nl",
                "note_pad",
                "project_issue_sheet",
                "web_linkedin",
#                "auth_oauth_signup",   [Migration V8]
                "email_template",
                "l10n_be_invoice_bba",
                "l10n_pa",
                "pad",
#                "project_long_term",   [Migration V8]
#                "web_shortcuts"    [Migration V8]
#               End list of all oficial modules.
    ],
    "demo": [],
    "data": [],
    'test': [],
    "installable": True,
    "active": False, }
