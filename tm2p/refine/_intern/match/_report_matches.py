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

    with open(filepath, "w", encoding="utf-8") as f:
        for preferred, variants in mapping.items():
            f.write(f"{preferred}\n")
            for variant in variants:
                f.write(f"    {variant}\n")
