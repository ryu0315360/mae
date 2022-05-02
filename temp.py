import argparse
import os
import uuid
from pathlib import Path
import torch

# import main_pretrain as trainer
# import submitit

# def main():
#     user = os.getenv("USER")
#     # print("This is user: ", user) # dongheelee
#     # print(Path("../checkpoint/"))
#     print(Path(f"/checkpoint/{user}/experiments"))
#     if Path("/checkpoint/").is_dir(): # ("/checkpoint")
#         p = Path(f"/checkpoint/{user}/experiments") # (f"/checkpoint/{user})~~
#         p.mkdir(exist_ok=True)
#         return p
#     else:
#         return print("fail")

# main()
# print(torch.cuda.is_available())
import pickle

pickle.load('/Users/dongheelee/Desktop/GitHub/mae/job_test/68751_submitted.pkl')
