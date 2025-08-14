import zipfile
from pathlib import Path


def create_zip(output_zip, files_to_add):
    """
    Create a zip file from a list of files.

    Parameters
    ----------
    output_zip : str or Path
        Path for the output ZIP file.
    files_to_add : list of tuple
        List of (source_path, archive_name) tuples.
        If archive_name is None, the original filename is used.
    """
    output_zip = Path(output_zip)

    with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for src, arcname in files_to_add:
            src_path = Path(src)
            if not src_path.is_file():
                print(f"Skipping missing file: {src_path}")
                continue
            if arcname is None:
                arcname = src_path.name
            zipf.write(src_path, arcname)
            print(f"Added {src_path} as {arcname}")


if __name__ == "__main__":

    baseline_protocol_files = [
        ("BloodVolumeControl.cellml", None),
        ("BloodVolumeControl.sedml", None),
        ("manifest.xml", None),
        ("simulation.json", None)
    ]

    eat_drink_protocol_files = [
        ("BloodVolumeControl.cellml", None),
        ("EatDrink.sedml", None),
        ("manifest-EatDrink.xml", "manifest.xml"),
        ("simulation-EatDrink.json", "simulation.json")
    ]

    create_zip("baseline-simulation.omex", baseline_protocol_files)
    print("ZIP file created: baseline-simulation.omex")

    create_zip("eat-drink-simulation.omex", eat_drink_protocol_files)
    print("ZIP file created: eat-drink-simulation.omex")