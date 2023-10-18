1. Spawn a process for the RL code:
```bash
python -m lamorel_launcher.launch \
       --config-path ./examples/PPO_finetuning/ \ 
       --config-name ./examples/PPO_finetuning/local_gpu_config \
       rl_script_args.path=./examples/PPO_finetuning/main.py \
       rl_script_args.output_dir=./out \
       lamorel_args.accelerate_args.machine_rank=0 \
       lamorel_args.llm_args.model_path=PATH_TO_YOUR_LLM
```

2. Spawn a process for the LLM:
```bash
python -m lamorel_launcher.launch \ 
       --config-path ./examples/PPO_finetuning/ \
       --config-name ./examples/PPO_finetuning/local_gpu_config \
       rl_script_args.path=./examples/PPO_finetuning/main.py \
       rl_script_args.output_dir=./out \
       lamorel_args.accelerate_args.machine_rank=1 \
       lamorel_args.llm_args.model_path=PATH_TO_YOUR_LLM
```