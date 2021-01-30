import os
import logging
import requests
import deepdiff
import json

MANGEMENT_BASE = 'https:///api/v1'

def load_products(org: str) -> str:
    requests
    api = f'{MANGEMENT_BASE}/apiProducts'


    pass

def load_json_file(filename: str) -> dict:
    with open(filename, 'r') as file:
        json_str = file.read()
    return json.loads(json_str)

def main():
    static_products_file = './apiProducts.json'
    managed_products = load_json_file(static_products_file)

    diff_products_file = './diff-apiProducts.json'
    edge_products = load_json_file(diff_products_file)
    
    unmanaged = deepdiff.DeepDiff(managed_products, edge_products, ignore_order=True)
    print(json.dumps(unmanaged))


if __name__ == '__main__':
    main()