# coding: utf-8
import time
from functools import reduce
from typing import Text, List, Dict

import pandas as pd
import xmltodict
from funcy import remove
from pandas import DataFrame

from unigloo_lib import get_availability
from unigloo_lib import get_listing_of_product
from domain_types import Inventory

gloves = 'gloves'
facemasks = 'facemasks'
beanies = 'beanies'
categories = [gloves, facemasks, beanies]
product_df = 'product_df'


def tabulate_products() -> Dict[str, DataFrame]:
    product_results: Dict[Text, DataFrame] = {}
    for category in categories:
        product_results[category] = pd.DataFrame(data=get_listing_of_product(category))
    product_results[product_df] = reduce(lambda first, second: first.append(second, sort=True),
                                         remove(lambda df: df.empty, product_results.values()), pd.DataFrame())

    return product_results


def select_distinct_manufacturers(product_results: Dict[Text, DataFrame]) -> List[Text]:
    manufacturers = list(
        product_results[product_df].manufacturer.unique())

    return manufacturers


def get_complete_inventory_data(manufacturers: List[Text]) -> List[List[Dict]]:
    inventory_list = [get_availability(manufacturer) for manufacturer in manufacturers]

    return inventory_list


def tabulate_availability(inventory: List[List[Dict]]) -> DataFrame:
    inventory_list = []
    for x in inventory:
        for i in x:
            inventory_list.append(Inventory(id=i.get('id').lower(),
                                            inventory=xmltodict.parse(
                                                i.get('DATAPAYLOAD'))['AVAILABILITY']['INSTOCKVALUE']
                                            )
                                  )

    return pd.DataFrame(data=inventory_list)


class Handler:
    def __init__(self):
        self.gloves = None
        self.facemasks = None
        self.beanies = None

    def export_final_df(self, product_results: Dict[Text, DataFrame], inventory_df: DataFrame):
        self.facemasks = pd.merge(left=product_results[facemasks], right=inventory_df, on='id')
        self.gloves = pd.merge(left=product_results[gloves], right=inventory_df, on='id')
        self.beanies = pd.merge(left=product_results[beanies], right=inventory_df, on='id')


def main():
    # Aggregate list of products
    product_results = tabulate_products()

    # Aggregate distinct manufacturers
    manufacturers = select_distinct_manufacturers(product_results)

    # Get complete inventory list SLOW subprocess
    complete_inventory_data = get_complete_inventory_data(manufacturers)

    # Aggregate complete inventory DF
    inventory_df = tabulate_availability(complete_inventory_data)

    # Join products and inventory
    handler = Handler()
    handler.export_final_df(product_results, inventory_df)

    return handler


if __name__ == '__main__':  # pragma: no cover
    main()
