export PROJECT_PATH=$(pwd)

# echo $PROJECT_PATH
# echo $PROJECT_PATH/examples/PPO_finetuning

python -m hydra1 \
       -cp $PROJECT_PATH/examples/PPO_finetuning \
       -cn local_gpu_config
