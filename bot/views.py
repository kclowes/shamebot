from django.shortcuts import render
from django.http import HttpResponse


# more?
CAP_REPOS = [
    "ethereum/py-evm",
    "ethereum/trinity",
    "ethereum/web3.py",
    "ethereum/eth-utils",
    "ethpm/py-ethpm",
    "ethpm/ethpm-cli",
    "ethereum/vyper",
    "ethereum/py-wasm",
    "ethereum/lahja",
    "ethereum/eth-tester",
    "ethereum/eth-typing",
]


JPG_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:jpg)"
JPEG_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:jpeg)"
PNG_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:png)"


def index(request):
    # whitelist contributors
    # scrape pr for cap
    # add comment/link if dupe
    return HttpResponse("Shame")

def get_img_link_from_body(body):
    jpg = re.search(JPG_REGEX, body)
    if jpg: 
        return jpg.group()

    jpeg = re.search(JPEG_REGEX, body)
    if jpeg:
        return jpeg.group()

    png = re.search(PNG_REGEX, body)
    if png:
        return png.group()
    return None

