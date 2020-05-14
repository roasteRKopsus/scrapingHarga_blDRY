import numpy as np
from price_capt_def import website_target
from site_input import site_terlaris

website_target(site_terlaris)
terlaris_array = np.array(website_target.productprice2)
