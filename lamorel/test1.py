import hydra
from lamorel import Caller, lamorel_init

lamorel_init()


@hydra.main(config_path="./conf/", config_name="config")
def main(config_args):
    lm_server = Caller(config_args)
    lm_server.close()


if __name__ == "__main__":
    main()
