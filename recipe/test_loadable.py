from openff.toolkit import ForceField

for off_improper in [True]:
    for version in range(1, 5):
        ForceField(
            f"ff14sb_{'off_impropers_' if off_improper else ''}"
            f"0.0.{version}.offxml"
        )
