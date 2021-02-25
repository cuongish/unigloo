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


def main():
    # Aggregate list of products
    product_results: Dict[Text, DataFrame] = {}
    for category in categories:
        product_results[category] = pd.DataFrame(data=get_listing_of_product(category))
    product_df = reduce(lambda first, second: first.append(second, sort=True),
                        remove(lambda df: df.empty, product_results.values()), pd.DataFrame())

    # Find out list of manufacturers
    manufacturers = list(product_df.manufacturer.unique())
    time.sleep(1.5)

    # Get complete inventory database
    inventory_list = [get_availability(manufacturer) for manufacturer in manufacturers]
    inventory_df = tabulate_availability(inventory_list)

    # Get final dataframes
    handler = Handler()
    handler.facemasks = pd.merge(left=product_results[facemasks], right=inventory_df, on='id')
    handler.gloves = pd.merge(left=product_results[gloves], right=inventory_df, on='id')
    handler.beanies = pd.merge(left=product_results[beanies], right=inventory_df, on='id')

    return handler


if __name__ == '__main__':  # pragma: no cover
    main()
