from flask import Flask, render_template
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet
from iconsdk.builder.call_builder import CallBuilder
import ast
test_node_uri = "https://bicon.net.solidwallet.io/api/v3"
local_node_uri = "http://127.0.0.1:9000/api/v3"
network_id = 3
test_score_address = "cx5bf48c165d5d0dcf77833d4d3b7f607698af55cc"
local_score_address = "cx447610af9484ed8b216e93b98a1eb0d730432a77"
# keystore_path = "../bomb_keystore"
# keystore_pw = "@icon111"
wallet = KeyWallet.load("../keystore/keystore_test1", "test1_Account")
wallet_address = wallet.get_address()
# wallet = KeyWallet.load(keystore_path, keystore_pw)
# tester_addr = wallet.get_address()
# # Creates an IconService instance using the HTTP provider and set a provider.
icon_service = IconService(HTTPProvider(test_node_uri))
# # Gets a block by a given block height.
# block = icon_service.get_block(1209)
# print(block)
# call = CallBuilder().from_(tester_addr)\
#                     .to(fcfs_address)\
#                     .method("hello")\
#                     .build()
# result = icon_service.call(call)
app = Flask("First Come First Served")
@app.route("/")
def home():
    params = {}
    call = CallBuilder().from_(wallet_address) \
        .to(test_score_address) \
        .method("get_results") \
        .params(params) \
        .build()
    result = icon_service.call(call)
    transactions = []
    for data in result['result']:
        # change str to json(dict)
        transactions.append(ast.literal_eval(data))
    # print(transactions)
    return render_template("index.html", result=transactions)
app.run()