from pathlib import Path

from tm2p._intern import Params


def report_matches(
    params: Params,
    mapping: dict[str, list[str]],
) -> None:

    filepath = (
        Path(params.root_directory) / "refine" / "thesaurus" / "candidate_matches.txt"
    )
    filepath.parent.mkdir(parents=True, exist_ok=True)

    keys = list(mapping.keys())
    sorted_keys = sorted(keys, key=lambda x: (x.split(" ")[-1], x), reverse=True)

    with open(filepath, "w", encoding="utf-8") as f:
        for preferred in sorted_keys:
            variants = mapping[preferred]
            variants = sorted(
                variants, key=lambda x: (x.split(" ")[-1], x), reverse=True
            )
            f.write(f"{preferred}\n")
            for variant in variants:
                f.write(f"    {variant}\n")
