from pathlib import Path


def import_config(import_file: str) -> dict[str, dict[str, list[str]], dict[str, int], str, Path, str]:
    """Import required program settings from the configuration file
        Looks like a very ugly data structure to return, but the unpacking is neat and happens only once in main.py

    Args:
        import_file: string for path to file
    Returns:
        packed_data: a dictionary containing imported values
            proxy_sources: a sub-dictionary of lists containing urls to proxy information
            program_options: a sub-dictionary containing numeric options, such as concurrent checks and timeouts
            test_urls: list of urls to test against
            output_dir: path to file to write alive proxies
            error_code: a code representing different types of issues with the configuration file, so users can be promoted appropriately
    """

    proxy_sources = {
        'socks5':[],
        'socks4':[],
        'http':[],
        'https':[],
    }
    program_options = {
        'timeout':5,
        'fetchtimeout':5,
        'concurrentchecks':1000,
    }
    test_urls= []
    export_path = ""
    error_code = '00'

    with open(import_file, "r", encoding="utf-8") as f:
        file_import = [line.strip() for line in f]

    # Adds urls to proxy_sources dictionary based on proxy type specificed in config file
    currentType = None
    for line in file_import:
        if line.startswith("[") and line.endswith("]"):
            currentType = line[1:-1].lower()
        else:
            # Ignore commented lines, otherwise process accordingly
            line = None if '#' in line else line
            if line and currentType is not None:

                # Square bracket value indicates proxy type
                if currentType in proxy_sources:
                    proxy_sources[currentType].append(line)
                # Square bracket value indicates test urls
                elif currentType == "test-urls":
                    test_urls.append(line)
                # Square bracket value indicates export path
                elif currentType == "export-path":
                    export_path = line
                # Square bracket value indicates program options
                elif currentType == "options":
                    # Split line around semicolon
                    line_cleaned = line.replace(" ", "").lower()
                    selected_option, split_point, value = line_cleaned.partition(":")

                    if selected_option in program_options:
                        try:
                            program_options[selected_option] = int(value) if value.isdigit() else value
                        except ValueError:
                            # User has entered invalud non-int number under [options], e.g. "Timeout: 5.5".
                            error_code = '01'
                    else:
                        # User has entered invalid option under [options], e.g. "timeuot".
                        error_code = '02'
                else:
                    # If currentType is not a type of proxy type, or "options", then the config file is wrong.
                    error_code = '03'

                output_dir = Path(export_path)
                output_dir.mkdir(exist_ok=True)

    packed_data = {
        "proxy_sources": proxy_sources,
        "program_options": program_options,
        "test_urls": test_urls,
        "output_dir": output_dir,
        "error_code": error_code,
    }

    return packed_data
