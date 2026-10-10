"""Entry point: python analyze.py <data-dir> <out-dir>

Writes out/proposal.md, out/sources.json and out/model_log.jsonl (see README.md).
"""
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: python analyze.py <data-dir> <out-dir>", file=sys.stderr)
        return 2
    data_dir, out_dir = sys.argv[1], sys.argv[2]
    print(f"not implemented yet (data: {data_dir}, out: {out_dir})", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
