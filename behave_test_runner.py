import sys
import os
import subprocess
from common.log_config import configure_logger
from common.generic_utils import *

logger = configure_logger(__name__)


def main(max_retries, test_suite_path, results_path):
    # Run the initial tests
    rerun_feature_filename = find_test_suite_rerun_file_name(
        test_suite_path, suffix=".feature"
    )
    cmd = [
        "behave",
        test_suite_path,
        "-f",
        "allure_behave.formatter:AllureFormatter",
        "-o",
        results_path,
        "--no-capture",
        "--tags=-skip",
        "-f",
        "rerun",
        "-o",
        rerun_feature_filename,
    ]
    logger.debug("Initial command: " + " ".join(cmd))  # Log the initial command
    init_result = subprocess.run(cmd)
    retry_result = 0

    if init_result.returncode != 0:
        retry_result = 1
        for i in range(max_retries):
            retry_cmd = [
                "behave",
                f"@{rerun_feature_filename}",
                "-f",
                "allure_behave.formatter:AllureFormatter",
                "-o",
                results_path,
                "--no-capture",
            ]
            logger.debug(
                f"Retry command, attempt {i + 1}: " + " ".join(retry_cmd)
            )  # Log retry command
            retry_result = subprocess.run(retry_cmd)

            if retry_result.returncode != 0:
                logger.debug(f"Test failed attempt {i+1}.")
                continue
            else:
                logger.debug(f"Test succeeded {i+1}.")
                break
    else:
        logger.debug(f"All tests passed on initial attempt.")

    # Clean up rerun file if it exists
    if retry_result and retry_result.returncode != 0:
        logger.debug(f"Tests failed even after {max_retries} retry attempts.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        logger.debug(
            "Usage: python behave_test_runner.py <max_retries> <test_suite_path> <results_path>"
        )
        sys.exit(1)

    max_retries = int(sys.argv[1])
    test_suite_path = sys.argv[2]
    results_path = sys.argv[3]

    main(max_retries, test_suite_path, results_path)
