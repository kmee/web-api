# Copyright 2021 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Endpoint Auth API key",
    "summary": """Provide API key auth for endpoints.""",
    "version": "14.0.1.2.1",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["simahawk"],
    "website": "https://github.com/OCA/web-api",
    "depends": ["endpoint", "auth_api_key_group"],
    "demo": ["demo/api_key_demo.xml", "demo/endpoint_demo.xml"],
    "data": ["views/endpoint_view.xml"],
}
