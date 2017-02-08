OPTIONS = [
    {'module': 'app_offer', 'display': 'App Offers'},
    {'module': 'attribute', 'display': 'Attributes'},
    {'module': 'brands', 'display': 'Brands'},
    {'module': 'categories', 'display': 'Categories'},
    {'module': 'issue_association', 'display': 'Issue Association'},
    {'module': 'issue', 'display': 'Issues'},
    {'module': 'manufacturers', 'display': 'Manufacturers'},
    {'module': 'products', 'display': 'Products'},
    {'module': 'related_products', 'display': 'Related Products'},
    {'module': 'reorder_C1', 'display': 'Reorder C1'},
    {'module': 'reorder_C2', 'display': 'Reorder C2'},
    {'module': 'reorder_C3', 'display': 'Reorder C3'},
    {'module': 'strings', 'display': 'Strings'},
    {'module': 'top_brands', 'display': 'Top Brands'},
    {'module': 'article', 'display': 'Articles'},
    {'module': 'product_messages', 'display': 'Product Messages'},
    {'module': 'source_based_configurations', 'display': 'Price, Buy Bar, Shipping and Message'},
    {'module': 'buy_bar_whitelisted_skus', 'display': 'Skip Buy Bar Visibility'},
]

__all__ = [option['module'] for option in OPTIONS]

# NOTE: This ensures that only above modules can be called
