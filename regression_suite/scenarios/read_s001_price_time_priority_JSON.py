import json

with open("./s001_price_time_priority.json") as f:
    config = json.load(f)

print(config["seed"])
print(config["exchange_config"]["stp_policy"])
print(config["agent_configs"][0]["params"]["arrival_rate_hz"])