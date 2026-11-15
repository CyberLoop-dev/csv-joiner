import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def read_csv(path: Path, key: str):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"{path} has no header row")
        if key not in reader.fieldnames:
            raise ValueError(f"Key column {key!r} is missing from {path}")
        return list(reader.fieldnames), list(reader)


def join_rows(left_fields, left_rows, right_fields, right_rows, key, how="left"):
    if how not in {"left", "inner", "full"}:
        raise ValueError("how must be left, inner, or full")
    output_fields = [key]
    output_fields += [f"left_{field}" for field in left_fields if field != key]
    output_fields += [f"right_{field}" for field in right_fields if field != key]
    right_index = defaultdict(list)
    for row in right_rows:
        right_index[row.get(key, "")].append(row)
    left_keys = set()
    output = []

    def combine(left, right, key_value):
        item = {key: key_value}
        for field in left_fields:
            if field != key:
                item[f"left_{field}"] = (left or {}).get(field, "")
        for field in right_fields:
            if field != key:
                item[f"right_{field}"] = (right or {}).get(field, "")
        return item

    for left in left_rows:
        value = left.get(key, "")
        left_keys.add(value)
        matches = right_index.get(value, [])
        if matches:
            output.extend(combine(left, right, value) for right in matches)
        elif how in {"left", "full"}:
            output.append(combine(left, None, value))
    if how == "full":
        for right in right_rows:
            value = right.get(key, "")
            if value not in left_keys:
                output.append(combine(None, right, value))
    return output_fields, output


def join_files(left_path, right_path, key, how, output_path):
    left_fields, left_rows = read_csv(left_path, key)
    right_fields, right_rows = read_csv(right_path, key)
    fields, rows = join_rows(left_fields, left_rows, right_fields, right_rows, key, how)
    output_path = Path(output_path)
    if output_path.exists():
        raise FileExistsError(f"Output already exists: {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Join two CSV files by a shared key column.")
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    parser.add_argument("--key", required=True)
    parser.add_argument("--how", choices=["left", "inner", "full"], default="left")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        count = join_files(args.left, args.right, args.key, args.how, args.output)
        print(f"Wrote {count} joined row(s) to {args.output}")
        return 0
    except (OSError, ValueError, csv.Error) as error:
        print(f"csv-joiner: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
