from setuptools import setup

setup(
    name='babyai',
    version='0.1.0',
    license='BSD 3-clause',
    keywords='memory, environment, agent, rl, openaigym, openai-gym, gym',
    packages=['babyai', 'babyai.levels', 'babyai.utils'],
    install_requires=[
        'gym',
        'numpy>=1.17.0',
        "torch>=0.4.1",
        'blosc>=1.5.1',
        # 'gym_minigrid @ https://github.com/maximecb/gym-minigrid/archive/master.zip'
    ],
)
