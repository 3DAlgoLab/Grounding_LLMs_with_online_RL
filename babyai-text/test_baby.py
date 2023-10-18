# %%
import gym
import babyai_text

env = gym.make("BabyAI-MixedTrainLocal")
print(env)

# %%
env.reset()
print(env.step(1))

# %%
