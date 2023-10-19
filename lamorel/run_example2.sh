export PROJECT_PATH=$(pwd)

python -m lamorel_launcher.launch \
  -cp "$PROJECT_PATH/examples/PPO_finetuning" \
  -cn "local_gpu_config" \
  rl_script_args.path=$PROJECT_PATH/examples/PPO_finetuning/main.py \
  rl_script_args.output_dir=$PROJECT_PATH/out \
  lamorel_args.accelerate_args.machine_rank=1 \
  main_process_port=12347
