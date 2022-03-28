import os
import re
import logging


def file_find_replace(
    fname: str, find_sent_regex: str, find_str_regex: str, replace_str: str
):
    if fname.is_file():
        with open(fname, "r") as f:
            lines = f.readlines()

        with open(fname, "w") as f:
            for i, line in enumerate(lines):
                if bool(re.search(find_sent_regex, line)):
                    find_sent = re.search(find_sent_regex, line)
                    if find_sent:
                        find_sent = find_sent.group()
                        logging.debug(f"Found sentence: {find_sent}")

                        # if find_str == replace_str: continue
                        logging.debug(f"Find string regex: {find_str_regex}")
                        find_replace_str = re.search(find_str_regex, find_sent)
                        if find_replace_str:
                            find_replace_str = find_replace_str.group()
                            logging.debug(
                                f"Found str within sentence: {find_replace_str.strip()}"
                            )

                            logging.debug(f"Replace str: {replace_str}")
                            line = line.replace(find_replace_str, replace_str)
                            logging.debug(f"Updated: {line.strip()}")

                        else:
                            logging.debug(f"Not found: {find_replace_str}")
                    else:
                        logging.debug(f"Not found: {find_sent_regex}")

                f.write(line)
