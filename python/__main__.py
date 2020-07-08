from modules import process_files, utils


def main():
    config: utils.ConfigVars = utils.get_variables()
    config["parallel"] = True
    file_paths: list = ["../data/log_data", "../data/song_data"]
    process_files.iterate_paths(file_paths, config)


if __name__ == "__main__":
    main()
