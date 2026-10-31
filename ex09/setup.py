"""Build configuration for the ft_package distribution."""

import sys

from setuptools import find_packages, setup


def main() -> None:
    """Configure the package metadata and report build failures."""
    try:
        setup(
            name="ft_package",
            version="0.0.1",
            description="A sample test package",
            author="ocartier",
            author_email="ocartier@42.fr",
            license="MIT",
            license_files=("LICENSE",),
            long_description=(
                "A sample test package providing count_in_list."
            ),
            package_dir={"": "src"},
            packages=find_packages(where="src"),
            python_requires=">=3.9",
            install_requires=[],
        )
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as error:
        print(f"{type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
