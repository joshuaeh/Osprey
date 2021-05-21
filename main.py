from code.Utilities import osprey, flock

# air_tag_url = "https://www.bestbuy.com/site/apple-airtag-silver/6461348.p?skuId=6461348"
name_link_dictionary = {
'NVIDIA3090' : 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434',
'NVIDIA3080' : 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
'NVIDIA3070' : 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442',
'NVIDIA3060TI' : 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402',
'Ventus3070' : 'https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3070-ventus-3x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card/6438278.p?skuId=6438278',
'ASUS3060' : 'https://www.bestbuy.com/site/asus-nvidia-geforce-rtx-3060-12gb-gddr6-pci-express-4-0-graphics-card-black/6460665.p?skuId=6460665',
# 'GIGABYTE6700XT' : 'https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6700-xt-gaming-oc-12gb-gddr6-pci-express-4-0-gaming-graphics-card/6457993.p?skuId=6457993',
# 'GIGABYTE6800XT' : 'https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6800-xt-gaming-oc-16gb-gddr6-pci-express-4-0-graphics-card/6453896.p?skuId=6453896',
'ASUS3080' : 'https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445',
'GIGABYTE3070' : 'https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?skuId=6437912',
'GEFORCE3080' : 'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400'
}

# osprey("3080", name_link_dictionary['NVIDIA3080'], headless=False)
if __name__ == '__main__':
    flock(name_link_dictionary)
