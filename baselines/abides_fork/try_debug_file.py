import json
from scenario_io import read_scenario
from config import build_config
import time
from abides_core import abides


config_path = "/users/cs/yitengz/agenthon/Agenthon-track3-simulation/regression_suite/scenarios/s001_price_time_priority.json"



# ----------------------------- 1.读取市场场景(完成类型转换) ----------------------------
# JSON object  → Python dict
# JSON array   → Python list
# JSON string  → Python str
# JSON number  → Python int / float
# JSON boolean → Python bool

scenario = json.loads(read_scenario(config_path))

# print(type(scenario))  # <class 'dict'>
# print(json.dumps(scenario, indent=2, ensure_ascii = False))
# -------------------------------------------------------------------------------------



# --------------------------------2.搭建完成,但尚未启动的市场场景------------------------
config = build_config(scenario)

# print(type(config))  # <class 'dict'>
# print(config.keys())
# dict_keys(['seed', 
#            'start_time', 
#            'stop_time', 
#            'agents', 
#            'agent_latency_model', 
#            'default_computation_delay', 
#            'custom_properties', 
#            'random_state_kernel', 
#            'stdout_log_level'
#         ])

# 交易所、交易者、规则和时钟都已就位
# 但还没有开始下单和撮合
# ------------------------------------------------------------------------------------



# --------------------------------3.真正启动市场模拟，以及测量时间 ----------------------
# t0 = time.perf_counter()       # 开始读数 t0, e.g. 开始读数 t0 = 100.00
end_state = abides.run(config)
# wall_clock_sec = time.perf_counter() - t0    
# 运行时间 = 当前读数 - 开始读数(t0)
# example, e.g. 运行时间 = 100.16 - 100.00 = 0.16 秒

# 真实时间（wall-clock time）：电脑实际运行多久。
# 例如 baseline 用了约 0.16 秒。

# 模拟时间（simulation time）：虚拟市场中经过多久。
# 在 s001 场景中模拟了 10 秒市场时间。


# print(type(end_state))  # <class 'dict'>
# print(end_state.keys())
# # dict_keys(['kernel_event_queue_elapsed_wallclock', 
# #            'kernel_slowest_agent_finish_time', 
# #            'agents', 
# #            'message_ledger', 
# #            'deliver_seq_by_key'])




# ------------------------------------------------------------------------------------



























