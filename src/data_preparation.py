from pathlib import Path
import random
import shutil


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "data" / "Eliteserien"
OUTPUT_DIR = BASE_DIR / "data" / "Eliteserien_partitioned"

YEARS = ["2021", "2022", "2023"]
TRAIN_SIZE = 175
VAL_SIZE = 25
TEST_SIZE = 50
RANDOM_SEED = 42

FILE_TYPES = {
    "frames": {
        "extension": ".jpg",
        "target_folder": "images"
    },
    "detection": {
        "extension": ".txt",
        "target_folder": "labels"
    }
}


def collect_sample_ids(year: str) -> list[str]:
    """
    Collect all sample IDs for a given year.
    """

    frame_dir = DATASET_DIR / year / "frames"

    sample_ids = []

    for match_dir in frame_dir.iterdir():

        if not match_dir.is_dir():
            continue

        for image_file in match_dir.iterdir():
            sample_ids.append(image_file.stem)

    return sample_ids


def create_splits(sample_ids: list[str]) -> dict[str, list[str]]:
    """
    Create train, validation and test splits.
    """

    expected_samples = TRAIN_SIZE + VAL_SIZE + TEST_SIZE

    if len(sample_ids) < expected_samples:
        raise ValueError(
            f"Expected at least {expected_samples} samples, "
            f"but found {len(sample_ids)}."
        )

    random.seed(RANDOM_SEED)
    random.shuffle(sample_ids)

    return {
        "train": sample_ids[:TRAIN_SIZE],
        "val": sample_ids[
            TRAIN_SIZE:
            TRAIN_SIZE + VAL_SIZE
        ],
        "test": sample_ids[
            TRAIN_SIZE + VAL_SIZE:
            TRAIN_SIZE + VAL_SIZE + TEST_SIZE
        ]
    }


def copy_sample(year: str, sample_id: str, split: str) -> None:
    """
    Copy image and label files to YOLO structure.
    """

    match_id = sample_id.split("_")[0]

    for source_folder, metadata in FILE_TYPES.items():

        source_file = (
            DATASET_DIR
            / year
            / source_folder
            / match_id
            / f"{sample_id}{metadata['extension']}"
        )

        if not source_file.exists():
            continue

        destination_dir = (
            OUTPUT_DIR
            / metadata["target_folder"]
            / split
        )

        destination_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            source_file,
            destination_dir / source_file.name
        )


def partition_dataset() -> None:
    """
    Partition the dataset into train, validation and test sets.
    """

    if not DATASET_DIR.exists():
        print(f"Dataset directory not found: {DATASET_DIR}")
        return

    print("Starting dataset partitioning...\n")

    for year in YEARS:

        sample_ids = collect_sample_ids(year)

        if not sample_ids:
            print(f"No samples found for {year}")
            continue

        splits = create_splits(sample_ids)

        for split_name, samples in splits.items():

            for sample_id in samples:
                copy_sample(
                    year,
                    sample_id,
                    split_name
                )

        print(
            f"{year}: {len(sample_ids)} samples processed"
        )

    original_images = len(
        list(DATASET_DIR.rglob("*.jpg"))
    )

    partitioned_images = len(
        list(OUTPUT_DIR.rglob("*.jpg"))
    )

    print("\nPartition summary")
    print(f"Original images: {original_images}")
    print(f"Partitioned images: {partitioned_images}")
    print(
        f"Integrity check: "
        f"{original_images == partitioned_images}"
    )


if __name__ == "__main__":
    partition_dataset()